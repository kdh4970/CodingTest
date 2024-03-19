# 주인공의 정보 클래스
class Character:
    def __init__(self, hp, attack, defense, level=1, exp=0, weapon=0, armor=0, accessories=[]):
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.level = level
        self.exp = exp
        self.weapon = weapon
        self.armor = armor
        self.accessories = accessories

    # 무기 착용
    def equip_weapon(self, weapon):
        self.attack += weapon
        self.weapon = weapon

    # 방어구 착용
    def equip_armor(self, armor):
        self.defense += armor
        self.armor = armor

    # 장신구 착용
    def equip_accessory(self, accessory):
        if len(self.accessories) < 4 and accessory not in self.accessories:
            self.accessories.append(accessory)

# 게임 그리드의 상태를 표현하는 클래스
class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['.'] * cols for _ in range(rows)]

    # 그리드에 오브젝트 추가
    def add_object(self, row, col, obj):
        self.grid[row][col] = obj

    # 그리드에서 오브젝트 삭제
    def remove_object(self, row, col):
        self.grid[row][col] = '.'

    # 그리드의 상태 출력
    def print_grid(self):
        for row in self.grid:
            print(''.join(row))

# 게임 결과 출력
def print_game_result(turns, character):
    print("Passed Turns:", turns)
    print("LV:", character.level)
    print("HP:", character.hp, "/", character.max_hp)
    print("ATT:", character.attack, "+", character.weapon)
    print("DEF:", character.defense, "+", character.armor)
    print("EXP:", character.exp, "/", character.level * 5)
    print("YOU WIN!" if character.hp > 0 else f"YOU HAVE BEEN KILLED BY {monster_name}..")

# 게임 그리드의 크기 입력 받기
N, M = map(int, input().split())

# 게임 그리드 생성
grid = Grid(N, M)

# 게임 그리드의 초기 상태 입력 받기
for i in range(N):
    row = input()
    for j in range(M):
        grid.add_object(i, j, row[j])

# 주인공의 이동 방향 입력 받기
commands = input()

# 몬스터 정보 입력 받기
K = int(input())
monsters = []
for _ in range(K):
    R, C, S, W, A, H, E = input().split()
    monsters.append((int(R), int(C), S, int(W), int(A), int(H), int(E)))

# 아이템 상자 정보 입력 받기
L = int(input())
for _ in range(L):
    R, C, T, S = input().split()
    R, C = int(R), int(C)
    if T == 'W' or T == 'A':
        # 무기 또는 방어구 상자 처리
        grid.add_object(R, C, T)
    else:
        # 장신구 상자 처리
        grid.add_object(R, C, T + " " + S)

# 주인공 캐릭터 생성
character = Character(hp=20, attack=2, defense=2)

# 주인공의 이동 및 상호작용 처리
turns = 0
for command in commands:
    # 주인공의 이동 처리
    if command == 'L':
        pass  # 왼쪽 이동 구현
    elif command == 'R':
        pass  # 오른쪽 이동 구현
    elif command == 'U':
        pass  # 위로 이동 구현
    elif command == 'D':
        pass  # 아래로 이동 구현

    # 주인공이 있는 위치의 오브젝트 타입 확인 및 처리
    current_object = grid.get_object(character.row, character.col)
    if current_object == 'M':
        pass  # 보스 몬스터와 전투 구현
    elif current_object == 'B':
        pass  # 아이템 상자 열기 구현
    elif current_object == '^':
        pass  # 가시 함정과 전투 구현

    # 게임 종료 조건 확인
    if character.hp <= 0:
        break
    elif current_object == 'M' and character.hp > 0:
        break
    elif len(commands) == 0:
        break

    turns += 1

# 최종 게임 결과 출력
grid.print_grid()
print_game_result(turns, character)
print("Press any key to continue.")
