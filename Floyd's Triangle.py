#lazy
row=int(input("Please enter the total of rows"))
number=1
print("Floyd's triangle")
for i in range(1,row+1) :
    for j in range (1,i+1) :
        print(number,end='  ')
        number=number+1
    print()