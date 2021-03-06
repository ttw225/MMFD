# -*- coding: utf-8 -*-
# Master

print("Material Measurement Fast Drawing Program")
print("使用方法：直接將檔案拖曳至本執行檔，即可進行繪圖")
print("Develop by 王麒淞大帥哥")
print("LOADING MODULES...", end='')

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

print("OK!")

# 處理沒有給檔案的狀況
if(len(sys.argv) == 1):
    print("未偵測到檔案輸入")
else:
    # 處理多個檔案
    for i in range(1, len(sys.argv)):
        print()
        try:
            print("Reading File: {0:s} ... ".format(sys.argv[i]), end="")
            data = pd.read_csv(sys.argv[i], sep="\t",
                               index_col='Wavelength_Ref (nm)')
            print("OK!")
            print("Generating Image ... ", end="")
            new = data['Quantum Efficiency (%)']
            new = new[(new.index>300)&(new.index<1100)]
            new.plot(title = data.columns[4])
            print("OK!")
            plt.show()
        except:
            print("**FALSE!!**")

print("FINISH~")
os.system('pause')
