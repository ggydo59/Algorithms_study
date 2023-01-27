def solution(n, m):
    big, small = max(n, m), min(n,m)
    while small != 0:
        big, small = small, big % small
    return [big, n*m / big]