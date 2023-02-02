def solution(arrayA, arrayB):
    a, b = get_GCD(arrayA), get_GCD(arrayB)
    
    for i in arrayA:
        if i % b == 0:
            b = 0
            break
    for i in arrayB:
        if i % a == 0:
            a = 0
            break
    
    return max(a,b)

def GCD(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def get_GCD(arr):
    a = arr[0]
    for i in arr:
        a = GCD(a,i)
    return a
    