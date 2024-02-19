class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = {'+','-','/','*'}

        for c in tokens:
            if c in oper:
                x = stack.pop()
                curr_ans = eval(stack[-1] + c + x)
                if curr_ans > 0:
                    stack[-1] = str(floor(curr_ans))
                else:
                    stack[-1] = str(ceil(curr_ans))
                # print(curr_ans)
                # stack[-1] = str(curr_ans)
            else:
                stack.append(c)

        return int(stack[-1])