import sys

input = sys.stdin.readline

n = int(input())
people = set()

for i in range(n):
    name, stat = input().split()
    if stat == 'enter':
        people.add(name)  # set에 이름 추가
    if stat == 'leave':
        people.discard(name)  # set에서 이름 제거

# 남아 있는 사람을 역순으로 정렬하여 출력
answer = sorted(people, reverse=True)
print('\n'.join(answer))
