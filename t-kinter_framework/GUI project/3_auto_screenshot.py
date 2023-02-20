import time
from PIL import ImageGrab

time.sleep(5) #5초 대기: 사용자가 준비하는 시간

for i in range(1,11): #2 초 간격으로 10장
    img = ImageGrab.grab() # 현재 스크린의 이미지를 가져옴
    img.save("image{}.png".format(i)) #파일로 저장
    time.sleep(2)