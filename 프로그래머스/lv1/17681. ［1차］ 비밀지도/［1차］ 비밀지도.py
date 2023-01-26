def convert(num,n):
    answer = ''
    while num >= 1:        
        num, r = num // 2, num % 2
        answer += str(r)
        
    while len(answer) < n:
        answer += "0"
    return answer[::-1]

def solution(n, arr1, arr2):
    answer = [''] * n
    i = 0
    while i < n:
        temp1, temp2 = convert(arr1[i], n), convert(arr2[i], n)
        j = 0
        while j < n:
            if temp1[j] == "1" or temp2[j] == "1":
                answer[i] += '#'
            elif temp1[j] == "0" and temp2[j] == "0":
                answer[i] += ' '
            j += 1
        i += 1

    return answer