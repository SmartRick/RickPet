#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @作者:黎九桐槐
# @时间:2020-08-02
import sys
from PyQt5.QtWidgets import QApplication
from modules.components.base_pet import PetWidget

' module description '

__author__ = 'SmartRick'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")
    pet_widget = PetWidget(init_pet_img="assets/imgs/new_year_rabbit.png")
    sys.exit(app.exec_())
