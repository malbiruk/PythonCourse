#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
import pandas as pd
import matplotlib as mpl

mpl.rcParams['figure.figsize'] = (12, 8)

# получаем данные
pareto=np.random.pareto(1000, 1000)

# считаем вероятность каждого из значений:
# словарь с случаями и количеством раз, которые они встречаются
cases = {}
for i in pareto:
    if not i in cases:
        cases[i]=0
    cases[i]+=1

summa=0
for i in cases:
    summa+=cases[i] # сумма всех значений для определения вероятности данного случая

keys=sorted(cases) # лист из случаев
values=[] # лист из значений
for i in keys:
    values.append(cases[i])

probabilities=[0] # вероятность быть меньше первого случая 0

# заполняем лист с вероятностями (для каждого случая вероятность соответствует сумме вероятностей предыдущих случаев)

for i in range(1, len(values)):
    probability=values[i]/summa+probabilities[i-1]
    probabilities.append(probability)

# строим график
# теперь лист со случаями это х, а лист с вероятностями это у
_, so = plt.subplots()
so.plot(keys, probabilities, lw=2, color='pink', alpha=1)
so.set_title('функция распределения парето')
so.set_xlabel('case')
so.set_ylabel('probability')
plt.show()
