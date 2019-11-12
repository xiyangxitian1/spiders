import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
txt = tk.StringVar()
label = tk.Label(root, textvariable=txt, background='blue', width=30)
label.pack()

ent = tk.Entry(root, width=60)
ent.pack()


def hit_me():
    """点击事件"""
    my_text = ent.get()  # 获取输入框中的输入
    txt.set(my_text)  # 设置内容


btn = tk.Button(root, text='hit me', command=hit_me)
btn.pack()

root.mainloop()
