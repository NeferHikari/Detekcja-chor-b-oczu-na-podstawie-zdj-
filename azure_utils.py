from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import requests

MODEL_URL_SECRET_NAME = "model-url" # TODO add model url secret name
PRED_HEADERS = {"Content-Type": "application/octet-stream"}
JSON_PREDICTION_NAME = "predictions"

def get_prediction(img):
    response = requests.post("model_url", img, headers=PRED_HEADERS)
    prediction = response.json().get(JSON_PREDICTION_NAME)
    return prediction