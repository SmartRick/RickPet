import math
import sys

import requests
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os


class Absorbable(QWidget):
    def mouseMoveEvent(self, event):
        super(Draggable, self).mouseMoveEvent(event)


# 左键点击拖动改变位置
class Draggable(QWidget):
    is_dragg = False

    def mousePressEvent(self, event):
        super(Draggable, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.is_dragg = True
            self.downX = event.x()
            self.downY = event.y()
            print("鼠标按下x:%d,y:%d" % (self.downX, self.downY))
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseReleaseEvent(self, event):
        super(Draggable, self).mouseReleaseEvent(event)
        self.is_dragg = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        print("鼠标松开")

    def mouseMoveEvent(self, event):
        super(Draggable, self).mouseMoveEvent(event)
        # 返回鼠标相对于窗口的坐标
        # print(event.x())
        # print(event.y())
        # print(self.geometry())
        # 返回相对于控件的当前鼠标位置.PyQt5.QtCore.QPoint(260, 173)
        # print(event.pos())
        # 获取鼠标当前位置，屏幕的
        if self.is_dragg:
            pos = QCursor().pos()
            print(pos)
            self.move(pos.x() - (self.rect().width() - (self.rect().width() - self.downX)),
                      pos.y() - (self.rect().height() - (self.rect().height() - self.downY)))


# 右键左右拖动调节大小
class RightButtonChangeSize(QWidget):
    size_change = False
    minimum = 30

    def mousePressEvent(self, event):
        super(RightButtonChangeSize, self).mousePressEvent(event)
        if event.button() == Qt.RightButton:
            self.pos = QCursor().pos()
            self.current_size = self.geometry()
            # print(min(self.current_size.size().width(),self.current_size.size().height()))
            self.size_change = True

    def mouseReleaseEvent(self, event):
        super(RightButtonChangeSize, self).mouseReleaseEvent(event)
        self.size_change = False

    def mouseMoveEvent(self, event):
        super(RightButtonChangeSize, self).mouseMoveEvent(event)
        if self.size_change:
            change_value_temp = -(self.pos.x() - QCursor().pos().x())
            change = min(self.current_size.size().width(), self.current_size.size().height()) - change_value_temp
            print(change)
            if change <= self.minimum:
                return
            else:
                change_value = change_value_temp
            # print(change_value)
            self.resize(self.current_size.width() - change_value, self.current_size.height() - change_value)
            self.move(self.current_size.x() + change_value // 2, self.current_size.y() + change_value // 2)
            self.update()


# 阴影支持
class Shadow(QWidget):
    def __init__(self, blur_radius):
        super(Shadow, self).__init__()
        self.blur_radius = blur_radius
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(blur_radius)
        # self.shadow.setColor(QColor(0, 0, 0, 300))
        self.shadow.setColor(Qt.gray)
        # self.shadow.setOffset(6, 6)
        self.shadow.setOffset(0, 0)
        self.setGraphicsEffect(self.shadow)


class ImgModule(Draggable, Shadow, RightButtonChangeSize):
    is_dragg = False
    _angle = 0
    size_change = False

    def __init__(self, img_path, size, blur_radius):
        self.blur_radius = blur_radius
        super(ImgModule, self).__init__(blur_radius=self.blur_radius)
        self.minimum = self.blur_radius + 40
        self.img_path = img_path
        self.size = size
        self.screenImg = None
        self.init_ui()
        # 计时器
        # q_timer = QTimer(self)
        # q_timer.timeout.connect(self.ref)
        # q_timer.start(10)
        # q_timer.

    def init_ui(self):
        if not isinstance(self.size, QSize):
            raise Exception("size不是Qsize类型")
        self.resize(self.size)
        # self.setMouseTracking(True)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.set_img()
        # self.update()
        self.show()

    def enterEvent(self, event):
        animation = QPropertyAnimation(self, b"angle")
        # 绑定目标对象
        animation.setTargetObject(self)
        # 设置属性动画开始值
        animation.setStartValue(0)
        # 设置属性动画结束值
        animation.setEndValue(180)
        # 设置动画过度曲线
        animation.setEasingCurve(QEasingCurve.InQuad)
        # 设置循环次数，-1一直循环
        animation.setLoopCount(-1)
        # 设置动画持续时间
        animation.setDuration(1000)  # 在5秒的时间内完成
        # 开始动画
        animation.start()
        print("进入")

    def leaveEvent(self, event):
        print("离开")

    def paintEvent(self, event):
        painter = QPainter()
        # 抗锯齿
        painter.setRenderHint(QPainter.Antialiasing, True)
        # 设置平滑变换
        painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
        painter.begin(self)
        self.paintCircle(painter)
        painter.end()

    def paintCircle(self, painter):
        pen = QPen()
        pen.setColor(QColor(255, 255, 255))
        penWidth = 2
        pen.setWidth(penWidth)
        # img = requests.get(self.img_path)
        # pixmap = QPixmap.loadFromData(img.content)
        if self.screenImg != None:
            pixmap = self.screenImg
        else:
            pixmap = QPixmap(self.img_path)
        scaled = pixmap.scaled(self.geometry().size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        bruch = QBrush(scaled)
        painter.setBrush(bruch)
        # pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        rect = QRect(penWidth // 2 + self.blur_radius // 2, penWidth // 2 + self.blur_radius // 2,
                     self.rect().width() - penWidth - self.blur_radius,
                     self.rect().height() - penWidth - self.blur_radius)
        painter.rotate(self._angle)
        painter.drawRoundedRect(rect, rect.width() // 2, rect.height() // 2)

    def mousePressEvent(self, event):
        super(ImgModule, self).mousePressEvent(event)

    def ref(self):
        # 截取屏幕
        screen = QApplication.primaryScreen()
        self.screenImg = screen.grabWindow(QApplication.desktop().winId())

        self.update()

    @pyqtProperty(int)
    def angle(self):
        return self._angle

    @angle.setter
    def angle(self, value):
        self._angle = value
        self.update()



if __name__ == '__main__':
    q_size = QSize(150, 150)
    app = QApplication(sys.argv)
    # http://api.btstu.cn/sjtx/api.php?lx=c3&format=images
    module = ImgModule("images/bz.jpg", q_size, blur_radius=20)
    sys.exit(app.exec_())
