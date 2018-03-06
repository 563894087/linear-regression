import numpy as np
import matplotlib.pyplot as plt
import random

def target_func(theta0,theta1,x):
    return x*theta1 + theta0

def cost_func(theta0,theta1,x,y):
    sum = 0
    for i in range(100):
        sum+=pow((target_func(theta0,theta1,x[i])-y[i]),2)
    return sum*(1/200)

def minimize_theta0(theta0,theta1,x,y,alpha):
    sum = 0
    for i in range(100):
        sum+=(target_func(theta0,theta1,x[i])-y[i])
    theta0 -= alpha * sum * (1/100)
    return theta0

def minimize_theta1(theta0,theta1,x,y,alpha):
    sum = 0
    for i in range(100):
        sum += ((target_func(theta0, theta1,x[i]) - y[i])*x[i])
    theta1 -= alpha * sum * (1/100)
    return theta1

x= np.array([])
y= np.array([])
for i in range(100):
    x = np.append(x,random.uniform(-2,2))
for i in range(100):
    y = np.append(y,-x[i]+1+random.uniform(-1,1))

theta0 = random.uniform(-1,1)
theta1 = random.uniform(-1,1)

while(cost_func(theta0,theta1,x,y) > 0.001):
    temp0 = minimize_theta0(theta0,theta1,x,y,0.01)
    temp1 = minimize_theta1(theta0,theta1,x,y,0.01)
    if(temp0 == theta0 and temp1 == theta1):
        break
    else:
        theta0 = temp0
        theta1 = temp1
    print("theta0=%f\ttheta1=%f\tcost=%f"%(theta0,theta1,cost_func(theta0,theta1,x,y)))

temp_x = np.linspace(-2,2,100)
temp_y = target_func(theta0,theta1,temp_x)

plt.figure(figsize=(10,6))
plt.plot(temp_x,temp_y,label = "$linear function$",color="red")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.legend()
plt.scatter(x,y)
plt.show()