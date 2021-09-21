# 효율성 통과
import sys
sys.setrecursionlimit(10000000) # 설정해주지 않으면 재귀가 많이 일어나면서 런타임에러 등이 나타날 수 있다.

def findEmptyRoom(number, rooms): # 빈방을 찾는 함수
    if number not in rooms:        
        rooms[number] = number + 1
        return number
    
    empty = findEmptyRoom(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = dict() # 몇번 방이 비어있는지 체크하는 딕셔너리

    for number in room_number:
        emptyRoom = findEmptyRoom(number, rooms)
        answer.append(emptyRoom)
    
    return answer


# 시간초과(rooms를 {}으로 선언한게 큰가?)
import sys
sys.setrecursionlimit(10000000)

def findEmptyRoom(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    
    empty = findEmptyRoom(rooms[number], rooms)
    rooms[empty] = empty + 1
    return empty

def solution(k, room_number):
    rooms = {}
    answer = []
    for number in room_number:
        allocated_room_num = findEmptyRoom(number, rooms)
        answer.append(allocated_room_num)
    
    return answer
