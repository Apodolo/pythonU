import numpy as np
import pandas as pd

random_list = np.random.randint(1, 101, size=10)

random_series = pd.Series(random_list, index=range(1, 11), name='numeros aleatorios')
random_series.index.name = 'idx'

print("Serie original:")
display(random_series)

squared_series = random_series ** 2

print("\nSerie al cuadrado:")
display(squared_series)

print("\nÚltimos 4 elementos de la serie al cuadrado:")
display(squared_series.tail(4))

numbers_greater_than_500 = squared_series[squared_series > 500].tolist()
print("\nNúmeros mayores a 500 (como lista):")
print(numbers_greater_than_500)