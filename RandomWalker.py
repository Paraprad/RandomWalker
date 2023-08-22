import matplotlib.pyplot as plt
import random as rn
import numpy as np
n = 10000
class Walker:
  def walk(n):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(1,n):
      val = rn.randint(1,4)
      if val == 1 :
        x[i] = x[i-1]+1
        y[i] = y[i-1]
      elif val == 2 :
        x[i] = x[i-1]-1
        y[i] = y[i-1]
      elif val == 3 :
        x[i] = x[i-1]
        y[i] = y[i-1]+1
      else :
        x[i] = x[i-1]
        y[i] = y[i-1]-1
    return x, y
w = Walker.walk(n)
x1, y1 = w
plt.title("Random Walk ($n = " + str(n) + "$ steps)")
plt.plot(x1, y1)
plt.show()
  
  
