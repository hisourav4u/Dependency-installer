def solution(A):
    word_dict={}

    for i in range(len(A)):
        word="".join(sorted(A[i]))
        if word in word_dict:
            word_dict[word].append(i+1)
        else:
            word_dict[word]=[i+1]
    return word_dict.values()


words=list(input().split())
print(list(solution(tuple(words))))
