import numpy as np
import pylab as pl

x = np.arange(0.0, 2.0*np.pi, 0.01)
y = np.sin(x)
pl.plot(x, y)
pl.xlabel('x')
pl.ylabel('y')
pl.title('sin')
pl.show()