#TRIANGLE
n=int(input("enter the num of rows"))
for i in range(n):
     for j in range (i+1)  :
        left_triangle = "*" * i
        right_triangle = "*" * (6 - i)
        print(left_triangle + " " + right_triangle)