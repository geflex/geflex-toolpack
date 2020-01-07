class GList(list):
    @staticmethod
    def contains(collections, obj):
        for collection in collections:
            if obj in collection:
                return True
        return False

    def uniques(self, *collections):
        _uniques = list(self)
        for coll in collections:
            for obj in coll:
                if obj not in _uniques:
                    _uniques.append(coll)
        return _uniques

    def diff(self, *collections):
        items = []
        for obj in self:
            if not GList.contains(collections, obj):
                items.append(obj)
        return items

    def intersect(self, *collections):
        items = []
        for obj in self:
            if GList.contains(collections, obj):
                items.append(obj)
        return items


class GDotDict(dict):
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__getitem__
    __getattr__ = dict.__getitem__


class ArgsKwargs:
    def __init__(self, *args, **kwargs):
        self.args = list(args)
        self.kwargs = kwargs

    def extend(self, *args, **kwargs):
        self.args.extend(args)
        self.kwargs = {**self.kwargs, **kwargs}

    def extended(self, *args, **kwargs):
        return self.__class__(*self.args, *args,
                              **self.kwargs, **kwargs)
