class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ans = 0
        oper = {'+','-','/','*'}

        for c in tokens:
            if c in oper:
                x = stack.pop()
                # print(stack[-1] + c + x)
                curr_ans = eval(stack[-1] + c + x)
                if curr_ans > 0:
                    curr_ans = floor(curr_ans)
                else:
                    curr_ans = ceil(curr_ans)
                # print(curr_ans)
                stack[-1] = str(curr_ans)
            else:
                stack.append(c)

        return int(stack[-1])