import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [39.2, 22.6,  28.5 , 25.9, 23.7,19.5,14.4]
y = [35.6, 20.5,  26.1, 23.7, 21.6, 18, 13]
plt.figure(figsize=(8,5), dpi=100)

plt.plot(x,y, 'b+-', color="green", markersize=10, markeredgecolor='red')

plt.title('Зависимость центра масс от a', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.ylabel('a, см')
plt.xlabel('Расстояние от Ц.М до оси, см')

plt.xticks()
plt.yticks()

plt.grid()

plt.legend()

plt.savefig('graph.png', dpi=300)

plt.show()