"""
Nombre del fichero: main.py
Autor: Francisco Manuel Villar Fernández
"""
# Importamos las librerías necesarias
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = 'clave de openai'

@app.route('/')
def index():
    return render_template('index.html')

# Procesamos la traducción
@app.route('/translate', methods=['POST'])
def translate():
    # Texto ingresado por el usuario
    english_text = request.form['english_text']

    # Usamos la API de OpenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt = f'Translate the following English text to Spanish: {english_text}',
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
    )

    # Obtenemos la traducción
    translation = response.choices[0].text.strip()

    return render_template('results.html', translation=translation)

if __name__ == '__main__':
    app.run()
