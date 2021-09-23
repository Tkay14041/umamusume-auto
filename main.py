# -*- coding: utf-8 -*-
import time

import android_auto_play_opencv as am

adbpath = ''
aapo = am.AapoManager(adbpath)
umamusume_path = 'jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity'


def main():
    training_mode = './screen_images/select/aoharu_mode.jpg'
    target_umamusume = './screen_images/uma/mejiro_mcqueen.jpg'
    start_app()
    tap_training_button()
    select_training(training_mode)
    select_umamusume(target_umamusume)
    select_random_parents()
    select_support()
    start_training()


def touch_image(image: str):
    touched = False
    while not touched:
        aapo.screencap()
        if aapo.touchImg(image):
            touched = True
            aapo.sleep(1)
        else:
            print(f'image not found: {image}')
        time.sleep(1)


def start_app():
    aapo.start(umamusume_path)
    # aapo.sleep(10)
    print('app has started.')


def tap_training_button():
    touch_image('./screen_images/home/training_button.jpg')


def is_target_training_mode(training_mode: str) -> bool:
    aapo.screencap()
    return aapo.chkImg2(training_mode)


def select_training(training_mode: str):
    if is_target_training_mode(training_mode):
        touch_image('./screen_images/select/next_button.jpg')


def select_umamusume(target_umamusume: str):
    touch_image(target_umamusume)
    touch_image('./screen_images/select/next_button.jpg')


def select_random_parents():
    touch_image('./screen_images/select/parents_random_select.jpg')
    touch_image('./screen_images/select/ok_button.jpg')
    touch_image('./screen_images/select/next_button.jpg')


def select_support():
    touch_image('./screen_images/select/support_random_select.jpg')
    touch_image('./screen_images/select/ok_button.jpg')


def start_training():
    touch_image('./screen_images/select/start_training.jpg')
    touch_image('./screen_images/select/confirm.jpg')


if __name__ == '__main__':
    main()
