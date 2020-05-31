def solution(A):

    opening="+-*/("
    closing=")"
    store=[]

    for op in A:
        if op in opening:
            store.append(op)

        elif op in closing:
            if store.pop()=="(":
                return 1
            store.pop()

    return 0

print(solution(input()))
