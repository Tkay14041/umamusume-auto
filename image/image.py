# -*- coding: utf-8 -*-
from pathlib import Path


class Image:

    def __init__(self, path_str: str):
        self._path = Path(path_str)

    @property
    def path(self):
        return self._path

    @property
    def str_path(self):
        return str(self._path.absolute())
