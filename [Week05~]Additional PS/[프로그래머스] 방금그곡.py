import heapq
def check_m(m, i, play_song):
    if len(play_song[i:]) < len(m):
        val_song = play_song[i:] + play_song[:len(m) - len(play_song[i:])]
    else:
        val_song = play_song[i:len(m)]

    for um, mm in zip(val_song, m):
        if um != mm:
            return False
    else:
        return True

def change_shap(strings):
    if 'C#' in strings:
        strings = strings.replace('C#', 'c')
    if 'D#' in strings:
        strings = strings.replace('D#', 'd')
    if 'F#' in strings:
        strings = strings.replace('F#', 'f')
    if 'G#' in strings:
        strings = strings.replace('G#', 'g')
    if 'A#' in strings:
        strings = strings.replace('A#', 'a')
    return strings

def solution(m, musicinfos):
    heap = []
    heapq.heapify(heap)
    musicinfos = [musicinfo.split(',') for musicinfo in musicinfos]
    m = change_shap(m)
    cnt = 0
    for musicinfo in musicinfos:
        cnt += 1
        play_time = (int(musicinfo[1][:2]) - int(musicinfo[0][:2])) * 60 + (int(musicinfo[1][3:]) - int(musicinfo[0][3:]))
        play_song = ''
        if len(musicinfo[3]) >= play_time:
            play_song = musicinfo[3][:play_time]
        else:
            t = (play_time - len(musicinfo[3])) // len(musicinfo[3])
            r = (play_time - len(musicinfo[3])) % len(musicinfo[3])
            play_song = musicinfo[3] + musicinfo[3] * t + musicinfo[3][:r]

        for i in range(len(play_song)):
            if m[0] == play_song[i] and check_m(m, i, play_song):
                heapq.heappush(heap, (-play_time, cnt, musicinfo[2]))
                break

    if heap:
        return heapq.heappop(heap)[2]   
    else:
        return None

m = 'CC#BCC#BCC#BCC#B'
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

print(solution(m, musicinfos))
