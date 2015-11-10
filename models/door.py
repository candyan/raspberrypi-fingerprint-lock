from utils.decorator import singleton
from store import r as redis

DOOR_LOCK_KEY = "fingerprint-lock:door:lock"

@singleton
class Door(object):
    def __init__(self):
        self._lock = (redis.get(DOOR_LOCK_KEY) == "1")

    @property
    def is_locked(self):
        return self._lock

    def lock(self):
        if (self.is_locked == False) and redis.set(DOOR_LOCK_KEY, 1):
            self._lock = True
            return True
        else:
            return False

    def unlock(self):
        if self.is_locked and redis.set(DOOR_LOCK_KEY, 0):
            self._lock = False
            return True
        else:
            return False
