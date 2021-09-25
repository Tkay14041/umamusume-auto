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

    @property
    @abstractmethod
    def training_home(self):
        pass

    @property
    @abstractmethod
    def next_button(self):
        pass

    @property
    @abstractmethod
    def race_button(self):
        pass

    @property
    @abstractmethod
    def training_completion_button(self):
        pass
