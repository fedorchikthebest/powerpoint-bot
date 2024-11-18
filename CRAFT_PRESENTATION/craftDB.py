import os
import shutil


def creat_DIR_site():
    if not os.path.isdir("save_present"):
        os.mkdir("save_present")
        print('DIR CRAFT POWER')
    else:
        print('DIR was save')

def delit_DIR_site():
    if os.path.isdir("save_present"):
        shutil.rmtree("save_present")
        print("DIR delete DELETE")
    else:
        print("DIR not founde in Proj")

creat_DIR_site()
delit_DIR_site()