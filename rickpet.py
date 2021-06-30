from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os
import math
import sys


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

    def __init__(self,minimum=30):
        super(RightButtonChangeSize, self).__init__()
        self.minimum = minimum

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


# 宠物类
class RickPet():
    def __init__(self, path, x, y,  width=None,height=None,auto_scale=False):
        # 宠物ID
        self.id = QUuid.createUuid()
        # 宠物的图片
        self.clothes = []
        # 坐标
        self.x = x
        self.y = y

        if auto_scale != True:
            # 高度
            self.height = height
            # 宽度
            self.width = width

        # 图像刷新间隔毫秒数
        self.gap = 200
        # 当前刷新图像的下标
        self.index = 0

        # 初始化
        self.init_clothes(path)

    def init_clothes(self, path):
        if os.path.exists(path) and os.path.isdir(path):
            listdir = os.listdir(path)
            for file in listdir:
                file_path = os.path.join(path, file)
                self.clothes.append(QImage(file_path))
                print(file_path)
        else:
            raise Exception("路径不存在或不是文件夹")

    def get_rect(self):
        return QRect(self.x, self.y, self.width, self.width)



class PetGui(Draggable, RightButtonChangeSize):
    def __init__(self, pet):
        super(PetGui, self).__init__()
        self.pet = pet
        # 初始化UI
        self.init_gui()
        self.tray()
        # 初始化角色
        # self.init_rule()
        self.start_action()
        self.show()

    def init_gui(self):
        # 窗口无边框，透明，置顶
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setGeometry(self.pet.get_rect())

    def init_rule(self):
        q_label = QLabel(self)
        q_label.setPixmap(QPixmap.fromImage(self.pet.clothes[0]))

    def paintEvent(self, event):
        super(PetGui, self).paintEvent(event)
        q_painter = QPainter(self)
        #q_painter.begin(self)
        # 抗锯齿
        q_painter.setRenderHint(QPainter.Antialiasing, True)
        # 高质量抗锯齿
        q_painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
        # 设置平滑变换
        q_painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        #q_brush = QBrush()
        #q_painter.setBrush(q_brush)
        q_painter.drawPixmap(0,0,QPixmap.fromImage(self.pet.clothes[self.pet.index]))

        #q_painter.end()

    def start_action(self):
        q_timer = QTimer(self)
        q_timer.timeout.connect(self.action)
        q_timer.start(self.pet.gap)

    def action(self):
        #if self.index<len(self.clothes):
        self.pet.index = (self.pet.index+1)%len(self.pet.clothes)
        self.update()

    # 系统托盘
    def tray(self):
        tray = QSystemTrayIcon(self)

        tray.setIcon(QIcon('image/meizi/0.png'))

        display = QAction(QIcon('image/eye.png'), '显示', self, triggered=self.display)
        quit = QAction(QIcon('image/exit.png'), '退出', self, triggered=self.quit)
        menu = QMenu(self)
        menu.addAction(quit)
        menu.addAction(display)
        tray.setContextMenu(menu)
        tray.show()

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):

        self.right_menu.setVisible(False)

    def display(self):
        self.right_menu.setVisible(True)


class PetSystem():
    def __init__(self):
        self.start()

    def start(self):
        app = QApplication(sys.argv)
        pet = RickPet("D:\\pythonProbject\\PyQt5Demo\\image\\meizi", 300, 500, 130, 160)
        gui = PetGui(pet)
        app.exit(app.exec_())


if __name__ == '__main__':
    system = PetSystem()
    # system = PetSystem()
