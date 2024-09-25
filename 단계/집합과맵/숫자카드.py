'''
숫자카드
10815번

숫자카드는 정수 하나가 적혀져 있는 카드
숫자 카드 N개 가지고 있다. 정수 M개가 주어졌을때,
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 구하라

첫째줄 N(1 <= N <= 500,000)
둘째줄 숫자카드에 적혀있는 정수 (-10,000,000 <= M <= 10,000,000)

첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자를 가지면
1, 아니면 0

ex)
5 <- N
6 3 2 10 -10
8 <- M
10 9 -5 2 3 4 5 -10
'''
import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
checks = list(map(int, sys.stdin.readline().split()))

_dict = {}

for i in range(len(card)):
    _dict[card[i]] = 0
#dictionary에 삽입
    
for j in range(m):
    if checks[j] not in _dict:
        print(0,end=' ')
    else:
        print(1,end=' ')
        
#list 내의 in 시간복잡도 O(n)
#set, dict, dict.keys -> O(1)