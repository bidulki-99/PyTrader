
self.lineEdit.textChanged.connect(self.code_changed)

def code_changed(self):
    code = self.lineEdit.text()
    name = self.kiwoom.get_master_code_name(code)
    self.lineEdit_2.setText(name)

accouns_num = int(self.kiwoom.get_login_info("ACCOUNT_CNT"))
accounts = self.kiwoom.get_login_info("ACCNO")

accounts_list = accounts.split(';')[0:accouns_num]
self.comboBox.addItems(accounts_list)

self.pushButton.clicked.connect(self.send_order)

def send_order(self):
    order_type_lookup = {'신규매수': 1, '신규매도': 2, '매수취소': 3, '매도취소': 4}
    hoga_lookup = {'지정가': "00", '시장가': "03"}

    account = self.comboBox.currentText()
    order_type = self.comboBox_2.currentText()
    code = self.lineEdit.text()
    hoga = self.comboBox_3.currentText()
    num = self.spinBox.value()
    price = self.spinBox_2.value()

    self.kiwoom.send_order("send_order_req", "0101", account, order_type_lookup[order_type], code, num, price, hoga_lookup[hoga], "")
