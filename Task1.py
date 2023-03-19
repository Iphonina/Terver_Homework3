# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Посчитать (желательно без использования статистических методов наподобие std, var, mean)
# среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий
# для данной выборки.
import math

import numpy as np

my_array = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
S = 0
count = 0
for i in range(len(my_array)):
    S += my_array[i]
    count += 1
average = S/count
average1 = np.mean(my_array)
print(round(average, 2))
print(round(average1, 2))

S1 = 0
for i in range(len(my_array)):
    S1 += (my_array[i] - average)**2
stand_div = math.sqrt(S1/count)
stand_div1 = np.std(my_array)
print(round(stand_div, 2))
print(round(stand_div1, 2))

disp = stand_div**2
disp1 = np.var(my_array)
print(round(disp, 2))
print(round(disp1, 2))

shift_disp = (math.sqrt(S1/(count-1)))**2
shift_disp1 = np.var(my_array, ddof=1)
print(round(shift_disp, 2))
print(round(shift_disp1, 2))