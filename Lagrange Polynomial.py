import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange #Імпортуємо функцію lagrange з бібліотки



x=np.array([-3.,-2.,0.,2.], dtype=float)
y=np.array([-22.,-13.,-7.,23.], dtype=float)

def lagranz(x,y,t):

    z=0

    for j in range(len(y)):

        p1=1; p2=1

        for i in range(len(x)):

            if i==j:

                p1=p1*1; p2=p2*1

            else:

                p1=p1*(t-x[i])

                p2=p2*(x[j]-x[i])

        z=z+y[j]*p1/p2

    return z



xnew=np.linspace(np.min(x),np.max(x),100) #Точки, за якими будуємо графік

ynew=[lagranz(x,y,i) for i in xnew]

plt.plot(x,y,'o',xnew,ynew) #Будуємо графік функції Лагранжа

plt.title('Lagrange Polynomial_1')

plt.grid(True)

plt.show()

f = lagrange(x, y)

fig = plt.figure(figsize = (5,5))

plt.plot(xnew, f(xnew), 'b', x, y, 'ro')

plt.title('Lagrange Polynomial_2')

plt.grid()

plt.xlabel('x')

plt.ylabel('y')

plt.show()

