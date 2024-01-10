##終極密碼
import random
a=random.randint(1,100)
g=eval(input("輸入終極密碼: "))

m=1
n=100

while g!=a:
    #g=eval(input("輸入你終極密碼介於",m,"-",n,"之間: "))#猜的數字
    if a>g:
        m=g
        n=n
        print("輸入你終極密碼介於",m,"-",n,"之間:")
        #g=eval(input("輸入你終極密碼介於",m,"-",n,"之間: "))
    else:
        m=m
        n=g
        print("輸入你終極密碼介於",m,"-",n,"之間:")
        
    g=eval(input("輸入終極密碼: "))

print("答案正確，終極密碼為",a)
        




