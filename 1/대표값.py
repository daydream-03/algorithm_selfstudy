from re import X


n = int(input())
my_list = list(map(int, input().split()))
min = 9999

avg = round(sum(my_list) / n + 0.5)  # 소수 첫째자리 반올림
for idx, x in enumerate(my_list):  # 학생번호, 성적을 모두 가져가기 위해 enumerate 사용
    tmp = abs(x - avg)  # 평균점수와의 차이를 기준점으로 잡음
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(avg, res)
