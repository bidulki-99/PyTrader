# 13.1
mystock = ['kakao', 'naver']
print(mystock[0])
print(mystock[1])

for stock in mystock:
    print(stock)

exam_dic = {'key1': 'room1', 'key2': 'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])

kakao_daily_ending_prices = [92300, 94300, 92100, 92400, 92600]

for price in kakao_daily_ending_prices:
    print(price)

kakao_daily_ending_prices = {'2016-02-19': 92600,
                             '2016-02-18': 92400,
                             '2016-02-17': 92100,
                             '2016-02-16': 94300,
                             '2016-02-15': 92300}
print(kakao_daily_ending_prices['2016-02-19'])

from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

print(kakao[0])
print(kakao[2])
print(kakao[4])

kakao2 = Series([92600, 92400, 92100, 94300, 92300], index = ['2016-02-19',
                                                            '2016-02-18',
                                                            '2016-02-17',
                                                            '2016-02-16',
                                                            '2016-02-15'])
print(kakao2)

print(kakao2['2016-02-19'])
print(kakao2['2016-02-18'])

for date in kakao2.index:
    print(date)

for ending_price in kakao2.values:
    print(ending_price)

mine   = Series([10, 20, 30], index=['naver', 'sk', 'kt'])
friend = Series([10, 30, 20], index=['kt', 'naver', 'sk'])

merge = mine + friend
print(merge)


# 13.2
raw_data = {'col0': [1, 2, 3, 4],
            'col1': [10, 20, 30, 40],
            'col2': [100, 200, 300, 400]}

data = DataFrame(raw_data)
print(data)

daeshin = {'open':  [11650, 11100, 11200, 11100, 11000],
           'high':  [12100, 11800, 11200, 11100, 11150],
           'low' :  [11600, 11050, 10900, 10950, 10900],
           'close': [11900, 11600, 11000, 11100, 11050]}

daeshin_day = DataFrame(daeshin)
print(daeshin_day)

daeshin_day = DataFrame(daeshin, columns = ['open', 'high', 'low', 'close'])

close = daeshin_day['close']
print(close)

day_data = daeshin_day.loc['16.02.24']
print(day_data)
print(type(day_data))

print(daeshin_day.columns)
print(daeshin_day.index)


# 13.3
import pandas_datareader.data as web
import datetime
start = datetime.datetime(2016, 2, 19)
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo", start, end)
print(gs)
print(gs.info())

gs = web.DataReader("078930.KS", "yahoo")
print(gs.info())

import matplotlib.pyplot as plt
plt.plot(gs['Adj Close'])
plt.show()

print(gs.index)


# 13.4
gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
print(gs.tail())

ma5 = gs['Adj Close'].rolling(window=5).mean()
type(ma5)
print(ma5.tail(10))
print(gs.tail())

print(gs['Volume'] != 0)
new_gs = gs[gs['Volume'] != 0]
print(new_gs.tail(5))

ma5 = new_gs['Adj Close'].rolling(window=5).mean()
print(ma5.tail(10))

ma5 = new_gs['Adj Close'].rolling(window=5).mean()
new_gs.insert(len(new_gs.columns), "MA5", ma5)
print(new_gs.tail(5))

ma20 = new_gs['Adj Close'].rolling(window=20).mean()
ma60 = new_gs['Adj Close'].rolling(window=60).mean()
ma120 = new_gs['Adj Close'].rolling(window=120).mean()
new_gs.insert(len(new_gs.columns), "MA20", ma20)
new_gs.insert(len(new_gs.columns), "MA60", ma60)
new_gs.insert(len(new_gs.columns), "MA120", ma120)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")

plt.legend(loc='best')
plt.grid()
plt.show()
