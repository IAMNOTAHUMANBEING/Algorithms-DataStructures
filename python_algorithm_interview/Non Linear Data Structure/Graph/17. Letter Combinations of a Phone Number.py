class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(i, path):
            # 종료 조건
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 마다 탐색을 반복하며 path에 추가
            for j in dic[digits[i]]:
                dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")
        
        return result

