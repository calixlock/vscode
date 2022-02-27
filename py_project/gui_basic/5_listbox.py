from tkinter import *
root = Tk()

root.title("test GUI") # 실행창 이름
root.geometry("640x480") # 창 크기 // 가로x세로 + x좌표 + y좌표 
root.resizable(1,0) # 창 가로,세로 값변경 (허용1 , 불허0)

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(END,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")

listbox.pack()


txt = Text(root, width=20 , height=0)
txt.pack()

def btncmd():
    
    #   listbox.delete(0) # 맨 앞부터 삭제
    #   listbox.delete(END) # 맨 뒤부터 삭제
      txt.delete("1.0",END)
      txt.insert(END, listbox.size())

def btncmd1():
    
    # print(listbox.get(0,2)) # (시작 idx, 끝 idx)
    print(listbox.curselection())# ("선택된 항목의 index 값 반환")



btn = Button(root, text="클릭", command=btncmd1)
btn.pack()

root.mainloop()