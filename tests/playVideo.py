from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
import pyglet
from pyglet.media import *
import os
import math
import sys
import numpy as np
import cv2

player = None
def testOne():
    global player
    app = QApplication(sys.argv)
    # playlist = QMediaPlaylist()
    # playlist.addMedia(QMediaContent(QUrl('../video/序列.mp4')))
    # playlist.addMedia(QMediaContent(QUrl('../video/序列.mp4')))
    # playlist.setCurrentIndex(1)
    # playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
    player = QMediaPlayer()
    player.stateChanged.connect(statusChange)

    vw = QVideoWidget()  # 定义视频显示的widget
    vw.show()
    player.setVideoOutput(vw)  # 视频播放输出的widget，就是上面定义的
    # url_ = QFileDialog.getOpenFileUrl()[0]
    # QFileDialog.getOpenFileUrl()[0]
    player.setMedia(QMediaContent(QUrl('../video/序列.mp4')))  # 选取视频文件
    # player.setPlaylist(playlist)
    player.play()  # 播放视频
    sys.exit(app.exec_())

def statusChange(state):
    print("状态改变",state)
    if state == QMediaPlayer.StoppedState:
        player.setPosition(0)
        player.play()  # 播放视频
        
def testTwo():
    window = pyglet.window.Window()
    player = Player()
    source = load('images/dddd.mp4')
    player.queue(source)
    player.play()
    print(player.get_texture())

    @window.event
    def on_draw():
        window.clear()
        player.get_texture().blit(20, 100)

    pyglet.app.run()


def testThree():
    import pyglet

    vid_path = '../video/烟.mp4'
    window = pyglet.window.Window(caption="视频插件", resizable=True)

    window.set_size(1920, 1080)
    # window.set_fullscreen()
    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vid_path)

    player.queue(MediaLoad)
    player.play()

    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(0, 0)

    pyglet.app.run()


def testFour():
    vid_path = '../video/囍.mp4'
    cap = cv2.VideoCapture(vid_path)

    while (cap.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(40) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def testFive():
    vid_path = '../video/囍.mp4'
    capture = cv2.VideoCapture(vid_path)
    if capture.isOpened():
        ret, frame = capture.read()
        print("读取视频文件是成功")
    else:
        ret = False
        print("读取视频文件失败")

    count = 0
    while ret:
        ret, frame = capture.read()
        img_path = f'../imgs/vid/{count}.jpg'
        cv2.imwrite(img_path, frame)
        count = count + 1
        # waitKey()--这个函数是在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环)
        # 这里设置10，表示每次抽帧等待10ms
        cv2.waitKey(10)
        if count == 60: break
    capture.release()


class VideoPlay(QVideoWidget):
    def __init__(self, video_path):
        super(VideoPlay, self).__init__()
        self.count = 0
        self.video_path = video_path
        self.initUI()
        # self.initCapture()
        # self.timer()
        # self.flushContent()
    def initCapture(self):
        vid_path = self.video_path
        self.capture = cv2.VideoCapture(vid_path)
        if self.capture.isOpened():
            self.ret, self.frame = self.capture.read()
            print("读取视频文件是成功")
        else:
            self.ret = False
            print("读取视频文件失败")

    def initUI(self):
        self.setWindowTitle("视频播放测试")
        self.resize(1920 // 2, 1080 // 2)
        player = QMediaPlayer(self)
        player.setVideoOutput(self)  # 视频播放输出的widget，就是上面定义的
        player.setMedia(QMediaContent(QUrl(self.video_path)))  # 选取视频文件
        player.play()  # 播放视频
        self.show()

    def timer(self):
        q_timer = QTimer(self)
        q_timer.timeout.connect(self.flushContent)
        q_timer.start(6)

    def flushContent(self):
        print("画面刷新")
        while self.ret:
            self.ret, self.frame = self.capture.read()
            height, width, depth = self.frame.shape
            cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            img = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
            # out_win = "output_style_full_screen"
            # cv2.namedWindow(out_win, cv2.WINDOW_NORMAL)
            # cv2.setWindowProperty(out_win, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            # cv2.imshow(out_win, self.frame)
            # k = cv2.waitKey(1)
            # height, width, depth = self.frame.shape
            # cvimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            # cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)
            #
            # # imgDown = cv2.pyrDown(self.frame)
            # # imgDown = np.float32(imgDown)
            # # cvRGBImg = cv2.cvtColor(imgDown, cv2.cv.CV_BGR2RGB)
            # # qimg = QImage(cvRGBImg.data, cvRGBImg.shape[1], cvRGBImg.shape[0], QImage.Format_RGB888)

            # q_pixmap = pixmap01.scaledToWidth(1920 // 2, Qt.SmoothTransformation)
            self.q_label.setPixmap(QPixmap.fromImage(img))
        self.capture.release()
        # self.count = self.count + 1



def testVideoQt():
    q_application = QApplication(sys.argv)
    play = VideoPlay('../video/序列.mp4')
    sys.exit(q_application.exec_())




def testcv2():
    img = cv2.imread('../imgs/wallhaven-28z3q9.jpg')
    if img.data != None:
        height, width, depth = img.shape
        print(height,width)
        # cvimg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

        cv2.namedWindow("Image")
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("图片为空")


if __name__ == '__main__':
    testOne()
    # testTwo()
    # testThree()
    # testFour()
    # testFive()
    # testVideoQt()
    # testcv2()
