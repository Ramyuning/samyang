from tkinter import *
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("제목 없음 - Windows 메모장")
menu = Menu(root)
frame = Frame(root)
frame.pack(expand=True, fill="both")
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
txt = Text(frame, yscrollcommand=scrollbar.set)
txt.pack(side="left",expand=True,fill="both")
def OPEN():
    #if os.path.isfile(filename): 있으면 True, 없으면 False import os 해야함
    f = open("C:\\Users\\조정현\\Desktop\\python workspace\\신비루\\mynote.txt", "r" ,encoding="utf8")
    txt.delete("1.0",END)
    line = f.read()
    txt.insert(END, line)
    f.close()
def store():
    f = open("C:\\Users\\조정현\\Desktop\\python workspace\\신비루\\mynote.txt", "w" ,encoding="utf8")
    f.write(txt.get("1.0",END))
    f.close()
    
menu_file= Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=OPEN)
menu_file.add_command(label="저장", command=store)
menu_file.add_command(label="끝내기", command=root.quit)



menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()