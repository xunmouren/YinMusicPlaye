import tkinter as tk
from MainPackage.buttonfk import buttonmain  # 从 MainPackage 导入 buttonmain 函数
from MainPackage.filefk import filemain  # 从 MainPackage 导入 filemain 函数
from player import MusicPlayer  # 从 yulePackage 导入 MusicPlayer 类

# 创建主窗口实例
root = tk.Tk()
root.title("阴乐播放器")
root.geometry("800x450")  # 设置窗口大小

# 调用 buttonmain 函数，将主窗口实例 root 传递给它
buttonmain(root)
# 调用 filemain 函数，将主窗口实例 root 传递给它
filemain(root)
# 创建 MusicPlayer 实例
player = MusicPlayer(root)

# 创建用户界面
player.create_ui()

# 进入主事件循环
root.mainloop()
