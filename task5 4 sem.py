import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BTC_data.csv')

plt.figure(figsize=(10,10))
plt.plot(df['time'], df['close'], color="green", label="Цена Bitcoin")
plt.xlabel('Время')
plt.ylabel('Цена')

plt.xticks([])
plt.yticks()

plt.grid(axis='both', linestyle='--')
plt.legend()
plt.savefig('graph_task5.png')
plt.show()