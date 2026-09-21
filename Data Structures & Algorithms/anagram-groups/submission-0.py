class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hash = defaultdict(list)

        for s in strs:
            count = [0] * 26 #알파벳 26개라 인덱스가 각 알파벳 몇번 나왔는지 체크 
            
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            my_hash[tuple(count)].append(s)
        
        return list(my_hash.values())
        