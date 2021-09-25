# -*- coding: utf-8 -*-
from typing import List, Optional

import android_auto_play_opencv as am

from image.image import Image
from screen.screen import Screen

adbpath = ''
aapo = am.AapoManager(adbpath)
# aapo.mtl.threshold = 0.86
umamusume_path = 'jp.co.cygames.umamusume/jp.co.cygames.umamusume_activity.UmamusumeActivity'
MAX_COUNT = 20


class Util:

    @staticmethod
    def start_app():
        aapo.start(umamusume_path)
        aapo.sleep(5)
        print('app has started')

    @staticmethod
    def touch_image(image: Image):
        touched = False
        count = 0
        while not touched:
            aapo.screencap()
            if aapo.touchImg(image.str_path):
                touched = True
                aapo.sleep(0.5)
            else:
                print(f'image not found: {image.path}, score: {aapo.mtl.maxVal}')
                count += 1
                if count == MAX_COUNT:
                    print('touch_image: reached MAX_COUNT')
                    return
                aapo.sleep(1)

    @staticmethod
    def get_current_screen(screens: List[Screen]) -> Screen:
        count = 0
        score = 0
        threshold = aapo.mtl.threshold
        most_likely_screen: Optional[Screen] = None
        while count < MAX_COUNT:
            aapo.screencap()
            for screen in screens:
                aapo.chkImg(screen.image.str_path)
                if score < aapo.mtl.maxVal:
                    score = aapo.mtl.maxVal
                    most_likely_screen = screen
            print(f'most likely: {most_likely_screen.__class__.__name__}, score: {score}')
            if threshold < score:
                print(f'Got: {most_likely_screen.__class__.__name__}, score: {score}')
                return most_likely_screen
            count += 1
            aapo.sleep(0.5)
        print('get_current_screen: reached MAX_COUNT')
        exit(1)
