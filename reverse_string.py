"""
Program:Reverse a string
Input: String
"""

ip_str=input("Enter a string")
ip_lst=ip_str.split()
ip_lst.reverse()
rev_str=""
for e in ip_lst:
    rev_str= e+" "+rev_str    
print ("The reversed string is ",rev_str.strip())