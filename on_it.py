def show_on():
    import tkinter
    from tkinter.scrolledtext import ScrolledText

    win = tkinter.Tk()
    win.geometry('1200x600')
    win.title('关于面板')
    win.resizable(False, False)
    win.iconbitmap('favicon.ico')
    # read a Text
    text = open('author.txt', 'r', encoding='utf-8')
    text = text.read()
    # 把文本放在框内
    # font = fontOperation()
    view_text = ScrolledText(win, font=('黑体', 12), fg='black', bg='white')
    view_text.insert('0.0', text)
    view_text.place(x=10, y=5, height=600 - 20, width=1200-20)



    win.mainloop()