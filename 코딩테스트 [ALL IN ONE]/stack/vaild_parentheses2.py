# [')', '}', ']']
# ')', '}', ']' 같은 문자가 들어왔을 때 pop() 후 stack len 반환

def is_valid(s):
    stack = []
    for p in s:
        if p == '(':
            stack.append(")")
        elif p == '{':
            stack.append("}")
        elif p == '[':
            stack.append("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack


print(is_valid(")(){}"))
