
_singletons = {}


def get_instance(cls, *args, **kwargs):
    if cls.instance == None:
        cls.instance = _singletons[cls](cls, *args, **kwargs)

    return cls.instance

                    
class SingletonMeta(type):
    def __init__(cls, name, bases, dct):
        super(SingletonMeta, cls).__init__(name, bases, dct)
        
        if cls not in _singletons:
            _singletons[cls] = cls.__new__

        cls.instance = None
        cls.__new__ = staticmethod(get_instance)
