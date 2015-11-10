def singleton(cls, *args, **kw):
    instances = {}
    def _sigleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _sigleton
