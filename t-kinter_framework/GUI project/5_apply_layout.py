from tkinter import * # __all__\
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import filedialog # submodule은 없ㅇ서ㅓ그래서 이걸 불러옴
from PIL import Image
import os
root = Tk()
root.title("GUI PROGRAM!")

#파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요", \
        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),\
        initialdir=r"C:\Users\조정현\Desktop") #최초에 사용자가 지정한 경로를 보여줌

    #사용자가 선택한 파일 목록 선택
    for file in files:
        list_file.insert(END, file)

#선택 삭제
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로
def browse_dest_path():
    
    folder_selected = filedialog.askdirectory()
    if folder_selected is '': #사용자가 취소를 누를때
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)


# 이미지 통합 작업
def merge_image():
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())
    #가로넓이
    try:
        img_width = cmb_width.get()
        if img_width == "원본유지":
            img_width = -1 # -1 일때는 원본 기준으로
        else:
            img_width = int(img_width)
        #간격
        img_space = cmb_space.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else:
            img_space = 0
        img_format = cmb_format.get().lower() # 문자값 소문자로 변경

        images = [Image.open(x) for x in list_file.get(0,END)]

        #이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []
        if img_width > -1:
            # width값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1]/ x.size[0]))for x in images]
        else:
            #원본 사이즈 사용
            image_sizes = [(x.size[0],x.size[1]) for x in images]

        #계산식
        # 100 * 60 이미지가 있음. -> width를 80으로 줄이면 height는?
        # 원본 width : 원본 height = 변경 width : 변경 height
        

        widths, heights = zip(*(image_sizes))
        #최대 넓이 , 높이 총합
        max_width, total_height = max(widths), sum(heights)

        #스케치북 준비
        if img_space > 0: #이미지 간격 옵션 적용
            total_height += (img_space * len(images)-1)
        result_img = Image.new("RGB", (max_width, total_height), (255,255,255))
        y_offset = 0 # y위치
        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1] # height 값 만큼 더해줌

        for idx, img in enumerate(images):
            #width 원본유지가 아닐경우
            if img_width > -1:
                img = img.resize(image_sizes[idx])
            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) #height값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 #실제 %정보 계산
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = "nado_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다")
    except Exception as err:
        msgbox.showerror("에러", err)



# 시작
def Start():
    # 각 옵션들 값 확인
    # print("가로넓이 : ", cmb_width.get())
    # print("간격 : ", cmb_space.get())
    # print("포맷 : ", cmb_format.get())
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return
    
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return
    merge_image()
    
   



# 파일 프레임 (파일 추가와 선택/삭제)
file_frame= Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, text="파일 추가", padx=5, pady=5, width=12, command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, text="선택삭제", padx=5, pady=5, width=12,command=del_file)
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill='y')

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand= scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4) #높이 변경
txt_dest_path.insert(0, r"C:\Users\조정현\Desktop\python workspace\t-kinter_framework\GUI project")

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5, ipady=5)

# 가로 넓이 옵션
#가로넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left", padx=5, pady=5)
#가로넓이 콤보
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# 간격 옵션 콤보
opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 파일 포맷 옵션
# 파일 포맷 레이블
lbl_format = Label(frame_option, text="포맷", width=8)
lbl_format.pack(side="left", padx=5, pady=5)
# 파일 포맷 콤보
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)

# 진행 상황 Prograss Bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

#실행 프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)


btn_stop = Button(frame_run, padx=5, pady=5, width=12, text="닫기", command=root.quit)
btn_stop.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=Start)
btn_start.pack(side="right", padx=5, pady=5)


root.resizable(False,False) #너비,높이 변경 불가
root.mainloop()