# https://leetcode.com/problems/generate-parentheses/

# Sol 1 - Backtracking

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # init answer arr 
        # left count < n --> add (
        # left count > right count --> add ) 
        # valid IIF n == right count == left count 

        answer = []

        def backtracking(cur_string, left_count, right_count):
            if n == left_count == right_count:
                answer.append("".join(cur_string))
            
            if left_count < n:
                cur_string.append("(")
                backtracking(cur_string, left_count + 1, right_count)
                cur_string.pop()
            
            if left_count > right_count:
                cur_string.append(")")
                backtracking(cur_string, left_count, right_count + 1)
                cur_string.pop()
            
        backtracking([], 0, 0)
        return answer