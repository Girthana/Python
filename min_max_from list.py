"""
Program:Display minimum and maximum values
Input: List of numbers
"""
input_string=input("Enter a list of numbers separated by space")
number_list=input_string.split()
for i in range(0,len(number_list)):
    number_list[i]=int(number_list[i])
print(number_list)
min_number=min(number_list)
max_number=max(number_list)
print("Minimum and Maximum values in the list are ",min_number,"and ",max_number)