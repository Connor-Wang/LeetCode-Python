class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = set()
        head = 0
        max = 0
        for i in range(s.__len__()):
            while(s[i] in queue):
                queue.remove(s[head])
                head += 1
            queue.add(s[i])
            max = max if max >= i-head+1 else i-head+1
        return max

if __name__ == "__main__":
    s = Solution()
    inp = "qwwkew"
    print(s.lengthOfLongestSubstring(inp))