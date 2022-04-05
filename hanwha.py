
import csv
from collections import defaultdict, deque
import datetime


def date_sort(data_name_list):
    dates = [[datetime.datetime.strptime(date, "%m/%d/%Y"), name] for date, name in data_name_list]
    dates.sort()
    # str(i[0]).replace(' 00:00:00', '')
    result = [[str(date).replace(' 00:00:00', ''), name] for date, name in dates]
    return result


Price_Dict = defaultdict(list)  # defaultdict에 list 선언
Enterprise_list = ['AAPL', 'AMD', 'AMZN', 'CSCO', 'Facebook, Inc', 'MSFT', 'QCOM', 'SBUX', 'TSLA', 'ZNGA']
for Enterprise in Enterprise_list:

    with open(Enterprise + '.csv', 'r', encoding='utf-8')as f:  # csv file open with read
        data = csv.reader(f)  # csv file reader
        for price_momentum in list(data)[1:]:  # 0번째 데이터는 설명임으로 스킵
            Price_Dict[float(price_momentum[1][1:])].append(
                [price_momentum[0], Enterprise])  # float을 해준 이유는 정렬할때 숫자로 정렬하기 위해서이며 날짜를 계속 추가해준다.
    closing_price_key = list(Price_Dict.keys())  # Key를 $~~.~~로 설정했기 때문에 이를 list 형태로 변환
    closing_price_key.sort(reverse=True)  # list로 변환된 float 형태의 123.12, ... 를 정렬

with open('all_2_a.csv', 'w', encoding='utf-8')as f:  # csv file open with write
    csv_fp = csv.writer(f)
    csv_fp.writerow(['Date', 'Name', 'Price'])  # 정렬된 데이터를 write
    for price_key in closing_price_key:  # 정렬된 Key를 뽑음
        if len(Price_Dict[price_key]) > 1:
            print(price_key, len(Price_Dict[price_key]), sep=' / ')  # 금액이 중복된 경우 출력해 날짜 정렬이 잘 되어있는지 확인
        sort_data = date_sort(Price_Dict[price_key])  # 중복된 금액이 있는 경우 날짜 정렬
        for data in sort_data:
            csv_fp.writerow(data + [price_key])  # 정렬된 데이터를 write
        # for data, name in Price_Dict[price_key]:

# csv library 관련 : http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
# collection 관련 : https://docs.python.org/ko/3/library/collections.html#collections.defaultdict


# 2-b
import numpy as np
import csv
from collections import defaultdict, deque
import datetime

#momentum -> https://comdoc.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AA%A8%EB%A9%98%ED%85%80momentum

def momentum(list_, day):
    i = 0
    result = list_[:-day]
    while i < len(list_)-day:
        result[i][1] = float(list_[i][1][1:]) - float(list_[i+day][1][1:])
        i+=1
    return result

def date_sort(data_name_list):
    dates = [[datetime.datetime.strptime(date, "%m/%d/%Y"),name] for date, name in data_name_list]
    dates.sort()
    result = [[str(date).replace(' 00:00:00', ''), name] for date, name in dates]
    return result

Price_Dict = defaultdict(list) #defaultdict에 list 선언

Enterprise_list = ['AAPL', 'AMD', 'AMZN', 'CSCO', 'Facebook, Inc', 'MSFT', 'QCOM', 'SBUX', 'TSLA', 'ZNGA']
for Enterprise in Enterprise_list:
    with open(Enterprise+'.csv', 'r', encoding='utf-8')as f: #csv file open with read
        data = csv.reader(f) #csv file reader
        for price_momentum in momentum(list(data)[1:], 10): #0번째 데이터는 설명임으로 스킵
            Price_Dict[price_momentum[1]].append([price_momentum[0], Enterprise]) #float을 해준 이유는 정렬할때 숫자로 정렬하기 위해서이며 날짜를 계속 추가해준다.
    closing_price_key = list(Price_Dict.keys()) #Key를 $~~.~~로 설정했기 때문에 이를 list 형태로 변환
    closing_price_key.sort(reverse=True) #list로 변환된 float 형태의 123.12, ... 를 정렬
with open('all_momentum.csv', 'w', encoding='utf-8')as f: #csv file open with write
    csv_fp = csv.writer(f)
    csv_fp.writerow(['Date', 'Name', 'Momentum']) #정렬된 데이터를 write
    for price_key in closing_price_key: #정렬된 Key를 뽑음
        if len(Price_Dict[price_key]) > 1:
            print(price_key,len(Price_Dict[price_key]), sep=' / ') #금액이 중복된 경우 출력해 날짜 정렬이 잘 되어있는지 확인
        sort_data = date_sort(Price_Dict[price_key]) #중복된 금액이 있는 경우 날짜 정렬
        for data in sort_data:
            csv_fp.writerow(data+[price_key]) #정렬된 데이터를 write
        # for data, name in Price_Dict[price_key]:

#csv library 관련 : http://pythonstudy.xyz/python/article/207-CSV-%ED%8C%8C%EC%9D%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
#collection 관련 : https://docs.python.org/ko/3/library/collections.html#collections.defaultdict