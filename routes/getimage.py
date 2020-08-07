#!/usr/bin/python3
""" ruta donde llegara  las imagenes """

from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__)

@home_bp.route('/photos/<imagen>', methods=['POST'])
def getImages(imagen):
    print(imagen)
    return jsonify({'STATUS': 'OK'})
    