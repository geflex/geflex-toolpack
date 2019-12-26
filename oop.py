from .core import *


class Singleton:
    def __init__(self):
        attrname = '__instance__'
        cls = self.__class__
        if not hasattr(cls, attrname):
            setattr(cls, attrname, self)


class _MethodWrapper:
    name: str
    func: callable

    def __init__(self, name):
        self.name = name
        self.func = None


def subclass(*classes, name=None):
    name = ifnone(name, str(classes))
    return type(name, classes, {})


def abstractattr(typehint):
    return typehint


def classattr(typehint):
    return typehint
