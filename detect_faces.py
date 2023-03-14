"""
Nombre del Programa: detect_faces
Author: Francisco Manuel Villar Fernández
"""

# Importamos lo necesario
import boto3
import os
from dotenv import load_dotenv

# Cargamos del fichero .env (Con nuestras claves)
load_dotenv()

accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
sessionToken = os.environ.get('SESSION_TOKEN')
bucket_source = os.environ.get('BUCKET_SOURCE')
region = os.environ.get('REGION')

# Uso de la API Rekognition
rekognition_client = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey,
    aws_session_token=sessionToken,
    region_name=region).client('rekognition')


# Función para detectar caras
def detect_faces(img):
    try:
        response = rekognition_client.detect_faces(
            Image={'S3Object': {'Bucket': bucket_source, 'Name': img}}, Attributes=['DEFAULT'])
        print("Se ha reconocido la imagen")
    except Exception:
        raise Exception("Ha ocurrido un error reconociendo la imagen")
    return response
