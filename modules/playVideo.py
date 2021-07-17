from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
import pyglet
from pyglet.media import *
import os
import math
import sys

def testOne():
    app = QApplication(sys.argv)
    player = QMediaPlayer()
    vw = QVideoWidget()  # 定义视频显示的widget
    vw.resize(600,600)
    player.setVideoOutput(vw)  # 视频播放输出的widget，就是上面定义的
    # url_ = QFileDialog.getOpenFileUrl()[0]
    q_url = QUrl('images/123.mp4')
    print(q_url)
    player.setMedia(QMediaContent(q_url))  # 选取视频文件
    player.play()  # 播放视频
    vw.show()
    sys.exit(app.exec_())

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

    vid_path = 'images/123.mp4'
    window = pyglet.window.Window(caption="视频插件", resizable=True,fullscreen=True)

    # window.set_size(220, 400)
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

if __name__ == '__main__':
    # testOne()
    # testTwo()
    testThree()