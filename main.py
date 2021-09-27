# -*- coding: utf-8 -*-
from image.images import Images
from training.training import Training
from training.training_mode import TrainingMode
from umamusume.umamusume import Umamusume
from util import Util


class Main:

    def __init__(self):
        self.training_mode = TrainingMode.AOHARU
        self.target_umamusume = self.get_target_umamusume('mejiro_mcqueen')
        self.images = Images()
        self.training = Training(self.target_umamusume)

    @staticmethod
    def get_target_umamusume(name: str):
        try:
            target = Umamusume(name)
        except AssertionError:
            print(f'No such Umamusume: {name}')
            exit(1)
        else:
            return target

    def execute(self):
        Util.start_app()
        self.tap_training_button()
        self.select_training()
        self.select_umamusume()
        self.select_random_parents()
        self.select_support()
        self.start_training()
        self.training.start()

    def tap_training_button(self):
        Util.touch_image(self.images.home.training_button)

    def select_training(self):
        Util.touch_image(self.images.select.next_button)

    def select_umamusume(self):
        Util.touch_image(self.target_umamusume.thumbnail)
        Util.touch_image(self.images.select.next_button)

    def select_random_parents(self):
        Util.touch_image(self.images.select.parents_random_select)
        Util.touch_image(self.images.select.ok_button)
        Util.touch_image(self.images.select.next_button)

    def select_support(self):
        Util.touch_image(self.images.select.support_random_select)
        Util.touch_image(self.images.select.ok_button)

    def start_training(self):
        Util.touch_image(self.images.select.start_training)
        Util.touch_image(self.images.select.confirm_starting_training)


if __name__ == '__main__':
    main = Main()
    main.execute()
