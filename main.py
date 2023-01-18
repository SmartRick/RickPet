#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @作者:黎九桐槐
# @时间:2020-08-02
import sys
from PyQt5.QtWidgets import QApplication

from consts.enums import PetType
from entity.core import PetMeta
from modules.components.base_pet import PetWidget

' module description '

__author__ = 'SmartRick'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")
    meta = PetMeta()
    meta.pet_type = PetType.STATIC
    meta.name = "新年小兔子"
    meta.source_path = "assets/pet_img/new_year_rabbit.png"
    pet_widget = PetWidget(meta)
    sys.exit(app.exec_())
