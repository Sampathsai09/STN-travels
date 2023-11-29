x =int(input("Enter: "))
a= ((x*2)-2)
for i in range(1,(x+1)):
    print("*"*i+" "*a +i * "*")
    a=a-2