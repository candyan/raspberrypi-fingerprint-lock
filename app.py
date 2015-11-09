from flask import Flask
from views.door import *

app = Flask(__name__)

door_lock_view = LockAPI.as_view('door_lock')
door_unlock_view = UnlockAPI.as_view('door_unlock')

app.add_url_rule('/api/door/lock/', view_func=door_lock_view, methods=['POST',])
app.add_url_rule('/api/door/unlock/', view_func=door_unlock_view, methods=['POST',])

if __name__=='__main__':
    app.run(host='0.0.0.0')
