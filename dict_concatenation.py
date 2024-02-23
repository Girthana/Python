"""
Program:Dictionary_concatenate three dictionaries by creating new one
Input: None or three dictionaries
Output: a new dictionary which is the concatenation of existing three dictionaries 

"""
dict1={"apple": 2,"orange":3,"banana":4,"choclate":2}
dict2={"aple": 2,"nge":3}
dict3={"chikoo":4, "banana":2}
new_dict={}
for dic in (dict1,dict2,dict3):
    new_dict.update(dic)
print("Newly created dictionary:",new_dict)
#print(dict1.get("choclate","Not exists"))