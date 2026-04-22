
import matplotlib.pyplot as plt
import numpy as np
x =np.array([10,20,30,40])
y =np.array([30,40,50,60])
plt.plot(x,y,marker='o')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("SIMPLE LINE PLOT")
plt.grid()
plt.show()