import heapq
T = 0
Kucha = []
heapq.heapify(Kucha)
N = int(input())
Spisokdel = []
for _ in range(N):
    t, d = (map(int, input().split()))
    Spisokdel.append((t, d))
Spisokdel.sort(key=lambda x: x[1])
for i in range(len(Spisokdel)):
    if Spisokdel[i][0]>Spisokdel[i][1]:
        continue
    if Spisokdel[i][0]<=Spisokdel[i][1]:
        heapq.heappush(Kucha, -Spisokdel[i][0])
        T += Spisokdel[i][0]
        if T>Spisokdel[i][1]:
            koren = heapq.heappop(Kucha)
            T += koren
        elif T<=Spisokdel[i][1]:
            continue
print(len(Kucha))