"""
Program:Dictionary_Check if a value exists in the dictionary
Input: Enter the value to be checked
Output: Value exists or Not exists

"""
dict1={"apple": 2,"orange":3,"banana":4,"choclate":2}
value=int(input("Enter the value to be checked in the dictionary:"))
dict_values=list(dict1.values())
print(dict_values)
if (value in dict_values):
    print("Value exists in the dictionary at index no. ",dict_values.index(value))
else:
    print("Value doesnot exists in the dictionary")
