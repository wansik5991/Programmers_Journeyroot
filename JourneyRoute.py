import os
os.system('cls')

from collections import defaultdict

def solution(tickets):

    tickets = sorted(tickets, key = lambda x : x[1])
    
    ticket = defaultdict(list)

    for from_, to_ in tickets :
        ticket[from_].append([to_, 1])

    flag = 0
    answer = []
    def dfs(airport, cnt, path) :
        nonlocal flag
        if flag == 1 :
            return

        elif cnt == len(tickets):
            flag = 1
            answer.append(path.split(' '))
            return

        for i in range(len(ticket[airport])) :
            destination = ticket[airport][i][0]
            check = ticket[airport][i][1]
            if check == 1 :

                ticket[airport][i][1] = 0
                dfs(destination, cnt+1, path + " " + destination)
                ticket[airport][i][1] = 1

    dfs('ICN', 0, 'ICN')
    
    return answer[0]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))