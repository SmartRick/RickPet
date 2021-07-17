import os

import win32api, win32gui, win32con
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

def openexe():
    # system = os.system("‪E:\\谷歌下载\\鲸猫试用小助手1.3.14.exe")
    # 执行程序
    # popen = os.popen(r"python D:\pythonProbject\PyQt5Demo\hello.py")
    pythonStr = r"python D:\pythonProbject\PyQt5Demo\hello.py"
    # 执行cmd命令
    # popen = os.popen("dir")

    popen = os.popen("dir")
    # print(system)
    print(popen.read())
    # win32api.ShellExecute(0, 'open', '‪E:\\谷歌下载\\鱼牙直播姬V1.24\\鱼牙直播姬V1.24.exe', '', '', 1)           # 前台打开

if __name__=='__main__':
    # pic='''D:\\pythonProbject\\PyQt5Demo\\images\\bz.jpg'''
    # setWallPaper(pic)
    openexe()