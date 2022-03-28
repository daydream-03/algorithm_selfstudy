어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. <br>예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. <br>문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건<br>
공백은 아무리 밀어도 공백입니다.
<br>s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
<br>s의 길이는 8000이하입니다.
n<br>은 1 이상, 25이하인 자연수입니다.

```python
def solution(s, n):
    answer = ""
    s_list = [ord(w) for w in list(s)]
    for i in s_list:
        if i == 32:
            pass
        elif i < 91 and i + n > 90:
            i = i + n - 26
        elif i < 123 and i + n > 122:  # elif i in range(97, 123)
            i = i + n - 26
        else:
            i += n
        answer += chr(i)
    return answer
```
i의 분기를 나눌 때 처음에 ```# elif i in range(97, 123)```처럼 range로 사용해 테스트 케이스를 통과했으나,
if, elif, else를 이해하고 중첩되지 않도록 적절히 분기로 나누어 코드를 작성하니 기존 대비 런타임이 3배 가량 빨라짐.