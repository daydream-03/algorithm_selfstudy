n, m = map(int, input().split())

cnt = [0] * (n + m + 1)
tmp = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > tmp:
        tmp = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == tmp:
        print(i, end=" ")

# 딕셔너리를 이용한 풀이
my_dict = {}
for i in range(1, n + 1):
    for j in range(1, m + 1):
        tmp = i + j
        if tmp not in my_dict.keys():
            my_dict[tmp] = 1
        my_dict[tmp] += 1

max_value = max(my_dict.values())
for key, value in my_dict.items():
    if value == max_value:
        print(key, end=" ")
