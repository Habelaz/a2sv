class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            if op == 'C':
                stack.pop()
            if op == 'D':
                stack.append(2*stack[-1])
            if op.isdigit():
                stack.append(int(op))
            if op[0] == "-":
                op = op[1:]
                stack.append(-1*int(op))
                
        return sum(stack)