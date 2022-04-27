주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

```python
import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().split()))
cnt = 0


def check(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for number in numbers:
    if check(number):
        cnt += 1

print(cnt)
```