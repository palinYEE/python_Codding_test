import sys
from pprint import pprint

SULV_DATE = sys.argv[1]

prob = '''
[문제]
 캐릭터 크기 : 1 x 1
 장소 크기 : N x M
 각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중 한 곳을 바라본다. 
 캐일터의 움직임을 설정하기 위해 정해 놓은 메뉴얼은 다음과 같다. 
 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향) 부터 차례대로 갈 곳을 정한다. 
 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 간이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행핟고 1단계로 돌아간다. 
 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸의 경우에는, 바라보는 방향으 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다. 
 ========================================================================================
[입력 조건]
 * 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3 <= N, M <= 50)
 * 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다. 방향 d값으로는 다음과 같이 4가지가 존재한다. 
    - 0: 북쪽
    - 1: 동쪽
    - 2: 남쪽
    - 3: 서쪽
 * 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 붕쪽부터 남쪽 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외각은 항상 바다로 되어있다. 
    - 0: 육지
    - 1: 바다
 * 처음에 게임 케릭터가 위치한 칸의 상태는 항상 육지이다. 
[출력 조건]
 * 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
 ========================================================================================
[입력 예시]
 4 4        # 4 x 4 맵 생성
 1 1 0      # (1,1)에 북쪽(0)을 바라보고 서 있는 케릭터
 1 1 1 1    # 첫 줄은 모두 바다
 1 0 0 1    # 둘쨰 줄은 바다/육지/육지/바다
 1 1 0 1    # 셋째 줄은 바다/바다/육지/바다
 1 1 1 1    # 넷쨰 줄은 모두 바다
[출력 예시]
 3
 ========================================================================================
'''

def solv_info():
    author = 'yyj'

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@                            @") 
    print("@       PYTHON PRACTICE      @")
    print("@                            @") 
    print(f"@ - 푼 날짜 : {SULV_DATE}     @")
    print(f"@ - 저자 : {author}               @")
    print("@ - 문제 이름 : 게임개발     @") 
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(prob)

def prob_info(map_col, map_row, user_info, g_map):
    print("="*10)
    print(f"[*] map size : ({map_col}, {map_row}) ")
    print(f"[*] user information : {user_info}")
    print(f"[*] map : ")
    for m in g_map:
        print(m)

def sol():
    col, row = input().split()
    user_info = input()
    g_map = []
    for _ in range(0,int(row)):
        g_map.append(input().split())
    prob_info(col, row, user_info, g_map)

class book_sol:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.d = [[0] * self.m for _ in range(self.n)]
        self.x, self.y, self.direction = map(int, input().split())
        self.d[self.x][self.y] = 1

        self.array = []
        for i in range(self.n):
            self.array.append(list(map(int, input().split())))
        self.dx = [-1, 0, 1, 0]
        self.dy = [0, 1, 0, -1]

    def turn_left(self):
        self.direction -= 1
        if self.direction == -1:
            self.direction = 3
    
    def result(self):
        count = 1
        turn_time = 0

        while True:
            self.turn_left()
            nx = self.x + self.dx[self.direction]
            ny = self.y + self.dy[self.direction]

            if self.d[nx][ny] == 0 and self.array[nx][ny] == 0:
                self.d[nx][ny] = 1
                self.x = nx
                self.y = ny
                count += 1
                turn_time = 0
                continue
            else:
                turn_time += 1
            
            if turn_time == 4:
                nx = self.x - self.dx[self.direction]
                ny = self.y - self.dy[self.direction]

                if self.array[nx][ny] == 0:
                    self.x = nx
                    self.y = ny
                else:
                    break
                turn_time = 0
        return count


if __name__ == '__main__':
    solv_info()
    sol()
    print("========================")
    print("[*] book solution : ")
    book = book_sol()
    print(f"     - result : {book.result()}")
