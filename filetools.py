import os, shutil


def filenames(path):
    return (p for p in os.listdir(path) if os.path.isfile(p))


def dirnames(path):
    return (p for p in os.listdir(path) if os.path.isdir(p))


def filepaths(path):
    """yields paths to the files in folder"""
    return (os.path.join(path, name) for name in os.listdir(path) if os.path.isfile(name))


def dirpaths(path):
    """yields paths to the dirs in folder"""
    return (os.path.join(path, name) for name in os.listdir(path) if os.path.isdir(name))


def clrdir(path):
    """remove all files from the dir"""
    for name in os.listdir(path):
        filepath = os.path.join(path, name)
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        elif os.path.isdir(filepath):
            shutil.rmtree(filepath)


def ext_split(path):
    """
    splits str on name ond extension
    if there are no extension returns name, None
    :returns: Tuple[str, Optional[str]]
    """
    try:
        path, ext = path.rsplit('.', 1)
        return path, ext
    except ValueError:
        return path, None


def get_ext(path):
    """
    return only extension of the file
    None if there are no extension
    """
    return ext_split(path)[1]
