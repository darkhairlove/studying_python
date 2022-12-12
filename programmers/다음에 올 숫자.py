def solution(com):
    answer = 0
    som = 0
    ans = len(com)-1
    if com[1]-com[0] == com[2]-com[1]:
        som += com[1]-com[0]
        answer = com[ans]+som
    elif com[1]//com[0] == com[2]//com[1]:
        som += com[1]//com[0]
        answer = com[ans]*som
    return answer
