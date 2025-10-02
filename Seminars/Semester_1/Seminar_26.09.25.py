import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0,1,2,3,4]
y = [0,2.2,4.1,5.7,7.5]

x_app = [0, 4]
y_app = [i*2 for i in x_app]
plt.plot(x_app,y_app, color = 'yellow', linewidth = 20, )

plt.scatter(x,y)
plt.grid()
plt.show()