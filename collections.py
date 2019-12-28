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
