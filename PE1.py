import math
def calc_fibo(n):
   if n <= 1:
       return n
   else:
       return(calc_fibo(n-1) + calc_fibo(n-2))
i=0
while calc_fibo(i)<1000:
    print(calc_fibo(i))
    i=i+1
