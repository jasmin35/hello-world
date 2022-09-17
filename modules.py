import sys

lines = sys.stdin.readlines()

from string import ascii_lowercase

# 여러 줄(정해진 개수 X)에 줄마다 여러 숫자 주어질 경우 :
    # lines를 일단 다 저장하고 
    # line 별로 map으로 숫자 끊어 저장. 

# int(input()) : string으로 들어온 한 숫자를 int형으로 변환. 
# int(sys.stdin.readline()) :  string으로 들어온 한 숫자를 int형으로 변환. (속도 향상)

# map(int,input().split()) : string으로 들어온 여러 개의 숫자를 각각 int형으로 변환 후 각 변수에 저장. 
# map(int,sys.stdin.readline().split()) : string으로 들어온 여러 개의 숫자를 각각 int형으로 변환. (속도 향상) 후 각 변수에 저장. 
# list(map(int,sys.stdin.readline().split())) : string으로 들어온 여러 개의 숫자를 각각 int형으로 변환. (속도 향상) 후 하나의 리스트에 저장

# 여러 줄(정해진 개수 O)에 줄마다 여러 숫자 주어질 경우.
# 어떤 부분이 반복되는가 공통 부분 제대로 알아차리기. 

# 시간 단축해야 하는 문제 ) import sys 통해 sys.stdin.readline() 사용

# for i in range(n) 내부에서 i 응용 출력 형태 주의. 범위의 경계 체크. 

# 한 줄에 여러 숫자가 주어지는 경우:
    # map으로 일단 끊어 받고 list로 저장

# 예약어 변수명으로 쓰지 않도록 주의. 

# append와 extend의 차이

# key로 value 불러오기 : a[key]
# value로 key 불러오기 : 

# key 모두 불러오기 : a.keys()
# values 모두 불러오기 : a.values()
# key-value 모두 불러오기 : a.items()

# for a in dictionary: key 접근

# dict['a']=1 : a 키 원래 있었으면 변경, 없었으면 추가. 
# dict.update(a=1) : a 키 원래 있었으면 변경, 없었으면 추가. 
# dict.update()는 여러 키-값 쌍을 한 번에 콤마를 이용해 다루기 가능. 

# math.ceil
# math.floor

# min(iterable)


# list.count(타겟)

# 문자열-정수 대응
    # 연속 & 0부터 시작 : list이용. index 활용
    # 불연속, 랜덤 : 딕셔너리 이용