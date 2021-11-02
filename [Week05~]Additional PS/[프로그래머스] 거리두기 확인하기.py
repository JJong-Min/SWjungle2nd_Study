def solution(places):
    answer = []
    for place in places:
        P_seats = []
        flag = True
        inner_break = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    P_seats.append([i,j])
        
        for idx_1 in range(len(P_seats)):
            for idx_2 in range(len(P_seats)):
                Manhattan_distance = abs(P_seats[idx_1][0]-P_seats[idx_2][0])+abs(P_seats[idx_1][1]-P_seats[idx_2][1])
                
                if Manhattan_distance == 1:
                    inner_break = False
                    flag = False
                    break
                elif Manhattan_distance == 2:
                    if P_seats[idx_1][0] == P_seats[idx_2][0]:
                        x = P_seats[idx_1][0]
                        y = max(P_seats[idx_1][1], P_seats[idx_2][1]) - 1
                        if place[x][y] == 'O':
                            inner_break = False
                            flag = False
                            break
                    
                    elif P_seats[idx_1][1] == P_seats[idx_2][1]:
                        x = max(P_seats[idx_1][0], P_seats[idx_2][0]) - 1
                        y = P_seats[idx_1][1]
                        if place[x][y] == 'O':
                            inner_break = False
                            flag = False
                            break
                    
                    else:
                        x_1 = min(P_seats[idx_1][0], P_seats[idx_2][0])
                        x_2 = max(P_seats[idx_1][0], P_seats[idx_2][0])
                        y_1 = min(P_seats[idx_1][1], P_seats[idx_2][1])
                        y_2 = max(P_seats[idx_1][1], P_seats[idx_2][1])
                        if place[x_1][y_1] == 'O' or place[x_2][y_2] == 'O':
                            inner_break = False
                            flag = False
                            break
            
            if inner_break == False:
                break
        
        if flag:
            answer.append(1)
        else:
            answer.append(0)
                             
        
    return answer
