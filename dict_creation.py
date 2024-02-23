"""
Program:Dictionary_Mapping separate list of keys and values to a single dictionary
Input: None
Output: Dictionary creation with keys and values

"""
list_keys=["apple","banana", "orange", "chickoo"]
list_values=[2,3,4,6]
diction=dict(zip(list_keys,list_values))
print("The newly created dictionary is :", diction)
