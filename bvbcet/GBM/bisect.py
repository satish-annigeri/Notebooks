#Bisection method to find a real root of an equation***********
a,b=input ('enter the value of a and b')
maxitr=input('enter the no. of iterations')
itr=0
print("itr, a, b, x, fx")
func= lambda x: x**3+x-1
while itr<maxitr:
    x=(a+b)/2.0
    fa=func(a)
    fx=func(x)
    if fa*fx<0.0:
        b=x
    else:
        a=x
        print ([a,b,x,fx])
        itr=itr+1