from bs4 import BeautifulSoup
import datetime
import webreader
import numpy as np


def get_3year_treasury():
    url = "http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=288401&amp;idx_cd=2884&amp;freq=Y&amp;period=1998:2016"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    td_data = soup.select("tr td")

    treasury_3year = {}
    start_year = 1998

    for x in td_data:
        treasury_3year[start_year] = x.text
        start_year += 1

    print(treasury_3year)
    return treasury_3year


def get_dividend_yield(code):
    url = "http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=" + code
    html = requests.get(url).text

    search = re_enc.search(html)
    if search is None:
        return {}

    encparam = re_enc.search(html).group(1)
    encid = re_id.search(html).group(1)

    soup = BeautifulSoup(html, 'html5lib')
    dt_data = soup.select("td dl dt")

    dividend_yield = dt_data[-2].text
    dividend_yield = dividend_yield.split(' ')[1]
    dividend_yield = dividend_yield[:-1]

    return dividend_yield


def get_estimated_dividend_yield(code):
    dividend_yield = get_financial_statements(code)
    if len(dividend_yield) == 0:
        return "0"

    dividend_yield = sorted(dividend_yield.items())[-1]
    return dividend_yield[1]


def get_previous_dividend_yield(code):
    dividend_yield = get_financial_statements(code)

    now = datetime.datetime.now()
    cur_year = now.year

    previous_dividend_yield = {}

    for year in range(cur_year-5, cur_year):
        if str(year) in dividend_yield.index:
            previous_dividend_yield[year] = dividend_yield[str(year)]

    return previous_dividend_yield


def calculate_estimated_dividend_to_treasury(self, code):
    estimated_dividend_yield = webreader.get_estimated_dividend_yield(code)

    if estimated_dividend_yield == 0:
        estimated_dividend_yield = webreader.get_dividend_yield(code)

        if estimated_dividend_yield == "":
            estimated_dividend_yield = 0


def get_min_max_dividend_to_treasury(self, code):
    previous_dividend_yield = webreader.get_previous_dividend_yield(code)
    three_years_treasury = webreader.get_3year_treasury()

    now = datetime.datetime.now()
    cur_year = now.year
    previous_dividend_to_treasury = {}

    for year in range(cur_year-5, cur_year):
        if year in previous_dividend_yield.keys() and year in three_years_treasury.keys():
            ratio = float(previous_dividend_yield[year]) / float(three_years_treasury[year])
            previous_dividend_to_treasury[year] = ratio

    print(previous_dividend_to_treasury)
    min_ratio = min(previous_dividend_to_treasury.values())
    max_ratio = max(previous_dividend_to_treasury.values())

    return min_ratio, max_ratio


def buy_check_by_dividend_algorithm(self, code):
    estimated_dividend_to_treasury = self.calculate_estimated_dividend_to_treasury(code)
    (min_ratio, max_ratio) = self.get_min_max_dividend_to_treasury(code)

    if estimated_dividend_to_treasury >= max_ratio and max_ratio != 0:
        return 1, estimated_dividend_to_treasury
    else:
        return 0, estimated_dividend_to_treasury


def run_dividend(self):
    buy_list = []

    for code in self.kospi_codes[0:50]:
        time.sleep(0.5)
        ret = self.buy_check_by_dividend_algorithm(code)
        if ret[0] == 1:
            buy_list.append((code, ret[1]))

    sorted_list = sorted(buy_list, key=lambda t:t[1], reverse=True)
    print(sorted_list)

    buy_list = []
    for i in range(0, 5):
        code = sorted_list[i][0]
        buy_list.append(code)

    self.update_buy_list(buy_list)
