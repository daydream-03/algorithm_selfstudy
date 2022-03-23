2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

```python
# 재귀함수
def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


def solution(n):
    return fibonacci(n)


# a, b = b, a
def solution(n):
    n1, n2 = 0, 1
    for i in range(n):
        n1, n2 = n2, n1 + n2
    return n1 % 1234567


# 리스트를 이용한 풀이
def solution(num):
    answer = [0, 1]
    for i in range(2, num + 1):
        answer.append((answer[i - 1] + answer[i - 2]) % 1234567)
    return answer[-1]
```