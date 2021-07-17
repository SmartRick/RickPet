#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年7月18日
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: 嵌入桌面
@description: 
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
import win32gui

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019'

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from win32con import SMTO_NORMAL
from win32con import SW_HIDE


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.showFullScreen()
        # self.showMaximized()
        geometry = QApplication.desktop().geometry()
        print(geometry)
        layout = QHBoxLayout(self)
        layout.setGeometry(geometry)
        q_pixmap = QPixmap("images/wallhaven-6od3px.jpg")
        q_pixmap = q_pixmap.scaled(geometry.width(), geometry.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        q_label = QLabel(self)
        # q_label.resize(geometry.width(), geometry.height())
        q_label.setPixmap(q_pixmap)
        layout.addWidget(q_label)
        self.bottom()
        self.show()
        # QPushButton('看什么看', self)

    def bottom(self):
        def enumWindows(hwnd, _):
            h1 = win32gui.FindWindow('Progman', 'Program Manager')
            # 向Progman发送特殊消息
            # print('h1:{}'.format(hex(h1)))
            win32gui.SendMessageTimeout(h1, 0x052c, 0, 0, SMTO_NORMAL, 0x3e8)

            h2 = win32gui.FindWindowEx(hwnd, 0, 'SHELLDLL_DefView', None)
            # print('h2:{}'.format(hex(h2)))
            if h2:
                # SysListView32即为桌面图标的窗口
                # h2 = win32gui.FindWindowEx(
                #     h1, None, 'SysListView32', 'FolderView')
                h3 = win32gui.FindWindowEx(
                    0, hwnd, 'WorkerW', None)
                # print('h3:{}'.format(hex(h3)))
                win32gui.ShowWindow(h3, SW_HIDE)
                win32gui.SetParent(int(self.winId()), h1)
                return True

        win32gui.EnumWindows(enumWindows, None)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
