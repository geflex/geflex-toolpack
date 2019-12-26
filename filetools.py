import os, shutil


def filenames(path):
    return next(os.walk(path))[2]


def dirnames(path):
    return next(os.walk(path))[1]


def filepaths(path):
    for filename in filenames(path):
        yield os.path.join(path, filename)


def dirpaths(path):
    for dirname in dirnames(path):
        yield os.path.join(path, dirname)


def clrdir(path):
    for name in os.listdir(path):
        filepath = os.path.join(path, name)
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)


def ext_split(path):
    try:
        path, ext = path.rsplit('.', 1)
        return path, ext
    except ValueError:
        return path, None


def get_ext(path):
    return ext_split(path)[1]
