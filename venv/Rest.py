from flask import Flask, request , jsonify
from flask_restful import Resource, Api
import json
import urllib.request


app = Flask(__name__)
api = Api(app)

camera = {
    "speed": "1000",
    "f": "2.8",
    "iso": "1800",
    "ldr": "0"
}

arduino = {
    "Water_Drop": "1"
}



print(camera)

class Camera(Resource):
    def get(self, speed, f, iso):
        if camera[speed] is not None and camera[f] is not None and camera[iso] is not None:
            return jsonify(camera)

    # def get(self, speed):
    #     return camera["speed"]

    # def put(self):
    #     data = request.get_json()
    #     camera["speed"]:(data)
    #     return camera

    def put(self,speed):
        data = request.get_json()
        # camera.update(data)
        # camera["speed"] = speed
        return data

class Arduino(Resource):
    def get(self,Water_Drop):
        return jsonify (arduino)

    def put(self, Water_Drop):
        data1 = request.get_json()
        arduino.update(data1)
        # camera["speed"] = speed
        return jsonify(arduino)



api.add_resource(Camera,'/Camera/<string:speed>/<string:f>/<string:iso>')
# api.add_resource(light,'/light/<string:l>')
api.add_resource(Arduino,'/Arduino/<string:Water_Drop>')



app.run(host='192.168.50.22', port=5000)
