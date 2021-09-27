# -*- coding: utf-8 -*-
from pathlib import Path

from image.image import Image


class Umamusume:

    def __init__(self, name: str):
        self._name = name
        image_path = Path('resources/image/umamusume').joinpath(self._name)
        assert image_path.is_dir()
        self._thumbnail = Image(str(image_path.joinpath('thumbnail.jpg')))
        self._next_button = Image(str(image_path.joinpath('next_button.jpg')))
        self._race_button = Image(str(image_path.joinpath('race_button.jpg')))
        self._training_completion_button = Image(str(image_path.joinpath('training_completion_button.jpg')))

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
