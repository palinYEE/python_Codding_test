# -*- coding: utf-8 -*- 

prob = '''
=============================================================================================
Date : 2021.12.04 토요일
Author : Yoon yeoung jin

문제 : 
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑은 게임이다. 단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다. 
    1. 숫자가 쓰인 카드들이 N x M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다. 
    2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다. 
    3. 그 다음 선택된 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다. 
카드들이 N x M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오. 

입력 조건 : 
 - 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다 (1 <= N, M <= 100)
 - 둘쟤 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000 이하의 자연수 이다. 

출력 조건 : 
 - 첫째 줄에서 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다. 

입력 예시 1 :                                     출력 예시 :  
3 3                                             2
3 1 2
4 1 4
2 2 2

입력 예시 2 :                                     출력 예시 :  
2 4                                             3
7 3 1 8
3 3 3 4
=============================================================================================
'''
def showProblem():
    print(prob)

# Find minimal value in list 
def findMinimalNumber(value):
    minimal = int(value[0])
    for v in value[1:]:
        if minimal > int(v):
            minimal = int(v)
    return minimal

def sol():
    mat = []
    col, row = input().split()
    col = int(col)
    row = int(row)

    # setting Matrix
    for i in range(0, col):
        mat.append(input().split())

    result = findMinimalNumber(mat[0])
    for l in mat[1:]:
        tmp = findMinimalNumber(l)
        if result < tmp:
            result = tmp
    return result


if __name__ == '__main__':
    print("1. Show problem")
    print("2. Show answer")
    select = int(input("Select : "))
    if(select == 1):
        showProblem()
    if select == 2:
        result = sol()
        print(f"-> result : {result}")
