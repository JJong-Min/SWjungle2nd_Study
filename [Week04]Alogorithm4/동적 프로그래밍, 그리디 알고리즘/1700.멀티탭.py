

# 27퍼 틀림
import sys

n, k = map(int, sys.stdin.readline().split())
plugs = list(map(int, sys.stdin.readline().split()))

now_plugin = set(plugs[:n])
left_plug = n - len(now_plugin)
cnt  = 0
for i in range(n, k, n):
    # 새롭게 들어갈 제품들
    new_plugin = set(plugs[i: i + n])
    # 꽃인 것 중 나와야할 것들
    out_plug = now_plugin - new_plugin
    # 들어가야한 것들
    in_plug = new_plugin - now_plugin

    if len(out_plug) == 0 or len(in_plug) == 0:
        continue
    else:
        now_plugin = new_plugin
        if len(out_plug) > len(in_plug):
            cnt += len(in_plug) - left_plug
        else:
            cnt += len(out_plug) - left_plug
        left_plug = n - len(now_plugin)

print(cnt)
            
    

    
    
