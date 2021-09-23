# -*- coding: utf-8 -*-
from image.image import Image
from umamusume.umamusume import Umamusume


class MejiroMcQueen(Umamusume):

    def __init__(self):
        self._name = 'メジロマックイーン'
        self._thumbnail = Image('resources/image/umamusume/mejiro_mcqueen/thumbnail.jpg')
        self._next_button = Image('resources/image/umamusume/mejiro_mcqueen/next_button.jpg')
        self._race_button = Image('resources/image/umamusume/mejiro_mcqueen/race_button.jpg')
        self._training_completion_button = Image('resources/image/umamusume/mejiro_mcqueen/training_complete_button.jpg')

    @property
    def name(self):
        return self._name

    @property
    def thumbnail(self):
        return self._thumbnail

    @property
    def next_button(self):
        return self._next_button

    @property
    def race_button(self):
        return self._race_button

    @property
    def training_completion_button(self):
        return self._training_completion_button
