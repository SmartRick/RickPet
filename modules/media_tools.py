import time
import imageio
from PIL import ImageGrab


def record_gif(duration: int, filename: str, fps: int = 20):
    frames = []
    start_time = time.time()
    interval = 1 / fps
    while time.time() - start_time <= duration:
        img = ImageGrab.grab()
        frames.append(img)
        time.sleep(interval)
    imageio.mimsave(filename, frames, 'GIF', duration=interval)
    print("GIF录制完成，保存在：" + filename)


# 截图
def screenshot():
    return ImageGrab.grab()
