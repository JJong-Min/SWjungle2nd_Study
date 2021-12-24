from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_dic = defaultdict(list)
    genres_total_play_times = defaultdict(int)
    
    for i, play in enumerate(plays):
        genres_dic[genres[i]].append((play, i))
        genres_total_play_times[genres[i]] += play
    
    for genre in genres_dic:
        genres_dic[genre] = sorted(genres_dic[genre], key=lambda x:(-x[0], x[1]))
    
    genres_total_play_times_list = []
    for k, v in genres_total_play_times.items():
        genres_total_play_times_list.append((k, v))
    
    genres_total_play_times_list.sort(key=lambda x:(-x[1]))
    
    for ele in genres_total_play_times_list:
        genre = ele[0]
        music_list = genres_dic[genre]
        if len(music_list) > 1:
            answer.append(music_list[0][1])
            answer.append(music_list[1][1])
        else:
            answer.append(music_list[0][1])
    return answer
