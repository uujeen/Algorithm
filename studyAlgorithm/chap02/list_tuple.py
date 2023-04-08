# list 와 tuple / 뮤터블과 이뮤터블

# list
""" 
뮤터블 자료형
리스트 원소의 개수는 리스트를 만들기 전에 반드시 결정해야 한다.
"""
list01 = [] # [] 빈 리스트
list02 = [1, 2, 3] # [1, 2, 3]
list03 = ['A', 'B', 'C', ] # ['A', 'B', 'C']와 동일
list04 = list() # [] 빈리스트
list05 = list('ABC') # ['A', 'B', 'C'] 문자열의 각 문자로부터 원소를 생성
list06 = list([1, 2, 3]) # 리스트로부터 원소를 생성
list07 = list((1, 2, 3)) # 튜플로부터 원소를 생성
list08 = list({1, 2, 3}) # 집합으로부터 원소를 생성
list09 = list(range(3)) # [1, 2, 3]
list10 = list(range(3,5)) # [3, 4]
list11 = list(range(2,5,2)) # [2, 4] 
list12 = [None] * 5 # [None, None, None, None, None]

# tuple
"""
튜플은 리스트와 다르게 원소를 변경할 수 없는 이뮤터블 자료형
"""
tuple01 = ()
tuple02 = 1,
tuple03 = (1,)
tuple04 = 1, 2, 3
tuple05 = 1, 2, 3,
tuple06 = (1, 2, 3)
tuple07 = 'A', 'B', 'C'
tuple08 = tuple()
tuple09 = tuple('ABC') # ('A', 'B', 'C') 문자열의 각 문자로부터 원소를 생성
tuple10 = tuple([1, 2, 3]) # (1, 2, 3) 리스트로부터 원소를 생성
tuple11 = tuple({1, 2, 3}) # (1, 2, 3) 집합으로부터 원소를 생성
tuple12 = tuple(range(3)) # [1, 2, 3]
tuple13 = tuple(range(3,5)) # [3, 4]
tuple14 = tuple(range(2,5,2)) # [2, 4]

a, b, c = tuple04 # or list02 a = 1, b = 2, c = 3

s = [11, 22, 33, 44, 55 ,66 ,77]
s[0:6] # 11, 22, 33 ,44 ,55 ,66 0부터 5까지 출력
s[0:7:2] # 11, 33, 55, 77 0부터 6까지 인덱스를 2씩 증가시키며 출력
s[::-1] # 리스트의 맨 끝부터 차례대로 출력

x = 6
y = 2
x, y = y+2, x+3 # x = 4, y = 9 x가 변경된 후 y가 변경되는 것이 아닌 동시에 이루어진다


[1, 2, 3] == [1, 2, 3] 
[1, 2, 5] < [1, 3, 4] # 원소의 값을 인덱스 순서로 비교하다가 한 개의 원소가 더 클 경우 배열이 더 크다고 판단
[1, 2, 3] < [1, 2, 3, 5] < [1, 2, 3, 5, 6] # 두 배열의 원소의 개수가 다를 경우 큰 배열이 더 크다고 판단