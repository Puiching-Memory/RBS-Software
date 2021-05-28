import math
def factorial(n):
   if n==0:
       return 1
   else:
       return n*factorial(n-1)

#计算π值的函数
def pi():
    sum =0
    k=0
    f=2*(math.sqrt(2))/9801
    while True:
        fz = (26390*k + 1103)*factorial(4*k)     #求和项分子
        fm = (396**(4*k))*((factorial(k))**4)    #求和项分母
        t = f*fz/fm
        sum += t
        if t< 0.0000000000000000000000001:                              #最后一项小于10^(-15)时跳出循环
            break
        k += 1                                   #更新k值
    return 1/sum
print(float(pi()))
