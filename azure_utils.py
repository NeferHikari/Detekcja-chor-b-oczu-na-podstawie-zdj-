from azure.keyvault.secrets import SecretClient
from azure.indentity import DefaultAzureCredential
import requests

KEY_VAULT_URI = "" # TODO add key vault public uri
MODEL_URL_SECRET_NAME = "" # TODO add model url secret name
PRED_HEADERS = {"Content-Type": "application/octet-stream"}
JSON_PREDICTION_NAME = "predictions"

sc = SecretClient(vault_url=KEY_VAULT_URI, credential=DefaultAzureCredential())
model_url = sc.get_secret(MODEL_URL_SECRET_NAME).value

def get_prediction(img):
    response = requests.post(model_url, img, headers=PRED_HEADERS)
    prediction = response.json().get(JSON_PREDICTION_NAME)
    return prediction