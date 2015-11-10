from flask.ext.restful import Resource
from flask import jsonify
from models.door import Door
from drivers.stepper import *

class DoorAPI(Resource):
    def get(self):
        door = Door()
        return jsonify({'lock': door.is_locked})

class LockAPI(Resource):
    def post(self):
        door = Door()
        if door.lock():
            forward(0.003, 256)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})


class UnlockAPI(Resource):
    def post(self):
        door = Door()
        if door.unlock():
            backward(0.003, 256)
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})
