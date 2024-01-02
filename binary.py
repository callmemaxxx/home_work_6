def binary_search(A ,vallue):
    N = 5000
    Result = False
    first = 0
    last = N - 1
    while first <= last:
        Mid = (first + last) // 2
        if vallue == A[Mid]:
            Result = True
            Pos = Mid
            break
        elif A[Mid] < vallue:
                first = Mid + 1

        elif A[Mid] > vallue:
                last = Mid - 1

    if Result:
        return f'Element found at index {Pos}'
    else:
        return 'Element not found'
A = list(range(0,5000))
result = binary_search(A,38)
print(result)