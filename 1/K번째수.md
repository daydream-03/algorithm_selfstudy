N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하세요.
```python
T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    my_list = list(map(int, input().split()))
    my_list = my_list[s - 1 : e - 1]
    my_list.sort()
    print(f"#{t+1} {my_list[k-1]}")
```
