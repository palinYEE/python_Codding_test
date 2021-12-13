# '''
#  - 00시00분00초 ~ N시 59분 59초 까지의 모든 수 중 3이 하나라도 포함되는 경우의 수를 출력
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
    print("@ - 문제 이름 : 시각         @") 
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

def sol():
    count = 0
    N = int(input("[*] N 값을 입력하세요. : "))

    for i in range(0, N + 1): 
        for j in range(0, 60):
            for k in range(0, 60):
                if '3' in f"{i}{j}{k}":
                    count += 1
    print(f"[*] 경우의 수 : {count}")

if __name__ == "__main__":
    solv_info()
    sol()