#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # import winreg
# # import cv2
# # import imageio as io
# # import numpy as np
# # import ffmpeg
# # def record_gif(fps: int, filename: str):
# #     (
# #         ffmpeg
# #             .input('desktop', f='gdigrab', offset_x=0, offset_y=0, video_size='1920x1080', framerate=str(fps) + '/1')
# #             .output(filename, f='gif', pix_fmt='rgb24', loop=0)
# #             .run(capture_stdout=True, capture_stderr=True)
# #     )
# #     print("GIF录制完成，保存在：" + filename)
# # def record_video(fps: int, filename: str):
# #     (
# #         # 在这里我选择了mp4格式来保存视频，你也可以根据需要选择其他格式，如：avi, flv, wmv等。
# #         ffmpeg
# #             .input('desktop', f='gdigrab', offset_x=0, offset_y=0, video_size='1920x1080', framerate=str(fps) + '/1')
# #             .output(filename, f='mp4', pix_fmt='yuv420p')
# #             .overwrite_output()
# #             .run(capture_stdout=True, capture_stderr=True)
# #     )
# #     print("视频录制完成，保存在：" + filename)
# import sys
# from PyQt5.QtCore import Qt, QUrl
# from PyQt5.QtGui import QCursor
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtWebEngineWidgets import QWebEngineView
#
#
# class MyWebView(QWebEngineView):
#     def __init__(self):
#         super().__init__()
#
#         # 隐藏边框
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#
#         # 允许点击网页
#         self.setAttribute(Qt.WA_AcceptTouchEvents)
#
#         self.setUrl(QUrl("https://www.example.com"))
#
#     def mousePressEvent(self, event):
#         # self.__mouse_press_pos = None
#         # self.__mouse_move_pos = None
#         # if event.button() == Qt.LeftButton:
#         #     self.__mouse_press_pos = event.global
#
# # if __name__ == '__main__':
# #     print()
# # 每30分钟提醒一次
# # interval = 2
# # while True:
# #     休息
# # time.sleep(interval)
# # 显示气泡提醒
# # ctypes.windll.user32.MessageBoxW(0, "该休息了!", "休息提醒", 0x40 | 0x1)
#
# # record_gif(filename="D:\\workfile\\temp\\screen.gif", fps=25)
# 小球运动
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class Ball:
#     def __init__(self, x, y, width):
#         self.m_pos = QPoint(x, y)
#         self.m_vel = QPoint(0, 0)
#         self.m_gravity = 8
#         self.m_elasticity = 0.75
#         self.m_radius = 10
#         self.m_bounds = QRect(0, 0, width, width)
#
#     def draw(self, painter):
#         # 绘制小球
#         painter.setBrush(QBrush(Qt.red))
#         painter.drawEllipse(self.m_pos, self.m_radius, self.m_radius)
#
#     def update(self):
#         # 更新小球的位置
#         self.m_pos += self.m_vel
#         self.m_vel.setY(self.m_vel.y() + self.m_gravity)
#
#         # 碰撞检测和反弹
#         if self.m_pos.y() + self.m_radius > self.m_bounds.bottom():
#             # 计算碰撞后的速度和加速度
#             vel = self.m_vel.y() * self.m_elasticity
#             acc = self.m_gravity
#
#             # 计算反弹后的速度和加速度
#             new_vel = -vel
#             new_acc = acc
#
#             # 计算反弹后的位置
#             delta_t = (self.m_pos.y() + self.m_radius - self.m_bounds.bottom()) / vel
#             delta_s = vel * delta_t + 0.5 * acc * delta_t ** 2
#             new_pos = QPoint(self.m_pos.x(), self.m_bounds.bottom() - self.m_radius - delta_s)
#
#             # 更新小球的状态
#             self.m_pos = new_pos
#             self.m_vel.setY(new_vel)
#             self.m_gravity = new_acc
#
#     def set_pos(self, pos):
#         self.m_pos = pos
#
#
# class MyWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setFixedSize(400, 400)
#         self.m_ball = Ball(self.width() // 2, 0, self.width())
#         self.m_timer = QTimer(self)
#         self.m_timer.timeout.connect(self.animate)
#         self.m_timer.start(1000/60)  # 设置刷新率为60帧/秒
#
#         # 添加一个成员变量，用于缓存所有的绘制操作
#         self.m_bufferPixmap = QPixmap(self.width(), self.height())
#
#     def paintEvent(self, event):
#         # 缓存所有的绘制操作
#         painter = QPainter(self.m_bufferPixmap)
#         painter.fillRect(self.rect(), Qt.white)
#         self.m_ball.draw(painter)
#         painter.end()
#
#         # 绘制缓存的绘制操作
#         painter = QPainter(self)
#         painter.drawPixmap(self.rect(), self.m_bufferPixmap)
#
#     def animate(self):
#         # 更新小球的状态
#         self.m_ball.update()
#
#         # 重新绘制
#         self.update()
#
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     w = MyWidget()
#     w.show()
#     w.m_timer.start()  # 开始定时器
#     sys.exit(app.exec_())

