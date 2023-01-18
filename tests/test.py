# import winreg
# import cv2
# import imageio as io
# import numpy as np
# import ffmpeg
# def record_gif(fps: int, filename: str):
#     (
#         ffmpeg
#             .input('desktop', f='gdigrab', offset_x=0, offset_y=0, video_size='1920x1080', framerate=str(fps) + '/1')
#             .output(filename, f='gif', pix_fmt='rgb24', loop=0)
#             .run(capture_stdout=True, capture_stderr=True)
#     )
#     print("GIF录制完成，保存在：" + filename)
# def record_video(fps: int, filename: str):
#     (
#         # 在这里我选择了mp4格式来保存视频，你也可以根据需要选择其他格式，如：avi, flv, wmv等。
#         ffmpeg
#             .input('desktop', f='gdigrab', offset_x=0, offset_y=0, video_size='1920x1080', framerate=str(fps) + '/1')
#             .output(filename, f='mp4', pix_fmt='yuv420p')
#             .overwrite_output()
#             .run(capture_stdout=True, capture_stderr=True)
#     )
#     print("视频录制完成，保存在：" + filename)


if __name__ == '__main__':
    print()
    # 每30分钟提醒一次
    # interval = 2
    # while True:
    #     休息
        # time.sleep(interval)
        # 显示气泡提醒
        # ctypes.windll.user32.MessageBoxW(0, "该休息了!", "休息提醒", 0x40 | 0x1)

    # record_gif(filename="D:\\workfile\\temp\\screen.gif", fps=25)
