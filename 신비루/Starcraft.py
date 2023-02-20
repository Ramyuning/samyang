from random import *
#일반유닛
from practice_class import FlyableUnit


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성 되었습니다.".format(name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("이 유닛은 파괴되었습니다.")

#공격유닛
class AttackUnit(Unit): #상속 Unit
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage))


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)
    
    #스팀팩 : 일정 시간 동안 이동 및 공격속도 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10감소)". format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 못했습니다.".format(self.name))

#탱크
class Tank(AttackUnit):
    #시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동불가
    seize_developed = False #시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mod = False

    def set_seize_mode(self) :
        if Tank.seize_developed == False:
            return True
        
        # 현재 시즈모드 아닐 때 ->시즈모드
        if self.seize_mod == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mod = True
        # 현재 시즈모드 일 때 -> 탱크모드
        else:
            print("{0} : 탱크모드로 전환합니다.".format(self.name))
            self.damage /= 2
            self.seize_mod = False
        

#드랍쉽 : 공중 유닛, 수송기. 마린/ 파뱃/ 탱크를 태우고댕김 공격불가

#날수있는 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날라갑니다~. [속도 {2}]"\
            .format(name,location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # move의 재정의가 들어감
        self.fly(self.name, location)

#레이스
class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드
        
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")
def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

#실제 게임 시작
game_start()

#마린 3기 생성
m1=Marine()
m2=Marine()
m3=Marine()

#탱크 2기 생성
t1=Tank()
t2=Tank()

# 레이스 1기 생성
w1 =wraith()

#유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("탱크 시즈모드 개발이 완료되었습니다.")

#공격 모드 준비 (마린: 싀팀팩, 탱크 : 시즈, 레이스: 클로킹)
for Unit in attack_units:
    if isinstance(Unit, Marine):
        Unit.stimpack()
    elif isinstance(Unit, Tank):
        Unit.set_seize_mode()
    elif isinstance(Unit, wraith):
        Unit.clocking()

#전군 1시방향 공격
for Unit in attack_units:
    Unit.attack("1시")

#전군 피해
for Unit in attack_units:
    Unit.damaged(randint(5,20)) # 공격은 랜덤으로 받음 (5~20)

# 게임 종료
game_over()