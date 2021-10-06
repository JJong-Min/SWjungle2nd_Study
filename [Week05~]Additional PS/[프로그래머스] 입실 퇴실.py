from collections import defaultdict, deque

def solution(enter, leave):
    answer = []
    person_meet_cnt = defaultdict(int)
    stack = []
    queue = deque(leave)
    
    for _enter in enter:
        stack.append(_enter)
        if len(stack) > 1:
            for _stack in stack[:-1]:
                person_meet_cnt[_stack] += 1
            person_meet_cnt[stack[-1]] += len(stack) - 1

        while queue and queue[0] in stack:
            stack.remove(queue[0])
            queue.popleft()

    answer = [person_meet_cnt[i] for i in range(1, len(enter) + 1)]

    return answer

enter = [1, 4, 2, 3]
leave = [2, 1, 3, 4]

print(solution(enter, leave))