# 第一版
# from PyQt5.QtCore import QRect, QPoint, QBasicTimer
# from PyQt5.QtGui import QPainter, QColor, QBrush
# from PyQt5.QtWidgets import QWidget, QApplication
# import sys
#
# class Ball:
#     def __init__(self, x, y, width):
#         self.m_pos = QPoint(x, y)
#         self.m_vel = QPoint(0, 0)
#         self.m_gravity = 1  # 调整重力加速度
#         self.m_elasticity = 0.75  # 调整弹性系数
#         self.m_friction = 0.02  # 增加摩擦力
#         self.m_radius = 10
#         self.m_bounds = QRect(0, 0, width, width)
#         self.stopped = False
#
#     def update(self):
#         self.m_vel.setY(self.m_vel.y() + self.m_gravity)
#         self.m_pos += self.m_vel
#         if self.m_pos.y() + self.m_radius >= self.m_bounds.bottom():
#             self.m_pos.setY(self.m_bounds.bottom() - self.m_radius)
#             self.m_vel.setY(-self.m_vel.y() * self.m_elasticity)
#             self.m_vel.setX(self.m_vel.x() * (1 - self.m_friction))  # 添加摩擦力计算
#             if abs(self.m_vel.y()) < 1 and abs(self.m_vel.x()) < 1:  # 判断小球是否停止
#                 self.stopped = True
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.ball = Ball(100, 100, 400)
#         self.timer = QBasicTimer()
#         self.timer.start(16, self)
#         self.setGeometry(300, 300, 500, 500)
#         self.setWindowTitle('Bouncing Ball')
#         self.show()
#
#     def paintEvent(self, event):
#         qp = QPainter()
#         qp.begin(self)
#         self.drawBall(qp)
#         qp.end()
#
#     def drawBall(self, qp):
#         qp.setBrush(QBrush(QColor(255, 0, 0)))
#         qp.drawEllipse(self.ball.m_pos, self.ball.m_radius, self.ball.m_radius)
#
#     def timerEvent(self, event):
#         if event.timerId() == self.timer.timerId() and not self.ball.stopped:
#             self.ball.update()
#             self.update()
#         elif self.ball.stopped:
#             self.timer.stop()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtCore import QCoreApplication
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import QFont
#
#
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # 提示框鼠标放上去提示
#         QToolTip.setFont(QFont('SansSerif', 10))
#         self.setToolTip('This is a <b>QWidget</b> widget')
#
#         btn = QPushButton('Button', self)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.resize(btn.sizeHint())
#         # 将点击事件连接到回调函数上
#         btn.clicked.connect(QCoreApplication.instance().quit)
#         # 获取当前运行示例的应用对象
#         # QCoreApplication.instance().quit
#         btn.move(50, 50)
#
#         # self.setGeometry(300, 300, 300, 200)
#         self.resize(250, 150)
#         self.center()
#         self.setWindowTitle('Tooltips')
#         self.statusBar().showMessage('Ready')
#
#         self.show()
#
#     def center(self):
#
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
#     # 重写窗口关闭事件方法
#     def closeEvent(self, event):
#
#         reply = QMessageBox.question(self, 'Message',
#                                      "Are you sure to quit?", QMessageBox.Yes |
#                                      QMessageBox.No, QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())


# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""


Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""
from PyQt5.QtCore import Qt
from QcureUi import cure
import sys
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(lcd)
        vbox2.addWidget(sld)

        sld.valueChanged.connect(lcd.display)

        vbox.addLayout(vbox2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    cure.Windows(ex, 'tray name', True, 'blueGreen', 'program name', 'myicon.ico')
    sys.exit(app.exec_())
