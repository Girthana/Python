list1=[1,2,3,4,5,2,3,4]
print("Number of occcurrences of 5 is ",list1.count(5))
print("Largest and smallest numbers are ",max(list1), min(list1))
#list1.sort()
print(list1)
list1.reverse()
print(list1)
l2=[]
if len(l2)==0:
    print("list is empty")
tup=(0,1,2,3)
print(tup.index(2))
a,b,c,d=tup
print(tup[3],tup[-4])
tup1=(0,1,3,2)
if(0 in tup1):
    print("element exist")