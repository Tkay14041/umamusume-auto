# -*- coding: utf-8 -*-
import time

from training.skip import Skip
from training.training_screen import *
from umamusume.umamusume import Umamusume
from util import Util


class Training:

    def __init__(self, umamusume: Umamusume):
        self.umamusume = umamusume
        self.screens = [GoingOut(umamusume.training_home),
                        OptionSelection(),
                        FanNotEnough(),
                        BeforeRace(umamusume.race_button),
                        FirstRaceSelection(),
                        FirstRaceDetail(),
                        RaceResult(),
                        AfterRace(),
                        Scoring(umamusume.next_button),
                        Next(),
                        TrainingCompletion(umamusume.training_completion_button),
                        CompletionConfirmation(),
                        TrainingClosing(),
                        SecondNameSelection(),
                        BackToHome(),
                        AoharuTutorial()]

    def start(self):
        self.skip()
        while True:
            current_screen = Util.get_current_screen(self.screens)
            Util.touch_image(current_screen.button)
            if isinstance(current_screen, FirstRaceDetail):
                time.sleep(3)

    @staticmethod
    def skip():
        Skip.prolog()
        Skip.first()
        Skip.second()
        Skip.decide()
