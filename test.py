#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @作者:黎九桐槐
# @时间:2020-08-02
# @代码功能:todo
# @代码重点:todo
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

' module description '

__author__ = 'SmartRick'


class COP(QWidget):
    def __init__(self):
        super(COP, self).__init__()
        self.show()

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        rc = QRect()
        p.setRenderHint(Qt.Antialiasing)
        barWidget = 20
        # circleX = rc.width() / 2;
        # circleY = rc.height() / 2;
        m_persent = 20
        m_rotateAngle = 360 * m_persent / 100
        allAngle = 360 * 100 / 100

        side = min(rc.width(), rc.height())
        outRect = QRectF(0, 0, side, side)
        inRect = QRectF(barWidget, barWidget, side - 40, side - 40)
        valueStr = '{}'.format(m_persent)
         # 画外圆
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(97, 117, 118)))
        p.drawEllipse(outRect)
        p.setBrush(QBrush(QColor(255, 107, 107)))
        p.drawPie(outRect, (90 - m_rotateAngle) * 16, m_rotateAngle * 16)
        # 绘制圆弧背景
        pen = QPen()
        pen.setCapStyle(Qt.RoundCap)
        pen.setWidthF(20)
        pen.setColor(QColor(97, 117, 118))
        p.setPen(pen)
        p.drawArc(inRect, 360 * 16, 360 * 16)
        # 绘制圆弧进度
        pen.setColor(QColor(255, 107, 107))
        p.setPen(pen)
        p.drawArc(inRect, 0 * 16, m_rotateAngle * 16)
        # 画文字
        f = QFont("Microsoft YaHei", 15, QFont.Bold)
        p.setFont(f)
        p.setFont(f)
        p.setPen(QColor("#555555"))
        p.drawText(inRect, Qt.AlignCenter, valueStr)
        p.end()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    cop = COP()
    sys.exit(app.exec_())
