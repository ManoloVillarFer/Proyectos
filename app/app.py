"""
Nombre del Programa: app.py
Realizar una web (sencilla) que transforme de texto a voz usando AWS Polly.

Esta web presenta un formulario que pide un modelo de voz entre las opciones disponibles en Polly
y el texto a transformar.

El formulario se envía a una aplicación Flask que será la encargada de hacer el proceso. En principio el mp3 se almacena
en un bucket, a partir de aquí haz las mejoras que se te ocurran para facilitar al usuario esta conversión.
Author: Francisco Manuel Villar Fernández
"""

from flask import Flask, render_template, request
import boto3

# Creamos el cliente de polly y ponemos las credenciales de AWS
# Esto consume tiempo de servicio
polly_client = boto3.Session(
    aws_access_key_id='ASIASWLAWU6ZFQMY3M6W',
    aws_secret_access_key='QKB8VoPQB3qo1BRlMlEDUk0O047Kz/BdrGDRyR8F',
    aws_session_token='FwoGZXIvYXdzEO7//////////wEaDKBINnqeLXZB3+txzCLIAeZWPAs7GfTmLqa75TjuzBvkB+jhq6EiHGVT36h0KY6ws7xZqoMW7DeqsVcDSJ0ubPYagiv+p0SDpC39acG4LCfX/9bC33ZjhFfnriEBX6iE2uAq/h15pi34p3Gar4kgoGzpxO9XC9QnSjoRuEy9DSX1y2GkKhgcGbTq7WQZWf2UhYb8BzmA7UN2R7zoa4VlogylCTOLE/j+2uAswiM5GRyFqCIVoTUCvy+MTQAkK2hzSdqKf1f6HiV+Pn58wUZHJJRQZYL/mJcoKKqfmp4GMi1ztFtDHpSu2/gNTfLuu+Oxf6pX+d5kSzJ8FE5xBCNJSSYOCSRdIyFENREop2Y=',
    region_name='us-east-1').client('polly')

# Creamos el archivo de audio
app = Flask(__name__, template_folder="./")


@app.route('/')
def inicio():
    return render_template("./index.html")


@app.route('/proceso', methods=['POST'])
def proceso():
    voices = request.form['voces']
    text_to_synthesize = request.form.get("texto")
    polly_client.start_speech_synthesis_task(
        VoiceId=voices,
        OutputS3BucketName='ceiabd-bucket2',
        OutputFormat='mp3',
        Text=text_to_synthesize,
        TextType='text',
        SampleRate='22050')


if __name__ == "__main__":
    app.run()
