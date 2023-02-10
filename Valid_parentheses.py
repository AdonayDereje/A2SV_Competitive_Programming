class Solution:
    def isValid(self, s):
        parentheses = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        if len(s)  == 0:
            return True
        if len(s) == 1:
            return False
        stack = []
        for index in s:
            if parentheses.get(index):
                stack.append(index)
            else: 
                try:
                    last_left_bracket = stack.pop()
                    correspond_bracket = parentheses.get(last_left_bracket)
                    if index != correspond_bracket:
                        return False
                except:
                    return False
        return len(stack) == 0
