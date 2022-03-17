T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    my_list = list(map(int, input().split()))
    my_list = my_list[s - 1 : e - 1]
    my_list.sort()
    print(f"#{t+1} {my_list[k-1]}")
