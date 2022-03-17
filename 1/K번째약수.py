# 내 풀이
n, k = map(int, input().split())
my_list = []

for i in range(1, n + 1):
    if n % i == 0:
        my_list.append(i)

try:
    if my_list[k - 1]:
        print(my_list[k - 1])
except:
    print(-1)

# 모범답안
n, k = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)
