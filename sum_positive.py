"""
Program:Display Sum of positive numbers
Input: List of integers
"""
input_str=input("Enter a list of integers separated by space")
inp_lst=input_str.split( )
sum=0
for i in range(len(inp_lst)):
    inp_lst[i]=int(inp_lst[i])
    if (inp_lst[i]>0):
        sum=sum+inp_lst[i]
print("Sum of positive integers is ", sum)