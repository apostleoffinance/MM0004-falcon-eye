# Fraud Detection Deployment

This folder contains the files used to deploy the trained model as a live app on Hugging Face Spaces using Gradio.

## 🚀 Try the App

👉 [Open the App on Hugging Face](https://huggingface.co/spaces/Adriana213/fraud-predictor)

## 🧩 Files

- `app.py`: The full Gradio interface including preprocessing, prediction logic, and threshold
- `rf_model_bundle.pkl`: The trained pipeline (preprocessor + feature selector + classifier)
- `requirements.txt`: Dependencies for the Hugging Face Space

## 💡 Notes

- The app uses all 15 original input features (as expected by the model pipeline)
- Threshold was optimized for best F1-Score based on test set evaluation