self.pushButton_2.clicked.connect(self.check_balance)

def check_balance(self):
    self.kiwoom.reset_opw00018_output()
    account_number = self.kiwoom.get_login_info("ACCNO")
    account_number = account_number.split(';')[0]

    self.kiwoom.set_input_value("계좌번호", account_number)
    self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")

    while self.kiwoom.remained_data:
        time.sleep(0.2)
        self.kiwoom.set_input_value("계좌번호", account_number)
        self.kiwoom.comm_rq_data("opw00018_req", "opw00018", 2, "2000")

    # opw00001
    self.kiwoom.set_input_value("계좌번호", account_number)
    self.kiwoom.comm_rq_data("opw00001_req", "opw00001", 0, "2000")

    # balance
    item = QTableWidgetItem(self.kiwoom.d2_deposit)
    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
    self.tableWidget.setItem(0, 0, item)

    for i in range(1, 6):
        item = QTableWidgetItem(self.kiwoom.opw00018_output['single'][i - 1])
        item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tableWidget.setItem(0, i, item)

    self.tableWidget.resizeRowsToContents()

    # Item list
    item_count = len(self.kiwoom.opw00018_output['multi'])
    self.tableWidget_2.setRowCount(item_count)

    for j in range(item_count):
        row = self.kiwoom.opw00018_output['multi'][j]
        for i in range(len(row)):
            item = QTableWidgetItem(row[i])
            item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
            self.tableWidget_2.setItem(j, i, item)

    self.tableWidget_2.resizeRowsToContents()
    
# Timer2
self.timer2 = QTimer(self)
self.timer2.start(1000*10)
self.timer2.timeout.connect(self.timeout2)

def timeout2(self):
    if self.checkBox.isChecked():
        self.check_balance()
