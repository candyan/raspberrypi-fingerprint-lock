from flask.views import MethodView
from drivers.stepper import *

class LockAPI(MethodView):

    def post(self):
        print "f"
        forward(0.003, 256)


class UnlockAPI(MethodView):

    def post(self):
        print "b"
        backward(0.003, 256)
