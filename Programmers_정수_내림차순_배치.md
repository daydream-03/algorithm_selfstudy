함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

```python
def solution(n):
    n = list(str(int(n)))
    n.sort(reverse=True)
    return int("".join(n))
```

접근방법
1. list에 담긴 str 타입 데이터도 sort가 가능하다 (alphabetical order)
2. 알파벳 역순으로 정렬한 뒤
3. list내 요소를 하나의 문자열로 묶어(join()), int로 변환한다
