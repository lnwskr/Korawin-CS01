Num = int(input("Enter your loop : "))
Numtotal = []
for i in range(Num):
    data = int(input('Enter your data : '))
    Numtotal += [data]
Numtotal.sort(reverse=False)
print(Numtotal[0])
print(Numtotal[Num-1])
