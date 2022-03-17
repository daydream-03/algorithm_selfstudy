n, k = map(int, input().split())
my_list = list(map(int, input().split()))

res = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(my_list[i] + my_list[j] + my_list[m])  # 리스트는 append, set은 add
res = list(res)
res.sort(reverse=True)
print(res[k - 1])
