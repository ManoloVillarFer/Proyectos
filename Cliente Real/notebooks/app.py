"""
Nombre del fichero: app.py
Autor: Francisco Manuel Villar Fernández
"""
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Cargar el modelo guardado
with open('arbol_decision.pkl', 'rb') as file:
    clf_tree = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del body de la petición POST
    data = request.get_json(force=True)
    # Convertir los datos en un arreglo de numpy
    features = np.array(list(data.values())).reshape(1,-1)
    # Realizar la predicción con el modelo cargado
    prediction = clf_tree.predict(features)
    # Crear una respuesta en formato JSON con la predicción
    output = {'prediction': 'Se convertira en cliente real' if prediction[0] == 1 else 'No se convertira en cliente real'}
    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
