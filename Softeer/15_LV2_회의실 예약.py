import sys

N,M = map(int,input().split())
rooms = [input() for _ in range(N)]
books = [list(input().split()) for _ in range(M)]

booked = [[False] *9 for _ in range(N)]
rooms.sort()
room_d = dict()
for _ in range(N):
    room_d[rooms[_]] = _
# room 별로 stk 구성

for book in books:
    room = book[0]
    start_time = int(book[1])-9
    end_time = int(book[2])-9
    room_id = room_d[room]
    for t in range(start_time,end_time):
        # print(f"{room} reserved time {t}")
        booked[room_id][t] = True
        
for id,name in zip(range(N),rooms):
    print(f"Room {name}:")
    if sum(booked[id])==9:
        print("Not available")
    else:
        isSegment = False
        segment=[]
        for _ in range(9):
            if booked[id][_]==False and not isSegment:
                segment.append(_)
                isSegment = True
            elif booked[id][_]==True and isSegment:
                segment.append(_)
                isSegment = False
            elif _==8 and booked[id][_]==False:
                segment.append(_+1)
                isSegment = False
            else:
                continue
        print(f"{len(segment)//2 if len(segment)%2==0 else len(segment)//2+1} available:")
        for _ in range(len(segment)//2):
            if segment[2*_]==0:
                print(f"09-{segment[2*_+1]+9}")
            else:
                print(f"{segment[2*_]+9}-{segment[2*_+1]+9}")
        if len(segment)%2==1:
            print("17-18")
    if id!= N-1:
        print("-----")

        