# -*- coding: utf-8 -*-
# Master

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

print("Material Measurement Fast Drawing Program")
print("使用方法：直接將檔案拖曳至本執行檔，即可進行繪圖")
print("Develop by 王麒淞")
# 處理沒有給檔案的狀況
if(len(sys.argv) == 1):
    print("未偵測到檔案輸入")
else:
    # 處理多個檔案
    for i in range(1, len(sys.argv)):
        print()
        try:
            print("Reading File: {0:s} ... ".format(sys.argv[i]), end="")
            # 圖片要支援多一些功能
            data = pd.read_csv(sys.argv[i], sep="\t",
                               index_col='Wavelength_Ref (nm)')
            print("OK!")
            print("Generating Image ... ", end="")
            data['Quantum Efficiency (%)'].plot(title=data.columns[4])
            print("OK!")
            plt.show()
        except:
            print("FALSE!!")

print("Good Bye~")
os.system('pause')
