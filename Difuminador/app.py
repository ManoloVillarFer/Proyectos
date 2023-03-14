"""
Nombre del Programa: app
Author: Francisco Manuel Villar Fernández
"""

# Importamos lo necesario
import base64
import boto3
import os
from flask import Flask, request, Response, abort
from dotenv import load_dotenv
from blur_faces import anonymize_face
from detect_faces import detect_faces

# Cargamos del fichero .env (Con nuestras claves)
load_dotenv()

accessKeyId = os.environ.get('ACCESS_KEY_ID')
secretKey = os.environ.get('ACCESS_SECRET_KEY')
sessionToken = os.environ.get('SESSION_TOKEN')
bucket_source = os.environ.get('BUCKET_SOURCE')
bucket_destination = os.environ.get('BUCKET_DEST')
region = os.environ.get('REGION')

# Uso de la API de S3
s3 = boto3.Session(
    aws_access_key_id=accessKeyId,
    aws_secret_access_key=secretKey,
    aws_session_token=sessionToken,
    region_name=region).resource('s3')

app = Flask(__name__)


# Función principal para difuminar caras cogiendo del bucket inicio al destino
@app.route('/api/analyze', methods=['POST'])
def analyze_image():
    key = request.get_json()['key']
    # Si no se mete imagen
    if key is None:
        abort(400)
    try:
        response = detect_faces(key)

        file_object = s3.Object(bucket_source, key).get()
        file_content = file_object['Body'].read()
        buffer_anon_img = anonymize_face(file_content, response)

        img_enc = base64.b64encode(buffer_anon_img)
        img_dec = base64.b64decode(img_enc)
        s3.Object(bucket_destination, f"Caras Difuminadas_{key}").put(Body=img_dec)
    except Exception as error:
        print(error)
        abort(500)
    return Response(status=200)


# Ejecutamos Flask
if __name__ == "__main__":
    app.run(debug=True)
