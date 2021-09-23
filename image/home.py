# -*- coding: utf-8 -*-
from pathlib import Path

from image.image import Image


class Home:

    def __init__(self):
        self.training_button = Image(Path('resources/image/home/training_button.jpg'))
