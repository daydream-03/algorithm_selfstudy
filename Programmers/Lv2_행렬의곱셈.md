2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

입출력 예
|arr1|	arr2|return|
|--|--|--|
|[[1, 4], [3, 2], [4, 1]]|	[[3, 3], [3, 3]]|	[[15, 15], [15, 15], [15, 15]]|
|[[2, 3, 2], [4, 2, 4], [3, 1, 4]]|	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]|	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]|

```python
# 내 풀이
def solution(arr1, arr2):
    calc = 0
    answer = []
    for k in range(len(arr1)):
        matrix = []
        for i in range(len(arr2[0])):
            result = 0
            for j in range(len(arr1[0])):
                calc = arr1[k][j] * arr2[j][i]
                result = result + calc
            matrix.append(result)
        answer.append(matrix)
    return answer

# 결괏값으로 리턴할 행렬을 전부 0으로 먼저 선언한 뒤 더하는 풀이방식
def solution2(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

# numpy 모듈로 간단하게 풀이도 가능하다. 공부에는 도움 안될 듯
import numpy as np

def solution3(A, B):
    return (np.matrix(A)*np.matrix(B)).tolist()

```