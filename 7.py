import numpy as np

def linsys(n, m, matr):           
  a = matr[:, :m-1]               
  b = matr[:, m-1:]               

                                    
  try:                              
    x = np.linalg.solve(a, b)
    return x.flatten().tolist()
  except np.linalg.LinAlgError:
    return None                     

                                    


n, m = map(int, input().split())
matr = [] 
for _ in range(n):      
    r = list(map(float, input().split()))
    matr.append(r)

matr = np.array(matr) 
solution = linsys(n, m, matr) 

if solution is not None:
    print("Решение:")
    i = 1
    for  x in (solution):   
        print(f"x{i} = {x}")
        i += 1
else:
    print("Системане имеет решения или имеет бесконечно много решений")