class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones = list(stones)
        s_dict = collections.Counter(stones)
        answer = 0
        for jewel in jewels:
            answer += s_dict[jewel]
        
        return answer


# 리스트 컴프리헨션을 이용한 출이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in J for s in S)
