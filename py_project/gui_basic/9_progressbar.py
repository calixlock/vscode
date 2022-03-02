from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()

root.title("test GUI")  # 실행창 이름
root.geometry("640x480")# 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0)     # 창 가로,세로 값변경 (허용1 , 불허0)


#progress bar

# # 1 progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()


# 2 
p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100,length = 150, variable = p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar2.update()
        print(p_var2.get())

btn2 = Button(root, text="클릭", command = btncmd2)
btn2.pack()

root.mainloop()