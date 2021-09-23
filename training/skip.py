# -*- coding: utf-8 -*-
from image.image import Image
from util import Util


class Skip:

    @staticmethod
    def prolog():
        Util.touch_image(Image('resources/image/training/skip_prolog.jpg'))

    @staticmethod
    def first():
        Util.touch_image(Image('resources/image/training/skip_off.jpg'))

    @staticmethod
    def second():
        Util.touch_image(Image('resources/image/training/skip_x1.jpg'))

    @staticmethod
    def decide():
        Util.touch_image(Image('resources/image/training/decide_button.jpg'))
