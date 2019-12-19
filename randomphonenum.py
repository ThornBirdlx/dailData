# -*- coding:utf-8 -*-
# @Time:    2019/12/19 15:48
# @Author:  liuxiu YOLO

import random
import xlrd
import pandas as pd
import xlwt
import openpyxl


def create_phonenum():
    # second number
    second = [3, 4, 5, 6, 7, 8][random.randint(0, 5)]
    # third number
    third = random.randint(0, 9)
    # last eighth number
    last = random.randint(11111111, 99999999)
    # 将各位数拼接成11位手机号
    return "1{}{}{}".format(second, third, last)


# 将生成的数据写入excel中
def write_data_to_excel():
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'phomenum', cell_overwrite_ok=True)
    for i in range(1, 100000):
        phoneNum = create_phonenum()
        print(phoneNum)
        sheet1.write(0, 0, "姓名")
        sheet1.write(0, 1, "手机号")
        sheet1.write(i, 0, '客户' + str(i))
        sheet1.write(i, 1, phoneNum)
        f.save('phonenum.xlsx')


def read_drop_duplicates():
    excel = pd.read_excel('D:\common\phonenum.xlsx', )
    df = pd.DataFrame(excel)
    print(df.shape)  # 打印行数
    f1 = df.drop_duplicates(subset="手机号")  # 去重
    print(f1.shape)  # 打印去重后的行数
    f1.to_excel('D:\common\phonenum_new.xlsx', index=False)  # 写到一个新的文件


if __name__ == '__main__':
    # write_data_to_excel()
    read_drop_duplicates()