from flask import Flask
from flask.ext.restful import Api
from views.door import *

app = Flask(__name__)
api = Api(app)

app.debug = True

api.add_resource(DoorAPI, '/api/door', endpoint = 'door')
api.add_resource(LockAPI, '/api/door/lock', endpoint = 'lock')
api.add_resource(UnlockAPI, '/api/door/unlock', endpoint = 'unlock')

if __name__=='__main__':
    app.run(host='0.0.0.0')
