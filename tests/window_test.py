import sys
from PyQt5.QtCore import Qt, QPoint, QRect, QSize
from PyQt5.QtGui import QIcon, QPainter, QColor, QBrush, QPixmap, QCursor, QPainterPath
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame


class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.setObjectName("TitleBar")
        self.setMinimumHeight(40)
        self.setIcon("../assets/imgs/music.ico")
        self.setTitle(self.parent.windowTitle())

        self.buttonSize = QSize(40, 40)

        self.minimizeBtn = QPushButton(self)
        self.minimizeBtn.setObjectName("MinimizeButton")
        self.minimizeBtn.setIcon(QIcon("../assets/system/minimize_win.png"))
        self.minimizeBtn.setStyleSheet("QPushButton { border:none; }")
        self.minimizeBtn.setFixedSize(self.buttonSize)
        self.minimizeBtn.clicked.connect(self.parent.showMinimized)

        self.maximizeBtn = QPushButton(self)
        self.maximizeBtn.setObjectName("MaximizeButton")
        self.maximizeBtn.setIcon(QIcon("../assets/system/maximize_win.png"))
        self.maximizeBtn.setStyleSheet("QPushButton { border:none; }")
        self.maximizeBtn.setFixedSize(self.buttonSize)
        self.maximizeBtn.clicked.connect(self.maximize)

        self.closeBtn = QPushButton(self)
        self.closeBtn.setObjectName("CloseButton")
        self.closeBtn.setIcon(QIcon("../assets/system/close_win.png"))
        self.closeBtn.setStyleSheet("QPushButton { border:none; }")
        self.closeBtn.setFixedSize(self.buttonSize)
        self.closeBtn.clicked.connect(self.parent.close)

    def setIcon(self, icon="icon.png"):
        self.icon = QIcon(icon)
        self.update()

    def setTitle(self, title):
        self.title = title
        self.update()

    def maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
            self.maximizeBtn.setIcon(QIcon("maximize.png"))
        else:
            self.parent.showMaximized()
            self.maximizeBtn.setIcon(QIcon("restore.png"))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.parent.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.parent.move(event.globalPos() - self.dragPos)
            event.accept()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制标题栏
        painter.fillRect(self.rect(), QColor(255, 255, 255, 50))
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(0, 0, 0, 0))
        painter.drawRect(self.rect())

        # 绘制标题栏图标和标题
        if hasattr(self, "icon"):
            iconSize = QSize(20, 20)
            iconRect = QRect(10, 10, iconSize.width(), iconSize.height())
            self.icon.paint(painter, iconRect, Qt.AlignVCenter | Qt.AlignLeft)

        if hasattr(self, "title"):
            font = painter.font()
            font.setBold(True)
            painter.setFont(font)
            textRect = QRect(40, 0, self.width() - 40, self.height())
            painter.drawText(textRect, Qt.AlignVCenter, self.title)

    def resizeEvent(self, event):
        self.closeBtn.move(self.width() - self.buttonSize.width(), 0)
        self.maximizeBtn.move(self.width()         - self.buttonSize.width() * 2, 0)
        self.minimizeBtn.move(self.width() - self.buttonSize.width() * 3, 0)

    def sizeHint(self):
        return QSize(self.parent.width(), self.minimumHeight())


class CustomWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("桌面宠物")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(640, 480)

        self.titleBar = CustomTitleBar(self)
        self.content = QFrame(self)
        self.content.setObjectName("Content")
        self.content.setStyleSheet("background-color: #F0F0F0;")

        self.initUI()

    def initUI(self):

        self.titleBar.setGeometry(0, 0, self.width(), self.titleBar.minimumHeight())
        self.content.setGeometry(0, self.titleBar.height(), self.width(), self.height() - self.titleBar.height())

    def resizeEvent(self, event):
        self.titleBar.setGeometry(0, 0, self.width(), self.titleBar.minimumHeight())
        self.content.setGeometry(0, self.titleBar.height(), self.width(), self.height() - self.titleBar.height())

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)


        # 绘制窗口边框
        brush = QBrush(QColor(255, 255, 255, 50))
        painter.setBrush(brush)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)

        # # 绘制窗口阴影
        # shadow = QGraphicsDropShadowEffect(self)
        # shadow.setBlurRadius(20)
        # shadow.setColor(QColor(0, 0, 0, 150))
        # self.setGraphicsEffect(shadow)

        # # 绘制窗口阴影
        # color = QColor(0, 0, 0, 50)
        # for i in range(1, 5):
        #     path = QPainterPath()
        #     path.setFillRule(Qt.WindingFill)
        #     path.addRoundedRect(self.rect(), 10, 10)
        #     color.setAlpha(50 - i * 10)
        #     painter.setPen(color)
        #     painter.drawPath(path)

        # 绘制窗口背景
        painter.fillRect(self.rect(), QColor(255, 255, 255))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPos)
            event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        # CustomWindow {
        #     border: 0px solid black;
        #     border-radius: 20px;
        #     background-color: white;
        #     box-shadow: 5px 5px 5px gray;
        # }
        #TitleBar {
            background-color: #F0F0F0;
            color: #333333;
        }
        #MinimizeButton:hover, #MaximizeButton:hover, #CloseButton:hover {
            background-color: #E0E0E0;
        }
        #MinimizeButton:pressed, #MaximizeButton:pressed, #CloseButton:pressed {
            background-color: #CCCCCC;
        }
    ''')

    window = CustomWindow()
    window.show()
    sys.exit(app.exec_())

