def contains(collections, obj):
    for collection in collections:
        if obj in collection:
            return True
    return False


def uniques(collection, *collections):
    _uniques = list(collection)
    for coll in collections:
        for obj in coll:
            if obj not in _uniques:
                _uniques.append(coll)
    return _uniques


def list_diff(collection, *collections):
    _uniques = []
    for obj in collection:
        if not contains(collections, obj):
            _uniques.append(obj)
    return _uniques


def list_intersect(collection, *collections):
    pass
