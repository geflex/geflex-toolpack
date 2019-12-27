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
    items = []
    for obj in collection:
        if not contains(collections, obj):
            items.append(obj)
    return items


def list_intersect(collection, *collections):
    items = []
    for obj in collection:
        if contains(collections, obj):
            items.append(obj)
    return items
