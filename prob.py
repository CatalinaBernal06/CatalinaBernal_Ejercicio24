import numpy as np
import matplotlib.pyplot as plt

def prob_lambda(l):
    if((l<1) or (l>100)):
       return 0
       
    else:
       return 1/99.0
       
def model(x, l):
    return np.exp(-x/l)/l
       
def prob_x_lambda(datos, l):
    pro = 1
    cons = 1/(-np.exp(-20/float(l)) + np.exp(-1/float(l)))
    for i in datos:
       pro *= cons*(model(i, l))
    return pro
       
datos = [1.2, 2.5, 2.8, 5.0]
       
prob_lambda_x = list()
for i in range(1, 100):
       p = prob_x_lambda(datos, i)*prob_lambda(i)
       prob_lambda_x.append(p)
       
plt.figure()
plt.plot(range(1,100), np.log(np.asarray(prob_lambda_x)))
plt.savefig('p_lambda.pdf')
            
