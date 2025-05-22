import tkinter as tk
from pygame import mixer

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        mixer.init()  # 初始化 pygame 的 mixer 模块

    def bflc(self):
        """播放音乐"""
        try:
            mixer.music.load("./material/music/8flc_dzht.mp3")  # 替换为音频文件路径
            mixer.music.play()
        except Exception as e:
            print(f"播放音乐时出错: {e}")

    def stopmusic(self):
        """停止音乐"""
        try:
            mixer.music.stop()
        except Exception as e:
            print(f"停止音乐时出错: {e}")

    def playmusic(self):
        """创建播放和停止音乐的按钮"""
        # 播放音乐按钮
        cnm_button = tk.Button(self.root, text="播放音乐", command=self.bflc)
        cnm_button.pack(pady=20)

        # 停止音乐按钮
        stop_button = tk.Button(self.root, text="停止音乐", command=self.stopmusic)
        stop_button.pack(pady=20)
