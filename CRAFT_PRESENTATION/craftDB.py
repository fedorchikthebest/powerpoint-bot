import os
import shutil


def creat_DIR_site():
    if not os.path.isdir("powerpoint-bot/save_present"):
        os.mkdir("powerpoint-bot/save_present")


def delit_DIR_site():
    if os.path.isdir("powerpoint-bot/save_present"):
        shutil.rmtree("powerpoint-bot/save_present")


creat_DIR_site()