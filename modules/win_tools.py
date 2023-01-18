import winreg
from win10toast import ToastNotifier
from win32com.client import Dispatch
import win32api, win32gui, win32con


# 获取并打印历史WIFI密码
def get_wifi_passwords():
    # 打开HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles')

    # 遍历所有的子键
    i = 0
    while True:
        try:
            sub_key_name = winreg.EnumKey(key, i)
            sub_key = winreg.OpenKey(key, sub_key_name)
            # 读取密码
            try:
                password = winreg.QueryValueEx(sub_key, 'KeyMaterial')[0]
                # 打印密码
                print(sub_key_name, password)
            except:
                pass
            i += 1
        except WindowsError as e:
            break


# 自定义图标文件必须是ico格式
def toast(title: str = "提示", msg: str = "消息", duration: int = 5, icon_path: str = None):
    toaster = ToastNotifier()
    toaster.show_toast(title, msg, duration=duration, icon_path=icon_path)
    # toaster.wait_until_closed()


# 获取快捷方式的真实路径
def get_lnk_path(path):
    shell = Dispatch("WScript.Shell")
    return shell.CreateShortCut(path).Targetpath


# 更换windows桌面壁纸
def setWallPaper(pic: str):
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

# if __name__ == '__main__':
#     get_wifi_passwords()
