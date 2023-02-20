T = int(input())
X=[]
Y=[]
running = True
def calculator(K,D,X,W):
    Y_sec= [] # Y가 될 위치를 저장하는 리스트
    Stack = []
    moment= []
    F_sum= []
    for i in range(K):
        while True:
            sum = 0
            if len(Stack) == 0:
                Stack.append(X[i])
            elif Stack[-1] != X[i] and Stack.count(X[i]) == 0:
                Stack.append(X[i])
            else: 
                break
            for _ in range(X.count(X[i])):
                Y_sec.append(X.index(Stack[-1])) # Stack의 마지막 수(X가 가르키는 수)가 가르키는 수들 전부 Y_sec에 저장
            for i in range(len(Y_sec)): # 지어지는 시간 저장(최대값으로다가)
                moment.append(D[Y_sec[i]])
                sum += max(moment)
            del Stack[-1]
            Stack.append(Y_sec) # 위아래 포함 3문장 반복?
            Y_sec.clear()
            if Stack[-1] not in X: # 더이상 갈길이 없다면?
                if Stack[-1] == W: # 그 값이 W라면 최종결과에 저장
                    F_sum.append(sum) # 최종 결과에 저장
                    sum = 0
                elif Stack.index == 0: #만일 Stack이 다 끝났다면 
                    break
                else: # W가 아니라면 최종결과에 저장하지 않음
                    pass
            else: # 갈길이 있으면 계속 반복분 돌리기
                pass
    return F_sum
for i in range(T):
    N, K = map(int, input().split()) #N과 K 입력 K는 규칙의 총 개수
    D = list(map(int,input().split())) #D건설에 걸리는 시간 리스트형식으로 입력
    for _ in range (K): #K번째까지 건설순서 주어짐
        O, P = map(int, input().split())
        X.append(O-1)
        Y.append(P-1)
    W = int(input()) # 건설해야하는 번호
    result = calculator(K, D, X, W)
    print(result)

# 개같이 유기각 ㅋㅋ