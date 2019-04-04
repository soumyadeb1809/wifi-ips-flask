# -*- coding: utf-8 -*-
"""
Created on Tue April 03 01:40:06 2019

@author: Soumya Deb
"""
from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS

from locations_helper import get_location_data


app = Flask(__name__)
CORS(app)


@app.route('/api/getLocation', methods=['GET'])
def location_controller():
    response = get_location_data()
    return make_response(jsonify(response), 200)


if __name__ == '__main__':
    port = 5000
    app.run(port=port, debug=True)
    print("Server running at port {}".format(port))

