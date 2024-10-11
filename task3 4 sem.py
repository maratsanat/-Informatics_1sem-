import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

fig = plt.figure(figsize = (16,9))
a1 = fig.add_subplot(121)
a2 = fig.add_subplot(122)

les12 = [c for c in df['PetalLengthCm'] if c <= 1.2]
more12 = [j for j in df['PetalLengthCm'] if j > 1.2]

les15 = [c for c in df['PetalLengthCm'] if c <= 1.5]
more15 = [c for c in df['PetalLengthCm'] if c > 1.5]

a1.pie([len(les12), len(more12)], labels = ['<= 1.2 cm','> 1.2 cm,'])
a2.pie([len(les15), len(more15)], labels = ['<= 1.5 cm','> 1.5 cm,'])

plt.savefig('graph_task3.png')

plt.show()
df = pd.read_csv('iris_data.csv')
df


x1=list(df['Species']).count('Iris-setosa')
x2=list(df['Species']).count('Iris-virginica')
x3=list(df['Species']).count('Iris-versicolor')
print(x1,x2,x3)
plt.pie([x1,x2,x3], labels = ['Iris-setosa','Iris-virginica','Iris-versicolor'])

plt.title('Species in percent')

plt.show()