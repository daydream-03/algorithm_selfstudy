자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

```python
def solution(n):
    answer = []
    n = list(str(n))[::-1]
    for i in n:
        answer.append(int(i))
    return answer
```

List Comprehension을 이용한 문제풀이
```python
def solution(n):
    answer = [int(i) for i in str(n)][::-1]
    return answer
```

map 함수를 이용한 문제풀이
```python
def solution(n):
    return list(map(int, reversed(str(n))))
```
map(func, *iterables)
