a = int(input())
b = int(input())
c = int(input())   
k = int(input()) 

if b!=0 and a!=0  and (a+b+c*(k-a/b**3))!=0: 
    print(abs((a**2/b**2+c**2*a**2)/(a+b+c*(k-a/b**3))+c+(k/b-k/a)*c))
else: 
    print ("oшибка, деление на 0")
 