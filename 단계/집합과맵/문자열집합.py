'''
문자열집합
14425번

첫째 줄에 문자열의 개수 N과 M
(1 <= N <= 10,000, 1 <= M <= 10,000)
다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.
다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0

s = set()
for i in range(n):
    s.add(input().strip())  # 줄바꿈 문자를 제거해야 함

for j in range(m):
    if input().strip() in s:  # 줄바꿈 문자를 제거해야 함
        answer += 1

print(answer)
