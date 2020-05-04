class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = [[None] * len(text2) for _ in range(len(text1))]

        # base case
        mem[0][0] = 1 if text1[0] == text2[0] else 0
        for i in range(1, len(text1)):
            if mem[i - 1][0] == 1:
                mem[i][0] = 1
            else:
                mem[i][0] = 1 if text2[0] == text1[i] else 0
        for j in range(1, len(text2)):
            if mem[0][j - 1] == 1:
                mem[0][j] = 1
            else:
                mem[0][j] = 1 if text1[0] == text2[j] else 0
        # recursive
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    mem[i][j] = mem[i - 1][j - 1] + 1
                else:
                    mem[i][j] = max(mem[i - 1][j], mem[i][j - 1])

        return mem[len(text1) - 1][len(text2) - 1]
