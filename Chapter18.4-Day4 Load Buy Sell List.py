def load_buy_sell_list(self):
    f = open("buy_list.txt", 'rt')
    buy_list = f.readlines()
    f.close()

    f=open("sell_list.txt", 'rt')
    sell_list = f.readlines()
    f.close()

    row_count = len(buy_list) + len(sell_list)
    self.tableWidget_4.setRowCount(row_count)

    #buy list
    for j in range(len(buy_list)):
        row_data = buy_list[j]
        split_row_data = row_data.split(';')
        split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rsplit())

        for i in range(len(split_row_data)):
            item = QTableWidgetItem(split_row_data[i].rstrip())
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tableWidget_4.setItem(j, i, item)

    #sell list
    for j in range(len(sell_list)):
        row_data = sell_list[j]
        split_row_data = row_data.split(';')
        split_row_data[1] = self.kiwoom.get_master_code_name(split_row_data[1].rstrip())

        for i in range(len(split_row_data)):
            item = QTableWidgetItem(split_row_data[i].rstrip())
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignCenter)
            self.tableWidget_4.setItem(len(buy_list) + j, i, item)

    self.tableWidget_4.resizeRowsToContents()
