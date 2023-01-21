def solution(board, moves):
    answer = 0
    stack = []
    for i in moves:
        for j in range(len(board)):
            doll = board[j][i-1]
        
            if doll != 0:
                stack.append(doll)
                board[j][i-1] = 0
    
                if len(stack) >= 2:
                    if stack[-2] == stack[-1]:
                        stack.pop()
                        stack.pop()
                        answer += 2
                break
    return answer