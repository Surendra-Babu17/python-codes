list1=[2,4,6,8,9]
list2=[1,3,5,7,10]
list1.extend(list2)
print(list1)   

list1=[2,4,6,8,9]
list2=[1,3,5,7,10]
list3=[*list1,*list2]
print(list3)

list1=[2,4,6,8,9]
list2=[1,3,5,7,10] 
C=list1+list2
print(c)  

list1=[2,4,6,8,9]
list2=[1,3,5,7,10]
res=[]
for val in list1:
    res.append(val) 
for val in list2:
    res.append(val)
print(res)   

#python find length of list without usinng len()

list=list(map(int,input("enter a list:").split()))
count=0
for val in list:
    if val>0:
        count+=1 
print(count)

#                                                   sorting a list

arr=list(map(int,input("enter a number:").split()))
arr.sort()
print(arr)   
#                                                Duplicate values in list:

a=list(map(int,input().split())) 
res=[]
for val in a:
    if val not in res:
        res.append(val)
print(res) 

#                                               Second largest Number in list:


a=[23,54,34,67,87,99]
max1=max2= float('-inf')
for val in a:
    if val>max1:
        max2=max1 
        max1=val
    elif val>max2 and val!=max1:
        max2=val 
print(max2)  


minimum number in list
arr=list(map(int,input().split()))  
min=arr[0]
for i in arr:
    if i<min:
        min=i  
print(min)



#sum of list
arr=list(map(int,input().split()))  
sum=0
for i in arr:
    sum+=i 
print(sum) 


num = ["a", 15, "B", "A", 24, "b"]

upper_list = []
lower_list = []
num_sum = 0

for item in num:
    if isinstance(item, str):
        if item.upper() not in upper_list:
            upper_list.append(item.upper())
        if item.lower() not in lower_list:
            lower_list.append(item.lower())
    elif isinstance(item, int):
        num_sum += item

print("Uppercase letters:", "".join(upper_list))
print("Lowercase letters:", "".join(lower_list))
print("Sum:", num_sum) 



arr=[1,2,3,4,2]
duplicates=[]
for i in arr:
    if arr.count(i)>1 and i not in duplicates:
        duplicates.append(i)
for i in duplicates:
    print(i) 

arr=[1,2,3,4,2] 
largest=arr[0]
smallest=arr[0]
for i in arr:
    if i > largest:
        largest=i 
for i in arr:
    if i<smallest:
        smallest=i 
print(f"In given arr {arr} largest number is {largest} and also smallest number is {smallest}.")
        
arr = [1, 4, 5, 2, 5] 
sum_target=6 
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==sum_target:
            print((arr[i],arr[j]))
 
n=6 
arr=[10,5,6,3,7,2]
odd_sum=0
xor_sum=0
for i in range(n):
    if (i+1)%2==0:
        odd_sum+=arr[i] 
    else:
        xor_sum^=arr[i]
result=odd_sum-xor_sum
print(result)   


n=8
arr=[11,1,2,8,10,11,15,7]  
targget=18
found_pairs=[]
for i in range(n):
    for j in range(i+1,n):
        if arr[i]+arr[j]==targget:
            found_pairs.append((arr[i],arr[j]))
result=list(found_pairs[1])
print(result[::-1]) 

'''LINEAR search'''
nums=[1,2,3,4,5,10]
x=10
def find_search(nums,x):
    for i in range(len(nums)):
       if nums[i]==x:
           return True
if find_search(nums,x):
    print("found")
else:
    print("not found") 


'''BINARY search'''
def binary_search(arr,x,left,right):
    if right>=left:
        mid=left+(right-left)//2
        if arr[mid]==x:
            return mid 
        elif arr[mid]>x:
            return binary_search(arr,left,mid-1,x)
        else: 
            return binary_search(arr,mid+1,right,x)
    else:
        return -1 
arr=[2,3,4,10,20]
x=20
result=binary_search(arr,0,len(arr)-1,x)
if result!=-1:
    print(result)
else:
    print("not found") 


'''Longest-prefix List in string'''
s=["surendra","suremanth","suresh"]  #longest prefix is "su" 
prefix=s[0]
for i in range(len(s)):
    while s[i].find(prefix)!=0:
        prefix=prefix[:-1]
print(prefix)
    


ele=[1,2,3,4,5,6,7,8,9]
res=[i for i in ele if i%2==0]   #[styntax for comprahensions: expression loop condition]
print(res) 


ele=[1,2,3,4,5,6,7,8,9]
res=[i**2 for i in ele ]   #[styntax for comprahensions: expression loop condition]
print(res) 

ele=[1,2,3,4,5,6,7,8,9]
res={i:i**3 for i in ele}  #[styntax for comprahensions: expression loop condition]
print(res) 

duplicate counts
nums=[1,1,2]
insert_postion=1
for i in range(1,len(nums)):
    if nums[i]!=nums[i-1]: #0!=-1 
        nums[insert_postion]=nums[i]
        insert_postion+=1 
print(insert_postion)




                
