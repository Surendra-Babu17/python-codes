'''                                                                       Print Numbers 1 to 100 using loop
FOR LOOPS
'''
user_input=int(input("enter a number"))                    
for i in range(1,user_input+1,1):
    print(i) 


    
for i in range(1,101,1):
    print(i)    


for i in range(1,101):
    print(i)
    i+=1     


                                                                        # print reverse order 10 to 1 

for i in range(10,0,-1):
    print(i)  

                                                                         # print all even numbers from 1 to 20 

                                                                            
for i in range(2,20+1,2):
    print(i)   

user_range=int(input("enter a range:"))
for i in range(2,user_range+1):
    if i%2==0:
        print(i)  
    
                                                                            # print all odd number in 1 to 15 


for i in range(1,15+1,2):
    print(i) 


for i in range(1,15):
    if 2%2!=0:
        print(i)   
                                                                         #  square numbers from 1 to 10

user_range=int(input("enter a number))
for i in range(2,user_range+1):
    i*=i 
    print(i) 
                                                                          # multication table 5

Multiplication_number=int(input("enter a number))
for i in range(1,10+1):
    i*=Multiplication_number
    print(i)   

                                                                           #sum of 1 to 100 

sum=0
for i in range(1,100+1):
    sum+=i 
print("sum of 1 to 100 numbers is :",sum)   

                                                                       sum of even number form 1 to 50                                                                          
sum=0 
for i in range(1,50+1,2):
    sum+=i 
print (sum)    
      
sum=0 
for i in range(1,50+1):
    if i%2==0:
        sum=sum+i                   
print(sum)
                                                             
                                                                            factorial from given numbers

                                                                            
n=int(input("entr a number"))
fac=1
for i in range(1,n+1):
    fac*=i
print("factorial of 1 to 5 is:",fac)      

                                                                            1 to 100 count how many numbers divisible by 3
user_range=int(input("enter a range:"))
count=0
for i in range(1,user_range+1):
    if i%3==0:
        count+=1 
print(count)                          
    


                                                                                 first 10 Multiples of 7
user_range=int(input("enter a range:"))
for i in range(1,user_range+1):
    if i%7==0:  
    print(i)                                         

                                                                                  Given number prime or not
user_number=int(input("enter a number:"))
temp=0
for i in range(2,user_number):
    if user_number%i==0:
        temp=1
        break 
if temp==1:
    print("Nmber is not prime")
else:
    print("Number is prime")                                      

                                                                                      digit count
user_enter_number=int(input("enter a number:"))
conver_str=str(user_enter_number) 
count=0
for i in conver_str:
    count+=1 
print(count)                                          


i=1
while i<=100:
    if i%2==0:
        print("even")
        i+=1


                                        max and min values in arr
arr=list(map(int,input().split()))  
max=min=arr[0]
for i in arr:
    if i>max:
        max=i 
    if i<min:
        min=i 
print("maximum value in arr is :", max)
print("minum value in arr is:",min)   


                                         # Average of list. 

list=list(map(int,input("enter a numbers").split()))
# avg =sum of numbers/length of numbers 
sum_of_numbers=0
for val in list:
    sum_of_numbers+=val
avg=sum_of_numbers/len(list)
print(avg)
