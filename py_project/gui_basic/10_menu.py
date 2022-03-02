from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()

root.title("test GUI")  # 실행창 이름
root.geometry("640x480")# 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0)     # 창 가로,세로 값변경 (허용1 , 불허0)
##################################################################
def create_new_file():
    print("make a new file")


menu = Menu(root)
# file 메뉴 
menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label= "new file", command=create_new_file) # 함수 사용
menu_file.add_separator()
menu_file.add_command(label= "open file file")
menu_file.add_separator()
menu_file.add_command(label= "save all", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label= "exit", command = root.quit)

menu.add_cascade(label="file", menu=menu_file)

menu.add_cascade(label="edit")

root.config(menu=menu)

##################################################################
def btncmd():
    pass

btn = Button(root, text="클릭", command = btncmd)
btn.pack()

root.mainloop()