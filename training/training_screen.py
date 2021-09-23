# -*- coding: utf-8 -*-
from image.image import Image
from screen.screen import Screen


class GoingOut(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/going_out.png')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class OptionSelection(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/option_2nd.png')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class FanNotEnough(Screen):

    def __init__(self):
        self._image = Image('resources/image/training/fan_not_enough.jpg')
        self._button = Image('resources/image/training/cancel_button.jpg')

    @property
    def image(self):
        return self._image

    @property
    def button(self):
        return self._button


class BeforeRace(Screen):

    def __init__(self, race_button: Image):
        self._button = race_button

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class FirstRaceSelection(Screen):

    def __init__(self):
        self._image = Image('resources/image/training/make_debut.jpg')
        self._button = Image('resources/image/training/enter_race.jpg')

    @property
    def image(self):
        return self._image

    @property
    def button(self):
        return self._button


class FirstRaceDetail(Screen):

    def __init__(self):
        self._image = Image('resources/image/training/race_detail.jpg')
        self._button = Image('resources/image/training/enter_race.jpg')

    @property
    def image(self):
        return self._image

    @property
    def button(self):
        return self._button


class RaceResult(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/result_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class AfterRace(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/tap_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class Scoring(Screen):

    def __init__(self, next_button: Image):
        self._button = next_button

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class Next(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/next_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class TrainingCompletion(Screen):

    def __init__(self, complete_button: Image):
        self._button = complete_button

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class CompletionConfirmation(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/complete_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class TrainingClosing(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/close_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class SecondNameSelection(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/decide_strong_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class BackToHome(Screen):

    def __init__(self):
        self._button = Image('resources/image/training/home_button.jpg')

    @property
    def image(self):
        return self._button

    @property
    def button(self):
        return self._button


class AoharuTutorial(Screen):

    def __init__(self):
        self._image = Image('resources/image/training/aoharu_tutorial.jpg')
        self._button = Image('resources/image/training/skip_explanation_button.jpg')

    @property
    def image(self):
        return self._image

    @property
    def button(self):
        return self._button
