# -*- coding: utf-8 -*-
# Master

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

print("Material Measurement Fast Drawing Program")
print("Develop by 王麒淞")
print()
# 要處理沒有給檔案的狀況
print("Reading Files ... ", end="")
data = pd.read_csv(sys.argv[1], sep="\t", index_col='Wavelength_Ref (nm)')
print("OK!")
print("Generating Image ... ", end="")
data['Quantum Efficiency (%)'].plot(title=data.columns[4])
print("OK!")
plt.show()


os.system('pause')
