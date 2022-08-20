def _opw00001(self, rqname, trcode):
    self.d2_deposit = self._comm_get_data(trcode, "", rqname, 0, "d+2추정예수금")
    
#_receive_tr_data 메서드에서 _opw00001 메서드를 호출하도록 코드를 수정합니다.
if rqname == "opt10081_req":
    self._opt10081(rqname, trcode)

elif rqname == "opw00001_req":
    self._opw00001(rqname, trcode)
    
    
