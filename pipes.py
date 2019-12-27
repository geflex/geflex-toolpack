import os
from abc import ABC, abstractmethod
from typing import *
from .filetools import filenames, clrdir


__all__ = 'Saver', 'Cacher', 'IO', 'Pipe'


class IO(ABC):
    @staticmethod
    @abstractmethod
    def load(path: str):
        """
        this method should load object from file and return it
        :param path: full(or relative) path to the file
        :return: loaded object
        """
        pass

    @staticmethod
    @abstractmethod
    def save(obj, path):
        """
        this method should dump object to the file
        :param obj: object that should be saved
        :param path: full(or relative) path to the file
        :type path: str
        """
        pass


class Saver:
    def __init__(self, path, func):
        self.path = path
        self.save_func = func

    def __call__(self, obj, name):
        filepath = os.path.join(self.path, name)
        self.save_func(obj, filepath)
        return self


class Cacher:
    def __init__(self, path, func, io):
        self.path = path
        self.func = func
        self.io = io

    def __call__(self, obj, name):
        """
        transforms an object with .func and caches result
        if result is already in cache returns it instead

        :param obj: obj that should be transformed
        :param name: name of the object that identifies it in cache
        :return: transformed object

        :type name: str
        """
        if self.path is None:
            return self.func(obj)

        cached_file_path = os.path.join(self.path, name)
        if name not in filenames(self.path):
            obj = self.func(obj)
            self.io.save(obj, cached_file_path)
            return obj
        else:
            return self.io.load(cached_file_path)


class Pipe:
    def __init__(self, generator, *transforms, caching=True, rewrite=False):
        """

        :type generator: Iterable[Tuple[Any, str]]
        :type transforms: Tuple[Union[Callable[[Any], Any], Saver, CacheableCommand]]
        :type caching: bool
        :type rewrite: bool
        """
        self.generator = generator
        self.transforms = transforms
        self.caching = caching
        if rewrite:
            self.clear_caches()

    def clear_caches(self):
        for trans in self.transforms:
            if isinstance(trans, (Saver, Cacher)):
                clrdir(trans.path)

    def process(self, obj, name):
        """process one object"""
        for trans in self.transforms:
            if isinstance(trans, Cacher):
                if self.caching:
                    obj = trans(obj, name)
                else:
                    obj = trans.func(obj)
            elif isinstance(trans, Saver):
                trans(obj, name)
            else:
                obj = trans(obj)
        return obj

    def __iter__(self):
        for obj, name in self.generator:
            yield self.process(obj, name), name
