import math
A = []
B= []
N = 10000 # 찾고자 하는 범위
C = math.floor(math.sqrt(N)) + 1
D = math.floor((N+1)/2)
E = []
sum = 0
for i in range(N +1):
    A.append(i)
for i in range(N + 1):
    E.append(1)
for num in range(2,C):
    if E[num] != 1:
        continue
    k = 2
    while True:
        try:
            E[num * k] = 0 
        except:
            pass 
        k += 1
        if num * k > N:
            break
E[0] = 0
E[1] = 0