import tkinter as tk
from tkinter import filedialog, messagebox

def filemain(root):

    # 文件操作函数
    def new_file(status_bar):
        # 新建文件逻辑
        status_bar.config(text="状态: 新建文件")
        print("新建文件")

    def open_file(status_bar):
        # 打开文件逻辑
        file_path = filedialog.askopenfilename(title="打开文件", filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(f"打开文件: {file_path}")
                print(content)
            status_bar.config(text=f"状态: 打开文件 {file_path}")

    def save_file(status_bar):
        # 保存文件逻辑
        file_path = filedialog.asksaveasfilename(title="保存文件", defaultextension=".txt",
                                                 filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")])
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("示例内容")  # 这里可以替换为实际内容
            print(f"保存文件: {file_path}")
            status_bar.config(text=f"状态: 保存文件 {file_path}")

    def show_about():
        # 显示关于信息
        messagebox.showinfo("关于", "这是一个示例 Tkinter 应用程序，演示菜单和状态栏功能。")

    # 添加菜单栏
    menu_bar = tk.Menu(root)

    # 文件菜单
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="新建", command=lambda: new_file(status_bar))
    file_menu.add_command(label="打开", command=lambda: open_file(status_bar))
    file_menu.add_command(label="保存", command=lambda: save_file(status_bar))
    file_menu.add_separator()
    file_menu.add_command(label="退出", command=root.quit)
    menu_bar.add_cascade(label="文件", menu=file_menu)

    # 帮助菜单
    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="关于", command=show_about)  # 确保 show_about 已定义
    menu_bar.add_cascade(label="帮助", menu=help_menu)

    root.config(menu=menu_bar)

    # 添加状态栏
    status_bar = tk.Label(root, text="状态: 就绪", bd=1, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)