"""
Program:Swapping of numbers at two different positions
Input: List of numbers
"""
inpt_str=input("Enter a set of numbers separated by space")
inp_lst=inpt_str.split()
print(inp_lst)
pos=input("Enter two positions to be swapped separated by space within the range")
print(pos ,len(inp_lst))
pos_a,pos_b=pos.split()
pos_a=int(pos_a)
pos_b=int(pos_b)
if ((pos_a<len(inp_lst)) & (pos_b<len(inp_lst))):
    temp=inp_lst[pos_a]
    inp_lst[pos_a] =inp_lst[pos_b]
    inp_lst[pos_b] = temp
    print(inp_lst)
else:
    print("The positions to be swappped are not in the range")