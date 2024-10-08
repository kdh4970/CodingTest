# 2204 ~ 2306
# 1.각 블럭의 한점을 x,y로 인자로 받아 블럭 내 영역을 리스트로 리턴하는 함수
n,m = map(int,input().rstrip().split(" "))
board = [list(map(int,input().rstrip().split(" "))) for _ in range(n)]
blocks=[] 

# block 1 - 단방향 네칸
block1=[]
block1.append([(0,x) for x in range(0,4)])
block1.append([(x,0) for x in range(0,4)])
blocks.append(block1)

# block 2 - 양방향 두칸 정사각형
block2=[]
block2.append([(0,0),(0,1),(1,0),(1,1)])
blocks.append(block2)

# block 3 - 단방향 세칸 직교방향 두칸
'''
x##  #   ##x   #  x# #x #   #
#    x##   # ##x  #   # #   #
                  #   # x# #x
'''
block3=[]
block3.append([(0,0),(0,1),(0,2),(1,0)]) 
block3.append([(0,0),(0,1),(0,2),(-1,0)]) 
block3.append([(0,0),(0,-1),(0,-2),(1,0)])
block3.append([(0,0),(0,-1),(0,-2),(-1,0)]) 
block3.append([(0,0),(1,0),(2,0),(0,1)]) 
block3.append([(0,0),(1,0),(2,0),(0,-1)]) 
block3.append([(0,0),(-1,0),(-2,0),(0,1)]) 
block3.append([(0,0),(-1,0),(-2,0),(0,-1)]) 
blocks.append(block3)

# block 4
'''
#   #  x# #x
x# #x ##   ##
 # #
'''
block4=[]
block4.append([(0,0),(-1,0),(0,1),(1,1)])
block4.append([(0,0),(-1,0),(0,-1),(1,-1)])
block4.append([(0,0),(0,1),(1,0),(1,-1)])
block4.append([(0,0),(0,-1),(1,0),(1,1)])
blocks.append(block4)

# block 5
'''
#   #  #
x# #x #x# #x#
#   #      #
'''
block5=[]
block5.append([(0,0),(-1,0),(0,1),(1,0)])
block5.append([(0,0),(-1,0),(0,-1),(1,0)])
block5.append([(0,0),(-1,0),(0,1),(0,-1)])
block5.append([(0,0),(1,0),(0,1),(0,-1)])
blocks.append(block5)

max_val=0
def scan(x,y):
    global max_val,combination
    for block_id in blocks: # 1~5번 블럭
        for block in block_id: # 한 블럭의 케이스
            try:
                tmp=0
                for direction in block:# 한 케이스의 구성 좌표
                    r=x+direction[0]
                    c=y+direction[1]
                    if r<0 or c<0:
                        tmp=0
                        break
                    tmp+=board[r][c]
                max_val=max(max_val,tmp)
            except IndexError as e:
                continue

for r in range(n):
    for c in range(m):
        scan(r,c)
print(max_val)