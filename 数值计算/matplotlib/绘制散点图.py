import numpy as np
import pylab as pl

x = np.arange(0.0, 2.0*np.pi, 0.1)
y = np.cos(x)
pl.scatter(x, y)
pl.xlabel('x')
pl.ylabel('y')
pl.title('cos')
pl.show()

a = np.random.random(100)
b = np.random.random(100)
pl.scatter(a, b, s=a*500, c='r', marker='*')
pl.show()