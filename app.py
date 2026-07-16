import streamlit as st
import pandas as pd
import numpy as np
import torch
from stable_baselines3 import PPO
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
# -------------------------------
# Load trained PPO model
# -------------------------------
ppo_model = PPO.load("Saved Model")

# Load scaler and feature columns (SAVE THESE DURING TRAINING!)
scaler = torch.load("scaler.pt")        # you must save scaler
feature_columns = torch.load("features.pt")  # list(X.columns)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="DRL IDS PPO", layout="centered")

with st.container(border=True):
    st.markdown(
        """
        <h1 style='
            text-align: center;
            color: #1f4fd8;
            font-weight: 700;
            margin-bottom: 10px;
        '>
        🛡️ Intrusion Detection System
        </h1>
        """,
        unsafe_allow_html=True
    )

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader("Upload Network Traffic Data", type=["csv"])


# -------------------------------
# Prediction function
# -------------------------------
def predict_single_row(model, row):
    obs = row.values.reshape(1, -1)
    obs_tensor = torch.tensor(obs).float()

    with torch.no_grad():
        dist = model.policy.get_distribution(obs_tensor)
        probs = dist.distribution.probs.cpu().numpy()[0]

    pred_class = np.argmax(probs)
    confidence = probs[pred_class] * 100

    return {
        "Prediction": "Attack" if pred_class == 1 else "Normal",
        "Normal Probability (%)": round(probs[0] * 100, 2),
        "Attack Probability (%)": round(probs[1] * 100, 2),
        "Confidence (%)": round(confidence, 2)
    }

# -------------------------------
# Main Logic
# -------------------------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.sidebar.subheader("📊 Uploaded Dataset Preview")
    st.sidebar.dataframe(df.head())

    #plot the distribution of the label column if it exists
    if 'label' in df.columns:
        st.sidebar.subheader("📈 Label Distribution")
        st.sidebar.bar_chart(df['label'].value_counts())


    # Drop optional columns safely
    df.drop(['id', 'attack_cat', 'label'], axis=1, inplace=True, errors='ignore')

    # One-hot encode
    df = pd.get_dummies(df)

    # -------------------------------
    # Dataset compatibility check
    # -------------------------------
    if not set(feature_columns).issubset(set(df.columns)):
        st.error("❌ Dataset Mismatch: Uploaded dataset does not match trained model features")
        st.stop()

    # Align columns
    df = df.reindex(columns=feature_columns, fill_value=0)

    # Scale
    df_scaled = scaler.transform(df)

    # -------------------------------
    # Single-row prediction
    # -------------------------------
    if df_scaled.shape[0] == 1:
        result = predict_single_row(
            ppo_model,
            pd.Series(df_scaled[0])
        )

        st.subheader("🔍 Prediction Result")
        st.json(result)

    # -------------------------------
    # Multiple-row prediction
    # -------------------------------
    else:
        col1,col2,col3 = st.columns([1,6,1])
        row_index = st.slider(
            "🔢 Enter row number for prediction",
            min_value=0,
            max_value=df_scaled.shape[0] - 1,
            step=1
        )
        st.sidebar.write("📌 Selected Row Data:")
        st.sidebar.dataframe(df.iloc[row_index:row_index+1])

        if st.button("Predict",type="primary"):
            #disaply the selected row
            
            result = predict_single_row(
                ppo_model,
                pd.Series(df_scaled[row_index])
            )

            st.subheader("🔍 Prediction Result")
            st.write(f"📌 Selected Row: {row_index}")
            with st.container(border=True):
                col1, col2 = st.columns([1, 1.5])

                # ------------------ COLUMN 1 ------------------
                with col1:
                    st.markdown(
                        f"""
                        <div style="
                            background: rgba(0,0,0,0.1);
                            padding: 20px;
                            border-radius: 12px;
                            text-align: center;
                            color: white;
                        ">
                            <h2>🛡️ Prediction</h2>
                            <h1 style="color: {'#ff4b4b' if result['Prediction']=='Attack' else '#00c853'};">
                                {result['Prediction']}
                            </h1>
                            <h3>Confidence</h3>
                            <h2 style="color: blue;">
                                {result['Confidence (%)']}%
                            </h2>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                # ------------------ COLUMN 2 ------------------
                with col2:
                    labels = ["Normal", "Attack"]
                    values = [
                        result["Normal Probability (%)"],
                        result["Attack Probability (%)"]
                    ]
                    colors = ["green", "red"]

                    fig, ax = plt.subplots()
                    ax.bar(labels, values, color=colors)
                    ax.set_ylim(0, 100)
                    ax.set_ylabel("Probability (%)")
                    ax.set_title("Intrusion Probability Distribution")

                    for i, v in enumerate(values):
                        ax.text(i, v + 1, f"{v}%", ha="center", fontweight="bold")

                    st.pyplot(fig)

