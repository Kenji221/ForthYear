# 1. Matplot Libを利用して２つのグラフを一つのグラフ内に書き込むようにする
# 2. use subplots to create multiple rows and columns in the graph / For文を使って
# 　それぞれのPlotを出力するようにする

import matplotlib.pyplot as plt

import numpy as np
x = np.linspace(0,5,11)
y = x**2

print(x)
print(y)

# plt.show () はOutを無くして出力をさせる
plt.plot(x,y)

# Object　としてPlotを持つようにする
# [w,x,y,z]　→それぞれの左右上下の位置と長さを示すことが可能

fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

