# Create a stack to store unused number
# Iterate through the input and push the number on the stack
# pop two nums for stack if seeing and operator
# runtime : O(n) space: O(n)
# https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in operators:
                n2 = stack.pop()
                n1 = stack.pop()

                if token == "+":
                    stack.append(n1 + n2)
                elif token == "-":
                    stack.append(n1 - n2)
                elif token == "*":
                    stack.append(n1 * n2)
                else:
                    stack.append(int(n1 / n2))

            else:
                stack.append(int(token))

        return stack.pop()
