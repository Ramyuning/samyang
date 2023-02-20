# 일반 가격
def price(people):
    print("{0}명 가격은 {1}(10000)원 입니다.".format(people, people * 10000))

# 조조할인 가격
def price_morning(people):
    print("{0}명 조조 할인 가격은 {1}(6000)원 입니다.".format(people, people * 6000))

#군인 할인 가격
def price_soldier(people):
    print("{0}명 군인 할인 가격은 {1}(4000)원 입니다.".format(people, people * 4000))