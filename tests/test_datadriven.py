import pytest
import openpyxl

from utilities.excelReader import get_data_from_ExcelFile


# def get_data():
#     return [
#         ['sasa@gmail.com','sasa'],
#         ['nasa@gmail.com','nasa'],
#         ['kasa@gmail.com','nasa']
#     ]

@pytest.mark.parametrize("username,password,age", get_data_from_ExcelFile("ExcelFile/ExcelSheet.xlsx","Login"))
def test_login(username, password,age):
    print("Logged in using: " + username + " and password :" + password +"and age is: "+str(age))
