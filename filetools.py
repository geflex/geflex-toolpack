import os, shutil


__all__ = 'filenames', 'dirnames', 'filepaths', 'dirpaths', 'reader', 'clrdir', 'ext_split', 'get_ext'


def _filt_pathnames(path, filt):
    return (p for p in os.listdir(path) if filt(os.path.join(path, p)))


def _filt_paths(path, filt):
    for name in os.listdir(path):
        filepath = os.path.join(path, name)
        if filt(filepath):
            yield filepath


def filenames(path):
    return _filt_pathnames(path, os.path.isfile)


def dirnames(path):
    return _filt_pathnames(path, os.path.isdir)


def filepaths(path):
    """yields paths to the files in folder"""
    return _filt_paths(path, os.path.isfile)


def dirpaths(path):
    """yields paths to the dirs in folder"""
    return _filt_paths(path, os.path.isdir)


def reader(path, func):
    for filename in filenames(path):
        filepath = os.path.join(path, filename)
        obj = func(filepath)
        yield obj, filename


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
