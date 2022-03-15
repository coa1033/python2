# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, 수작업으로 순회출력
# 조건 : 1월부터 3월까지만 담고 출력해주세요

dic = {}

dic["1월"] = 31
dic["2월"] = 28
dic["3월"] = 31

print(dic["1월"])
print(dic["2월"])
print(dic["3월"])


# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담고, keys()로 key 순회출력

dic1 = {}
dic1_list = [31,28,31,30,31,30,31,31,30,31,30,31]
for i , j in enumerate(dic1_list):
    month = str(i+1) + "월"
    dic1[month] = j
    print(month)
