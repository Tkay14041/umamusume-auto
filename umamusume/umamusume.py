# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Umamusume(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def thumbnail(self):
        pass
