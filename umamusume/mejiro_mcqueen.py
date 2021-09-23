# -*- coding: utf-8 -*-
from image.image import Image
from umamusume.umamusume import Umamusume


class MejiroMcQueen(Umamusume):

    def __init__(self):
        self._name = 'メジロマックイーン'
        self._thumbnail = Image('resources/image/umamusume/mejiro_mcqueen/thumbnail.jpg')

    @property
    def name(self):
        return self._name

    @property
    def thumbnail(self):
        return self._thumbnail
