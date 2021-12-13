# '''
#  - 가장 왼쪽 위 좌표 : (1,1)
#  - 가장 오른쪽 위 좌표 : (N,N)
#  - 시작 좌표는 항상 (1,1) 이다. 
#  - 여행자는 상하좌우로 움직일 수 있다. 
#  - L, R, U, D
#  - NxN 정사각형을 벗어나는 움직임은 무시된다. 
# '''

def solv_info():
    solv_date = '2021.12.11'
    author = 'yyj'

    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@                            @") 
    print("@       PYTHON PRACTICE      @")
    print("@                            @") 
    print(f"@ - 푼 날짜 : {solv_date}     @")
    print(f"@ - 저자 : {author}               @")
    print("@ - 문제 이름 : 상하좌우     @") 
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# input param
#   - num : N 값 
def sol():
    N = int(input("N 값을 입력하세요. : "))
    pathList = input("이동 경로를 입력하세요. : ").split(" ")

    start = [1,1]
    for direct in pathList:
        if direct.upper() == "R":
            if start[1] + 1 <= N:
                start[1] = start[1] + 1
            else:
                print(f"[!] 정사각형에서 벗어났습니다. (R)==> {start}")
        elif direct.upper() == "L":
            if start[1] -1 > 0:
                start[1] = start[1] - 1
            else:
                print(f"[!] 정사각형에서 벗어났습니다. (L)==> {start}")
        elif direct.upper() == "D":
            if start[0] + 1 <= N:
                start[0] = start[0] + 1
            else:
                print(f"[!] 정사각형에서 벗어났습니다. (D)==> {start}")
        elif direct.upper() == "U":
            if start[0] - 1 > 0:
                start[0] = start[0] - 1
            else:
                print(f"[!] 정사각형에서 벗어났습니다. (U)==> {start}")
        else:
            print("인자를 잘못 입력하였습니다.")
            exit()
    print(f"최종 위치는 {start[0]}, {start[1]} 입니다. ")


if __name__ == '__main__':
    solv_info()
    sol()
