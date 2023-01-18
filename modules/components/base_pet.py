from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# 基本宠物组件
class PetWidget(QWidget):
    def __init__(self, init_pet_img="../img/hamster_pet.png"):
        super().__init__()
        self.init_pet_img = init_pet_img

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.min_size = QSize(60, 60)
        self.max_size = QSize(200, 200)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap(self.init_pet_img))
        self.label.setScaledContents(True)
        self.label.resize(100, 200)
        self.resize(100, 200)

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

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            new_size = self.label.size() + QSize(10, 10)
        else:
            new_size = self.label.size() - QSize(10, 10)

        if self.min_size.width() <= new_size.width() <= self.max_size.width() and self.min_size.height() <= new_size.height() <= self.max_size.height():
            self.label.resize(new_size)
            self.resize(new_size)
