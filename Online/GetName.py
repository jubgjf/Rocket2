import tkinter
import sys
import os
import json

sys.path.append('..')


def launch_online(my_name):
    os.system('python Online/Client.py %s' % my_name)


def find_exist_name():
    try:
        with open(r'Online/Name.json', 'r') as f:
            name = json.load(f)
    except FileNotFoundError:
        return 0

    return name


def save_name():
    global name_entry

    name = name_entry.get()

    with open(r'Online/Name.json', 'w') as f:
        json.dump(name, f)

    launch_online(name)


def draw_window():
    ''' 设置窗口 '''
    window = tkinter.Tk()
    window.title('Rocket2')
    window.geometry('500x400')
    ''' Logo '''
    Logo = tkinter.PhotoImage(file="pictures/Online/Online.png")
    logo_label = tkinter.Label(window, image=Logo)
    logo_label.pack()
    ''' 标题 '''
    title_label = tkinter.Label(window, text='Rocket2联机模式', font=('Consolas', 18))
    title_label.pack()
    ''' 文本框标签 '''
    name_label = tkinter.Label(window, text="请输入玩家名称", font=('等线', 12))
    ''' 文本框 '''
    name = tkinter.StringVar()

    global name_entry
    name_entry = tkinter.Entry(window, show=None, textvariable=name)
    ''' 显示文本框及其标签 '''
    name_label.pack()
    name_entry.pack()
    ''' 按钮 '''
    button = tkinter.Button(window,
                            text='开始游戏',
                            font=('等线', 10),
                            command=save_name)
    button.pack()
    ''' 主循环 '''
    tkinter.mainloop()


if __name__ == '__main__':
    if find_exist_name() == 0:
        draw_window()
    else:
        name = find_exist_name()
        launch_online(name)
