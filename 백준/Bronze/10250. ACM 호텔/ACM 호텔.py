import sys
#sys.stdin.readline()이 빠른 이유는 입력 후 엔터까지 포함하여 한 번에 읽어들이기 때문입니다.

results = []

# 첫 번째 줄에서 테스트 케이스의 개수 T를 입력받습니다.
T = int(sys.stdin.readline())

# T번 만큼 반복합니다.
for _ in range(T):
    # 각 테스트 케이스마다 필요한 입력을 받습니다.
    # 예: 띄어쓰기로 구분된 세 숫자 입력
    H, W, N = map(int, sys.stdin.readline().split())
    # 여기서 H는 호텔의 층 수, W는 각 층의 방 수, N은 손님의 번호입니다.

    if N % H != 0:
        X = str(N % H)
        Y = str((N // H) + 1).zfill(2)
        results.append(X + Y)
    else:
        X = str(H)
        Y = str(N // H).zfill(2)
        results.append(X + Y)
    # .zfill(2)는 두 자리 수로 맞추기 위해 앞에 0을 채워줍니다.
    # 예: 1 -> '01', 9 -> '09', 10 -> '10'

print('\n'.join(results))