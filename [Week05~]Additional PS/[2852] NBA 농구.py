import sys

n = int(sys.stdin.readline())

first_team_winning_time = 0
second_team_winning_time = 0
total_time = 48 * 60
infos = []

for _ in range(n):
    team, time = map(str, sys.stdin.readline().split())
    time = time.split(':')
    time = int(time[0]) * 60 + int(time[1])
    infos.append([team, time])

team_score = {'1':0, '2':0}
standard_time = {'1':0, '2':0}
check_zero_start = {'1':0, '2':0}

for team, time in infos:
    if team == '1':
        team_score[team] += 1
        if team_score[team] > team_score['2']:
            if time == 0:
                check_zero_start[team] = 1
            elif standard_time[team] == 0 and not check_zero_start[team]:
                standard_time[team] = time
        elif team_score[team] == team_score['2']:
            second_team_winning_time += (time - standard_time['2'])
            standard_time['2'] = 0
            check_zero_start['2'] = 0
    else:
        team_score[team] += 1
        if team_score[team] > team_score['1']:
            if time == 0:
                check_zero_start[team] = 1
            elif standard_time[team] == 0 and not check_zero_start[team]:
                standard_time[team] = time
        elif team_score[team] == team_score['1']:
            first_team_winning_time += (time - standard_time['1'])
            standard_time['1'] = 0
            check_zero_start['1'] = 0

if team_score['1'] > team_score['2']:
    first_team_winning_time += (total_time - standard_time['1'])

elif team_score['2'] > team_score['1']:
    second_team_winning_time += (total_time - standard_time['2'])
                            
    


first_team_winning_minute = str(first_team_winning_time // 60)
first_team_winning_seconds = str(first_team_winning_time % 60)
first_team_winning_time = first_team_winning_minute.zfill(2) + ':' + first_team_winning_seconds.zfill(2)

second_team_winning_minute = str(second_team_winning_time // 60)
second_team_winning_seconds = str(second_team_winning_time % 60)
second_team_winning_time = second_team_winning_minute.zfill(2) + ':' + second_team_winning_seconds.zfill(2)

print(first_team_winning_time)
print(second_team_winning_time)
