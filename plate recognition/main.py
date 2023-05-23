"""
Nombre del fichero: main.py
Autor: Francisco Manuel Villar Fernández
"""

# Libraries to import
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OPENALPR_CLOUD_API_URL = 'https://api.openalpr.com/v2/recognize?recognize_vehicle=1&country=eu'
OPENALPR_RESULTS = 'results'
OPENALPR_CANDIDATES = 'candidates'
OPENALPR_VEHICLE = 'vehicle'
OPENALPR_MAKE = 'make'
OPENALPR_MAKE_MODEL = 'make_model'
OPENALPR_COLOR = 'color'

# Function that takes the results obtained
def analyse_results(results):
    plate = results[OPENALPR_RESULTS][0][OPENALPR_CANDIDATES][0]['plate']
    region = results[OPENALPR_RESULTS][0]['region']
    name = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE][0]['name']
    model = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_MAKE_MODEL][0]['name']
    color = results[OPENALPR_RESULTS][0][OPENALPR_VEHICLE][OPENALPR_COLOR][0]['name']

    return plate, region, name, model, color

# Endpoint and method to get the results
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get the key and the image
            api_key = request.form['api_key']
            image = request.files['image']

            # Create the request to the API
            request_url = OPENALPR_CLOUD_API_URL + '&secret_key=' + api_key
            files = {'image': image}

            # We get the results to store
            response = requests.post(request_url, files=files)
            data = response.json()

            # We analyse the results
            plate, region, name, model, color = analyse_results(data)

            return render_template('result.html', plate=plate, region=region, name=name, model=model, color=color)

        except:
            return render_template('index.html', error='Error processing the image. Please try again.')

    return render_template('index.html', error=None)


if __name__ == "__main__":
    app.run()
