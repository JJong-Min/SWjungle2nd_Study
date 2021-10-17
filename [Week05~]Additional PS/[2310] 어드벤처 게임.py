import sys

sys.setrecursionlimit(100000)

actions = {"E": lambda poc, val: poc,
           "L": lambda poc, val: poc if poc > val else val,
           "T": lambda poc, val: poc - val}


class Game:
    def __init__(self, n):
        self.n = n
        self.miros = [{}]
        for _ in range(n):
            room = input().strip().split(' ')
            self.miros.append({"type": room[0], "value": int(room[1]), "rooms": list(map(int, room[2:-1]))})
        self.success = False
        self.visited = [False for i in range(n + 1)]

    def dfs(self, room_i, pocket):
        room = self.miros[room_i]
        n_pocket = actions[room["type"]](pocket, room["value"])
        if n_pocket >= 0:
            if room_i == n:
                self.success = True
                return 0
            else:
                for new_room_i in room["rooms"]:
                    if new_room_i != room_i and not self.visited[new_room_i]:
                        self.visited[new_room_i] = True
                        self.dfs(new_room_i, n_pocket)
                        self.visited[new_room_i] = False
        self.visited[room_i] = False

    def main(self):
        self.dfs(1, pocket=0)
        if self.success:
            return "Yes"
        return "No"


answers = []
while True:
    n = int(input().strip())
    if n == 0:
        break
    game = Game(n)
    answers.append(game.main())

print('\n'.join(answers))
