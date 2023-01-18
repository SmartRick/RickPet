from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from entity import PetMeta


# 基本宠物组件
class PetWidget(QWidget):
    def __init__(self, pet_meta: PetMeta):
        super().__init__()
        self.pet_meta = pet_meta
        self.init_pet_img = pet_meta.source_path
        self.setWindowTitle(pet_meta.name)
        q_icon = QIcon(pet_meta.source_path)
        self.setWindowIcon(q_icon)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        pet_img = QPixmap(self.init_pet_img)
        _pet_img_size = pet_img.scaledToWidth(100).size()

        self.min_size = _pet_img_size / 2
        self.max_size = _pet_img_size * 3
        self.label = QLabel(self)
        self.label.setPixmap(pet_img)
        self.label.setScaledContents(True)
        self.label.resize(_pet_img_size)
        self.resize(_pet_img_size)

        # 初始化样式和功能
        # self._init_style()
        self._init_animation()
        # self._init_menu_bar()
        self._init_tray()
        self.show()

    def _init_animation(self):
        # 初始化缩放动画
        self.animation = QPropertyAnimation(self.label, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

    # def _init_style(self):
    # self.setStyleSheet("""
    #             QLabel {
    #                 border-radius: 15px;
    #                 background-color: rgba(255, 255, 255, 0.5);
    #                 border: 2px solid gray;
    #                 border-image: url(pet.png);
    #                 border-style: solid;
    #                 box-shadow: 0px 0px 10px #00bfff;
    #             }
    #             """)

    def _init_tray(self):
        self.tray_icon = QSystemTrayIcon(QIcon(self.init_pet_img), self)
        self.tray_icon.show()
        self.tray_icon.activated.connect(self.tray_icon_activated)
        self.hide_action = QAction("Hide", self)
        self.hide_action.triggered.connect(self.hide)
        self.show_action = QAction("Show", self)
        self.show_action.triggered.connect(self.show)
        self.tray_menu = QMenu()
        self.tray_menu.addAction(self.hide_action)
        self.tray_menu.addAction(self.show_action)
        self.tray_icon.setContextMenu(self.tray_menu)

    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        # context_menu.setSeparatorsCollapsible(True)
        # context_menu.setAutoFillBackground(False)
        # context_menu.setAttribute(Qt.WA_TranslucentBackground)
        change_img_action = context_menu.addAction("切换图片")
        open_main_action = context_menu.addAction("打开主界面")

        # context_menu.setStyleSheet("""
        #             QMenu {
        #                 background-color: rgba(255, 255, 255, 0);
        #                 border: 1px solid gray;
        #                 font-size: 14px;
        #                 border-radius: 10px;
        #             }
        #             QMenu::item {
        #                 padding: 5px 30px 5px 30px;
        #             }
        #             QMenu::item:selected {
        #                 background-color: lightgray;
        #             }
        #         """)
        change_img_action.triggered.connect(self.change_img)
        open_main_action.triggered.connect(self.change_img)
        context_menu.exec_(event.globalPos())

    def change_img(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if file_name:
            self.label.setPixmap(QPixmap(file_name))

    def enterEvent(self, event):
        print("进入")

    def leaveEvent(self, event):
        print("离开")

    # 鼠标点击事件
    def mousePressEvent(self, event):
        self.offset = event.pos()

    # 鼠标移动事件
    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    # 鼠标滚动事件
    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            new_size = self.label.size() + QSize(10, 10)
        else:
            new_size = self.label.size() - QSize(10, 10)

        if self.min_size.width() <= new_size.width() <= self.max_size.width() and self.min_size.height() <= new_size.height() <= self.max_size.height():
            self.label.resize(new_size)
            self.resize(new_size)
