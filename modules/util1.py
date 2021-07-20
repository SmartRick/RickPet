import os

import win32api, win32gui, win32con
from win32com.client import Dispatch
import time


# 更换windows桌面壁纸
def setWallPaper(pic):
    # 打开指定注册表路径
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    # 设置壁纸风格，最后的参数是（2：拉伸，0居中，6适应，10填充，0平铺）
    win32api.RegSetValueEx(regKey, "WallpaperStyle", 0, win32con.REG_SZ, "2")
    # 最后的参数（1平铺，拉伸居中都是0）
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # 刷新桌面
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDWININICHANGE)


def openexe(path):
    # with open(path, 'r') as file:
    #     print(file.name)
    execute = win32api.ShellExecute(0, 'open', path, '', '', 1)  # 前台打开
    # win32api.ShellExecute(0, 'open', path, '', '', 1)  # 前台打开
    # win32api.ShellExecute(0, 'open', path, '1.txt', '', 1)  # 打开文件
    # win32api.ShellExecute(0, 'open', 'http://www.sohu.com', '', '', 1)  # 打开网页
    # win32api.ShellExecute(0, 'open', 'D:\\Opera.mp3', '', '', 1)  # 播放视频
    # win32api.ShellExecute(0, 'open', 'D:\\hello.py', '', '', 1)  # 运行程序
    # print(execute)
    # system = os.system(path)
    # print(system)
    # 执行程序
    # popen = os.popen(r"python D:\pythonProbject\PyQt5Demo\hello.py")
    # 执行cmd命令
    # popen = os.popen("dir")
    # print(popen.read())


shell = Dispatch("WScript.Shell")
# 获取快捷方式的真实路径
def getLnkPath(path):
    return shell.CreateShortCut(path).Targetpath

if __name__ == '__main__':
    # pic='''D:\\pythonProbject\\PyQt5Demo\\images\\bz.jpg'''
    # setWallPaper(pic)
    # openexe('E:\\softword\\CloudMusic\\cloudmusic.exe')
    # openexe('../鲸猫试用小助手.lnk')
    getLnkPath('../鲸猫试用小助手.lnk')
