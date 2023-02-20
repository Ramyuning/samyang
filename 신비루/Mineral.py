damage_normal = int(input("기본뎀 입력"))
damage_upgrade = int(input("업글 계수 입력"))
damage_upgradecount = int(input("현제 업글 되어있는 수"))
Unit_count = int(input("현제 유닛 개수 입력"))
Mineral1 = int(input("업글 미네랄 입력"))
Mineral2 = int(input("유닛 미네랄 입력"))

Upgradedamage = damage_upgrade / Mineral1
Unitdamage = Unit_count + 1 / Mineral2