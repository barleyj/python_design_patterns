from design_patterns.singleton import SingletonMeta

def test_singleton():
    class Test():
        __metaclass__=SingletonMeta

        def __init__(self, value):
            self.value = value


    t1 = Test('t1')
    t2 = Test('t2')

    assert t1.value == t2.value


def test_instance():
    class Test():
        __metaclass__=SingletonMeta

        def __init__(self, value):
            self.value = value


    t1 = Test('t1')
    t2 = Test('t2')

    assert t1.instance == t2.instance
