
import gradio as gr
import joblib
import pandas as pd
import numpy as np

# Load model bundle
bundle = joblib.load("rf_model_bundle.pkl")
model = bundle["model"]
threshold = bundle["threshold"]

# Prediction function
def predict_fraud(step, amount, oldbalanceOrig, newbalanceOrig,
                  oldbalanceDest, newbalanceDest,
                  nameDest_freq, nameDest_fraud_rate,
                  type, OrigEmptyBefore, OrigEmptyAfter, DestEmptyBefore, DestEmptyAfter):

    balanceChangeOrig = oldbalanceOrig - newbalanceOrig
    balanceChangeDest = newbalanceDest - oldbalanceDest

    X = pd.DataFrame([{
        "step": step,
        "amount": amount,
        "oldbalanceOrig": oldbalanceOrig,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "balanceChangeOrig": balanceChangeOrig,
        "balanceChangeDest": balanceChangeDest,
        "nameDest_freq": nameDest_freq,
        "nameDest_fraud_rate": nameDest_fraud_rate,
        "type": type,
        "OrigEmptyBefore": OrigEmptyBefore,
        "OrigEmptyAfter": OrigEmptyAfter,
        "DestEmptyBefore": DestEmptyBefore,
        "DestEmptyAfter": DestEmptyAfter
    }])

    prob = model.predict_proba(X)[0][1]
    pred = int(prob >= threshold)
    return f"{'🚨 Fraud' if pred else '✅ Not Fraud'} (Probability: {prob:.2f})"

# Gradio UI
demo = gr.Interface(
    fn=predict_fraud,
    inputs=[
        gr.Number(label="Transaction Step", info="Time unit since system start"),
        gr.Number(label="Transaction Amount ($)", info="Total amount of the transaction"),
        gr.Number(label="Sender's Balance Before", info="Balance before transaction"),
        gr.Number(label="Sender's Balance After", info="Balance after transaction"),
        gr.Number(label="Recipient's Balance Before", info="Recipient balance before transaction"),
        gr.Number(label="Recipient's Balance After", info="Recipient balance after transaction"),
        gr.Number(label="Recipient Account Frequency", info="Number of prior transactions to recipient"),
        gr.Number(label="Recipient Fraud Rate", info="Historical fraud rate for recipient (0–1)"),
        gr.Radio(["CASH_OUT", "TRANSFER", "PAYMENT", "CASH_IN"], label="Transaction Type", info="CASH_OUT & TRANSFER are riskier"),
        gr.Radio([0, 1], label="Sender Balance Empty Before?", info="1 = Yes, 0 = No"),
        gr.Radio([0, 1], label="Sender Balance Empty After?", info="1 = Yes, 0 = No"),
        gr.Radio([0, 1], label="Recipient Balance Empty Before?", info="1 = Yes, 0 = No"),
        gr.Radio([0, 1], label="Recipient Balance Empty After?", info="1 = Yes, 0 = No"),
    ],
    outputs="text",
    title="💸 Fraud Detection App (Random Forest)",
    description="Enter transaction data to predict the likelihood of fraud using a trained ML model.",
)

demo.launch()
