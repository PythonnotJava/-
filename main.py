# 用户窗口
import os
from configobj import ConfigObj
import tkinter
from PIL import ImageTk,Image
import snow_draw
import commands
import drawtree
import on_it
from tkinter.messagebox import showinfo

root = tkinter.Tk()
size = 500, 400
root.title('冬至迈向新年的礼物')
root.iconbitmap('favicon.ico')
root.geometry(f'{size[0]}x{size[1]}')
root.resizable(False, False)
# root.config(bg='silver')

# 我们将定义如下功能：开始、调整雪花个数、窗口自适应图片大小比例、导入别的图片、修改图片透明度、修改背景音乐、修复注册机
# 如上功能由按钮事件触发的，将会随着窗口变化而改变按钮自适应(由于源代码开源，使用者可能考虑修改用户界面的大小，这里我因此灵活点)

# 封面初始化
init_value_cover = list(ConfigObj('cover.ini').values())[0]

# 先导入界面背景图片
image = Image.open(init_value_cover)
bg_image = ImageTk.PhotoImage(image)
width = bg_image.width()
height = bg_image.height()
root.geometry('%dx%d+0+0' % (width, height))
background_label = tkinter.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# 开始按钮
button10 = tkinter.Button(root, text='看雪', font=('华文行楷', 14),
                         bg='silver', fg='red', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=snow_draw.main)
# 圣诞节版本
button100 = tkinter.Button(root, text='Christmas', font=('华文行楷', 14),
                         bg='silver', fg='yellow', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=drawtree.main)

button10.place(x=int(float(size[0] * 0.8)), y=int(float(0.05 * size[1])))
button100.place(x=int(float(size[0] * 0.55)), y=int(float(0.05 * size[1])))



# 调整雪花个数按钮
button11 = tkinter.Button(root, text='雪花个数', font=('华文行楷', 14),
                         bg='silver', fg='blue', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=commands.snow_num)

button11.place(x=int(float(size[0] * 0.8)), y=int(float(0.20 * size[1])))


# 雪花窗口图片自适应图片按钮
button12 = tkinter.Button(root, text='自适应', font=('华文行楷', 14),
                         bg='silver', fg='black', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=commands.fit)
button12.place(x=int(float(size[0] * 0.8)), y=int(float(0.35 * size[1])))

# 导入别的图片
button13 = tkinter.Button(root, text='导入图片', font=('华文行楷', 14),
                         bg='silver', fg='yellow', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=commands.import_image)
button13.place(x=int(float(size[0] * 0.8)), y=int(float(0.5 * size[1])))

# 导入别的背景音乐
button14 = tkinter.Button(root, text='导入音乐', font=('华文行楷', 14),
                         bg='silver', fg='indigo', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=commands.music)
button14.place(x=int(float(size[0] * 0.8)), y=int(float(0.65 * size[1])))

# 修改图片透明度
button15 = tkinter.Button(root, text='透明度', font=('华文行楷', 14),
                         bg='silver', fg='green', width=int(float(size[0] * 0.02)), height=int(float(0.0025 * size[1])),
                          command=commands.alpha)
button15.place(x=int(float(size[0] * 0.8)), y=int(float(0.8 * size[1])))

# 菜单
menu = tkinter.Menu(root)
root['menu'] = menu
f1 = tkinter.Menu(menu, tearoff=False)
f1.add_command(label='重置注册机', command=commands.reg)
f1.add_command(label='关于', command=on_it.show_on)
menu.add_cascade(label='菜单', menu=f1)

def hu():
    os.startfile('new_year')

f2 = tkinter.Menu(menu, tearoff=False)
f2.add_cascade(label='虎年特别版本', command=hu)
menu.add_cascade(label='虎年特别版本', menu=f2, command=hu)

root.mainloop()