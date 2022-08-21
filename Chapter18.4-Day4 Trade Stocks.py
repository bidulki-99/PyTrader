def trade_stocks(self):
    hoga_lookup = {'지정가': "00", '시장가': "03"}

    f = open("buy_list.txt", 'rt')
    buy_list = f.readlines()
    f.close()

    f = open("sell_list.txt", 'rt')
    sell_list = f.readlines()
    f.close()

    #account
    account = self.comboBox.currentText()

    #buy list
    for row_data in buy_list:
        split_row_data = row_data.split(';')
        hoga = split_row_data[2]
        code = split_row_data[1]
        num = split_row_data[3]
        price = split_row_data[4]

        if split_row_data[-1].rstrip() == '매수전':
            self.kiwoom.send_order("send_order_req", "0101", account, 1, code, num, price, hoga_lookup[hoga], "")

    #sell list
    for row_data in sell_list:
        split_row_data = row_data.split(';')
        hoga = split_row_data[2]
        code = split_row_data[1]
        num = split_row_data[3]
        price = split_row_data[4]

        if split_row_data[-1].rstrip() == '매도전':
            self.kiwoom.send_order("send_order_req", "0101", account, 2, code, num, price, hoga_lookup[hoga], "")

    #buy list
    for i, row_data in enumerate(buy_list):
        buy_list[i] = buy_list[i].replace("매수전", "주문완료")

    #file update
    f = open("buy_list.txt", 'wt')
    for row_data in buy_list:
        f.write(row_data)
    f.close()

    #sell list
    for i, row_data in enumerate(sell_list):
        sell_list[i] = sell_list[i].replace("매도전", "주문완료")

    #file update
    f = open("sell_list.txt", 'wt')
    for row_data in sell_list:
        f.write(row_data)
    f.close()
