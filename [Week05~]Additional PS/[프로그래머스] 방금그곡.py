def change_shap(music):
    music = music.replace('C#', 'c')
    music = music.replace('D#', 'd')
    music = music.replace('F#', 'f')
    music = music.replace('G#', 'g')
    music = music.replace('A#', 'a')
    return music

def solution(m, musicinfos):
    available_musicinfos = []
    m = change_shap(m)
    # 전처리 과정
    for i, musicinfo in enumerate(musicinfos):
        start_time, end_time, title, music = musicinfo.split(',')
        music = change_shap(music)
        start_hour, start_minute = start_time.split(':')
        end_hour, end_minute = end_time.split(':')
        play_time = (int(end_hour) - int(start_hour)) * 60 + (int(end_minute) - int(start_minute))
        
        if len(music) >= play_time:
            music = music[:play_time]
        else:
            music = music * (play_time // len(music)) + music[:play_time % len(music)]
        
        if m in music: 
            available_musicinfos.append((play_time, i, title))
    
    if available_musicinfos:
        available_musicinfos = sorted(available_musicinfos, key = lambda x: (-x[0], x[1]))
        return available_musicinfos[0][2]
    
    return  "(None)"
        
