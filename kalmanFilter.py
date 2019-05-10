


import math
def mean(x):
    return(sum(x)/len(x))



def variance(x):
    m = mean(x)
    #print(sum([(a - m)**2 for a in x]))
    v = (1.0/len(x))*sum([(a - m)**2 for a in x])
    print(v)
    return(v)

def standDev(x):
    return(math.sqrt(variance(x)))

 
def cov(x,y):
 
    if len(x) != len(y):
        return
         
    n = len(x)
     
    xy = [x[i]*y[i] for i in range(n)]
     
    mean_x = sum(x)/float(n)
    mean_y = sum(y)/float(n)
     
    return (sum(xy) - n*mean_x * mean_y) / float(n)

 
 
x = [1,2,3,4,5,6,7,8,9 ,10]
y = [0.1, 0.2,0.3, 0.4, 0.5,0.6, 0.7,0.8,0.9,1.0]
 
print ('Covariance : ' + str(cov(x,y)) ) 



print(mean([-1,-2,0,1,2]))
print(variance([-1,-2,0,1,2]))
print(standDev([-1,-2,0,1,2]))