import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("GUI PROGRAM!")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 32까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정


readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)# 0번째 인덱스값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get())
    print(readonly_combobox.get())
btn = Button(root, text="주문", command=btncmd)
btn.pack()


root.mainloop()