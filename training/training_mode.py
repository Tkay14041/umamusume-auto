# -*- coding: utf-8 -*-
from enum import Enum, unique

from image.image import Image


@unique
class TrainingMode(Enum):
    AOHARU = ('aoharu', Image('resources/image/training_mode/aoharu_mode.jpg'))

    def __init__(self, name: str, image: Image):
        self._name = name
        self._image = image

    @property
    def image(self):
        return self._image
