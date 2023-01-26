def solution(dartResult):
    answer = 0
    dart = dartResult.replace("10","X")
    score = [ str(i) for i in range(9)]
    bonus = {"S":1, "D":2, "T":3}
    stack = []

    for i in dart:
        if i.isdigit() or i == "X":
            stack.append(10 if i =="X" else int(i))   
            
        elif i in bonus.keys():
            num = stack.pop()
            stack.append(num ** bonus[i])           
    
        elif i == "#":
            stack[-1] *= -1
        elif i == "*":
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(num * 2)   
    return sum(stack)