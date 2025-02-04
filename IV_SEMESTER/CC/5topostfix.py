def precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '^':
        return 3
    return -1

def infixToPostfix(expression):
    result = []
    stack = []

    for c in expression:
        if c.isalnum():
            result.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack and stack[-1] != '(':
                return "Invalid Expression"
            else:
                stack.pop()
        else:
            while stack and precedence(c) <= precedence(stack[-1]):
                if stack[-1] == '(':
                    return "Invalid Expression"
                result.append(stack.pop())
            stack.append(c)

    while stack:
        if stack[-1] == '(':
            return "Invalid Expression"
        result.append(stack.pop())

    return ''.join(result)

expr = "A*(B+C)/D"
print("Infix Expression:", expr)
print("Postfix Expression:", infixToPostfix(expr))
