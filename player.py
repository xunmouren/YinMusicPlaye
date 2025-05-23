import tkinter as tk
from pygame import mixer
import json

# 加载音乐列表
with open("./data/musiclist.json", "r", encoding="utf-8") as file:
    data = json.load(file)

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.current_index = 0  # 当前播放的音乐索引
        self.is_playing = False  # 当前播放状态
        self.is_paused = False  # 当前是否暂停
        mixer.init()  # 初始化 pygame 的 mixer 模块

    def toggle_play_pause(self):
        """播放或暂停音乐"""
        if self.is_playing and not self.is_paused:
            # 暂停音乐
            mixer.music.pause()
            self.play_pause_button.config(text="播放")  # 切换按钮文本为“播放”
            self.is_paused = True
        elif self.is_paused:
            # 恢复播放
            mixer.music.unpause()
            self.play_pause_button.config(text="暂停")  # 切换按钮文本为“暂停”
            self.is_paused = False
        else:
            # 播放新音乐
            mixer.music.load(data[self.current_index]['path'])  # 加载当前音乐
            mixer.music.play()
            self.play_pause_button.config(text="暂停")  # 切换按钮文本为“暂停”
            self.is_playing = True
            self.is_paused = False

    def next_music(self):
        """播放下一首音乐"""
        self.current_index = (self.current_index + 1) % len(data)  # 循环播放
        mixer.music.load(data[self.current_index]['path'])  # 加载下一首音乐
        mixer.music.play()  # 播放音乐
        self.play_pause_button.config(text="暂停")  # 更新按钮文本为“暂停”
        self.is_playing = True
        self.is_paused = False

    def previous_music(self):
        """播放上一首音乐"""
        self.current_index = (self.current_index - 1) % len(data)  # 循环播放
        mixer.music.load(data[self.current_index]['path'])  # 加载上一首音乐
        mixer.music.play()  # 播放音乐
        self.play_pause_button.config(text="暂停")  # 更新按钮文本为“暂停”
        self.is_playing = True
        self.is_paused = False

    def set_volume(self, volume):
        """设置音量"""
        mixer.music.set_volume(float(volume))  # 音量范围为 0.0 到 1.0

    def create_ui(self):
        """创建播放控制按钮和音量滑块"""
        # 播放/暂停按钮
        self.play_pause_button = tk.Button(self.root, text="播放", command=self.toggle_play_pause)
        self.play_pause_button.pack(pady=10)

        # 下一首按钮
        next_button = tk.Button(self.root, text="下一首", command=self.next_music)
        next_button.pack(pady=10)

        # 上一首按钮
        prev_button = tk.Button(self.root, text="上一首", command=self.previous_music)
        prev_button.pack(pady=10)

        # 音量滑块
        volume_slider = tk.Scale(self.root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="音量", command=self.set_volume)
        volume_slider.set(0.5)  # 默认音量为 50%
        volume_slider.pack(pady=10)
