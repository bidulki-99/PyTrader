class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행': 'A000100'}
    def GetCount(self):
        return len(self.stocks)
    def NameToCode(self, name):
        return self.stocks[name]


instCpStockCode = CpStockCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))

import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
# explore.Visible = True

word = win32com.client.Dispatch("Word.Application")
# word.Visible = True

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1, 1).Value = "hello world"
wb.SaveAs('c:\\Users\\Username\\Desktop\\test.xlsx')
excel.Quit()

wb = excel.Workbooks.Open('c:\\Users\\Username\\Desktop\\test.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1, 1).value)

ws.Cells(1, 2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10
ws.Range("A2:C2").Interior.ColorIndex = 27
excel.Quit()
