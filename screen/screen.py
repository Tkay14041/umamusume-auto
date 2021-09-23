# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

from image.image import Image


class Screen(ABC):

    @property
    @abstractmethod
    def image(self) -> Image:
        pass

    @property
    @abstractmethod
    def button(self) -> Image:
        pass
