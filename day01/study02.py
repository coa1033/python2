# 딕셔너리

# 문제 : 딕셔너리에 각 달의 마지막 날들을 한번에 담기
# 조건 : 1월 ~ 3월까지
# 조건 : 2월의 마지막은 28일로 함
# 조건 : 첫 데이터의 key는 "1월", value는 31일

dic = {"1월":"31일","2월":"28일","3월":"31일"}
print(dic["1월"])


# 문제 : 딕셔너리에 각 달의 마지막 날들을 반복문을 통해 담기

dic1 = {}

i = 1
while i<=12 :
    if i == 2 :
        dic1[str(i)+"월"] = 28
    elif i == 4 or i == 6 or i ==9 or i == 11 : 
        dic1[str(i)+"월"] = 30
    else :
        dic1[str(i)+"월"] = 31
    i+=1
print(dic1)

dic2 = {}

for i in range(1,13):
    month = str(i) + "월"
    endday = 31
    if i == 2 :
        endday = 28
    elif i in [4,6,9,11]:
        endday =30
    dic2[month] = endday
print(dic2)
