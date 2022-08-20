#UI 구성 및 배치는 1일차 업로드 이후에 시행 예정
def send_order(self, rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no):
    self.dynamicCall("SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)",
                     [rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no])
                     
def get_chejan_data(self, fid):
    ret = self.dynamicCall("GetChejanData(int)", fid)
    return ret
    
self.OnReceiveChejanData.connect(self._receive_chejan_data)    

def _receive_chejan_data(self, gubun, item_cnt, fid_list):
    print(gubun)
    print(self.get_chejan_data(9203))
    print(self.get_chejan_data(302))
    print(self.get_chejan_data(900))
    print(self.get_chejan_data(901))
    
def get_login_info(self, tag):
    ret = self.dynamicCall("GetLoginInfo(QString)", tag)
    return ret
    
