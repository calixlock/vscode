from tkinter import *
root = Tk()

root.title("test GUI") # 실행창 이름
root.geometry("640x480") # 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,1) # 창 가로,세로 값변경 (허용1 , 불허0)

# 사용할 이미지
photo = PhotoImage(file="gui_basic/check.png")
photo2 = PhotoImage(file="gui_basic/x.png")

#

label1 = Label(root, text="label test")
label1.pack()

label2 = Label(root, image = photo)
label2.pack()

def change():
    label1.config(text="change text")
    label2.config(image=photo2)    


btn = Button(root, text="O", command=change)
btn.pack()

root.mainloop()