# -*- coding: utf-8 -*-
import time

import android_auto_play_opencv as am

from image.image import Image
from image.images import Images
from training.training_mode import TrainingMode
from umamusume.mejiro_mcqueen import MejiroMcQueen

adbpath = ''
aapo = am.AapoManager(adbpath)
umamusume_path = 'jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity'


class Main:

    def __init__(self):
        self.training_mode = TrainingMode.AOHARU
        self.target_umamusume = MejiroMcQueen()
        self.images = Images()

    def execute(self):
        self.start_app()
        self.tap_training_button()
        self.select_training()
        self.select_umamusume()
        self.select_random_parents()
        self.select_support()
        self.start_training()

    @staticmethod
    def touch_image(image: Image):
        touched = False
        while not touched:
            aapo.screencap()
            if aapo.touchImg(image.str_path):
                touched = True
                aapo.sleep(1)
            else:
                print(f'image not found: {image.str_path}')
            time.sleep(1)

    @staticmethod
    def start_app():
        aapo.start(umamusume_path)
        # aapo.sleep(10)
        print('app has started.')

    def tap_training_button(self):
        self.touch_image(self.images.home.training_button)

    @staticmethod
    def is_target_training_mode(training_mode: TrainingMode) -> bool:
        aapo.screencap()
        return aapo.chkImg2(training_mode.image.str_path)

    def select_training(self):
        if self.is_target_training_mode(self.training_mode):
            self.touch_image(self.images.select.next_button)

    def select_umamusume(self):
        self.touch_image(self.target_umamusume.thumbnail)
        self.touch_image(self.images.select.next_button)

    def select_random_parents(self):
        self.touch_image(self.images.select.parents_random_select)
        self.touch_image(self.images.select.ok_button)
        self.touch_image(self.images.select.next_button)

    def select_support(self):
        self.touch_image(self.images.select.support_random_select)
        self.touch_image(self.images.select.ok_button)

    def start_training(self):
        self.touch_image(self.images.select.start_training)
        self.touch_image(self.images.select.confirm_starting_training)


if __name__ == '__main__':
    main = Main()
    main.execute()
