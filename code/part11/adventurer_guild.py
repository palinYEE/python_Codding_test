import sys
from typing import Match 

SOLV_DATE = sys.argv[1]
prob = '''
 =========================================================
 [문제]
 한 마을에 모험가가 N명 존재. 모험가 길드에서는 Nㅂ명의 모험가를 대상으로 공포도를 측정했는데. 이게 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어진다. 
 모험가 길드장은 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 떠날수 있도록 규정하였다. 
 동빈이는 최대 몇개의 모험가 그룹을 만들 수 있는지 궁금함. 
 동빈이를 위해 N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오. 
 =========================================================
 [조건]
 * 입력 조건 : 
    - 첫째 줄에 모험가 수 N이 주어진다 (1 <= N <= 100,000)
    - 둘째 줄에 각 모험가의 공보도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분한다. 
 * 출력 조건 : 여행을 떠날 수 있는 그룹 수의 최댓값을 출력
 =========================================================
 [예시]
 - 입력 예시 : 
    5
    2 3 1 2 2
 - 출력 예시 : 
    2
 =========================================================
'''

def solv_info():
    author = 'yyj'

    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(" @                            @") 
    print(" @       PYTHON PRACTICE      @")
    print(" @                            @") 
    print(f" @ - 푼 날짜 : {SOLV_DATE}     @")
    print(f" @ - 저자 : {author}               @")
    print(" @ - 문제 이름 : 왕실의 나이트@") 
    print(" @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(f"{prob}")

def sol():
    N = int(input())
    scare_list = list(map(int, input().split()))
    scare_list.sort()
    count = 0
    result = 0
    for i in scare_list:
        count += 1
        if count >= i:
            result += 1
            count = 0
    return result

if __name__ == "__main__":
    solv_info()
    result = sol()
    print(f"     - result : {result}")