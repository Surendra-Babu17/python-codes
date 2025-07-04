# method-1
# user_input=int(input("enter a number:"))
# if user_input%2==0:
#     print("even")
# else:
#     print("odd")

# Method2
# user_input=int(input("enter a number:"))
# print("even" if user_input%2==0 else "odd" )

#                                                           #  Number postive or Negitive
# user_input=int(input("enter a number:"))
# if user_input<0:
#     print(user_input,"is negitive number")
# elif user_input>=1:
#     print(user_input,"is Positive number")
# elif user_input==0:
#     print(user_input,"is zero")
# elif user_input>0:
#     print("is float number")
# else:
#     print("hey this is invali")


#                                               #  if number is divisible by 3 and 5

# user_number=int(input("enter a number:"))
# if user_number%3==0 and user_number%5==0:
#     print("number divisible by both 3&5")
# elif user_number%3==0 and user_number%5!=0:
#     print("number is only divisible by 3")
# elif user_number%3!=0 and user_number%5==0:
#     print("number is only divisible by 5")
# else:
#     print("not divisible by 3 and 5") 
                                            


#                                                    #     Maximum of tw0 numbers

# user_first_number=int(input("enter a first number:"))
# user_second_number=int(input("enter a second number:")) 
# if user_first_number>user_second_number:
#     print(user_first_number,"is high")
# elif user_first_number==user_second_number:
#     print("numbers equal")
# else:
#     print(user_second_number,"is very high")  


#                                                   #  vote eligible 
# user_age=int(input("enter your age:"))
# if user_age>=18:
#     print("you are eligible to vote")
# else:
#     print("sorry your age not eligible")  

#                                                #   Marks check


# user_marks=int(input("enter your marks:"))
# if user_marks>=90 and user_marks<=100:
#     print("you are passing with 'A' grade")
# elif user_marks>=75 and user_marks<=89:
#     print("you are passing with 'B' grade")
# elif user_marks>=50 and user_marks<=74:
#     print("you are passing with 'c' grade")
# else:
#        print("sorry you are fail")


#                                                 #    triangel is valid based are not 

# user_enter_side_number=int(input("enter a number:"))
# if user_enter_side_number==3:
#     print("its triangle")
# elif user_enter_side_number==4:
#     print("its sqaure")
# else:
#     print("sorry traingle does not support ",user_enter_side_number,"no.of sides" ) 


#                                                 #    find between the range 10 to 50

# user_number=int(input("enter a number:"))
# if user_number>=10 and user_number<=50:
#     print(user_number,"is btween the range of 10 to 50")
# else:
#     print("sorry",user_number,"is not between the range of 10 to 50") 

#                                                   #   find number three digit are not
# user_number=int(input("enter a number:"))
# if user_number>=100 and user_number<=999:
#     print("successfully",user_number,"it is three digit number")
# else:
#     print("sorry",user_number,"it is not three digit number")


# n1=int(input("enter a number:"))
# n2=int(input("enter a number:"))
# n3=int(input("enter a number:"))
# if n1==n2 and n1==n3 and n2==n3:
#     print("three numbers are equal")
# else:
#     print("enter your three numbers are equal") 



# user_enter=input("enter a character:")
# if user_enter=="a":
#     print("your character is a vowel") 
# elif user_enter=="e":
#     print("your character is a vowel") 
# elif user_enter=="i":
#     print("your character is a vowel") 
# elif user_enter=="o":
#     print("your character is a vowel") 
# elif user_enter=="u":
#     print("your character is a vowel") 
# else:
#     print("sorry! your character is not a vowel its a consonant")


# n=input("enter a character or digit")
# if n.isdigit():
#     print("it is a digit")
# else:
#     print("it is not a digit sorry its a character")



# n=int(input("enter a number:"))
# if n>9:
#     print("it is  not a singl digit")
# elif n<=9 and n>-9:
#     print("it is a single digit")
# else:
#     print("sorry!")  



# n=int(input("enter a number"))
# if n%2==0 and n%3==0:
#     print("your number is divisibile by 2 and 3")
# elif n%3==0:
#     print("your number is divisibile by 3")
# elif n%2==0:
#     print("your number is divisibile by both 2")
# else:
#     print("your number is not divisible by 2 or 3")



# n=int(input("enter a number"))
# if n%7==0 and n%5==0:
#     print("your number is divisibile by 7 and 5")
# elif n%7==0and n%5!=0:
#     print("your number is divisibile by 7 not 5")
# elif n%5==0and n%7!=0:
#     print("your number is divisibile by 5 not 7")

# else:
#     print("your number is not divisible by 7 or 5")




# temparature=int(input("enter a your temparature"))
# if temparature>0:
#     print("your temparature is above freezing point")
# else:
#     print("your temparature is below freexing point")



# n=int(input("enter a number"))
# if n>=10 and n<=20:
#     print("your number is btween 10 to 20")
# else:
#     print("your number is not btween 10 to 20")


# n=int(input("enter a number"))
# if n>0:
#     print("your number is absolute number",n)
# else:
    
#     print("your number is not an absolute number",n)



# n=int(input("enter a number:"))
# if n>99:
#     print("it is a three digit number")
# else:
#     print("it is not a three digit number")





# vijay=int(input("enter a number"))
# surendra=int(input("enter a number"))
# if vijay>surendra:
#     age=vijay-surendra
#     print("vijay elder than surendra difference of both ages is:",age)
# elif surendra>vijay:
#     age=surendra-vijay
#     print("surendra elder than vijay difference of both ages is:",age)
# else:
#     print("Both ages are equal")  






# n=int(input("enter a number"))
# if n<1000 and n%11==0:
#     print("wow! your number is less than 1000 and divisible by 11")
# elif n<1000 and n%11!=0:
#     print("oops! your number is less than 1000 but not divisible by 11")
# else:
#     print("sorry! your number is out of range")




# n=int(input("enter a month number:"))
# if n>=1 and n<=2 and n==12:
#     print("woww! its winter season")
# elif n>=3 and n<=5:
#     print("nice! its spring season") 
# elif n>=6 and n<=8:
#     print("nice! its summer season")
# elif n>=7 and n<=11:
#     print("nice! its fall season")
# else:
#     print("sorry! your number is not a moth number")


# n=int(input("enter a month number:"))
# result=n**0.5 
# if result*result==n:
    
#     print("square")
# else:
#     print("not")






















#                                        # LEAP YEAR OR NOT

# n=int(input("enter anumber:"))           # user enter  a year
# if (n%4==0 and n%100!=0) or n%400==0:     #number divisible 4 or 400 and not equal 100
#     print("Leap year")            #leap year or not leap year
# else:
#     print("Not Leap Year")

#                                         # max and min values in arr
# arr=list(map(int,input().split()))  
# max=min=arr[0]
# for i in arr:
#     if i>max:
#         max=i 
#     if i<min:
#         min=i 
# print("maximum value in arr is :", max)
# print("minum value in arr is:",min)   


#                                          # Average of list. 

# list=list(map(int,input("enter a numbers").split()))
# # avg =sum of numbers/length of numbers 
# sum_of_numbers=0
# for val in list:
#     sum_of_numbers+=val
# avg=sum_of_numbers/len(list)
# print(avg)


                        # python code Merge two lists in four differnt methods
# list1=[2,4,6,8,9]
# list2=[1,3,5,7,10]
# list1.extend(list2)
# print(list1)   

# list1=[2,4,6,8,9]
# list2=[1,3,5,7,10]
# list3=[*list1,*list2]
# print(list3)

# list1=[2,4,6,8,9]
# list2=[1,3,5,7,10] 
# C=list1+list2
# print(c)  

# list1=[2,4,6,8,9]
# list2=[1,3,5,7,10]
# res=[]
# for val in list1:
#     res.append(val) 
# for val in list2:
#     res.append(val)
# print(res)  


                                       # python find length of list without usinng len()

# list=list(map(int,input("enter a list:").split()))
# count=0
# for val in list:
#     if val>0:
#         count+=1 
# print(count)


#                                          # convert celcius to fahrenheit  f=(c*9/5)+32 

# c=float(int(input("enter a celcius")))
# f=(c*9/5)+32 
# print(c)
# print(f)
 
                                                #convert farhenheit to celcius (f-32)*5/9 
# f=int(input("enter a farhenesit:"))
# c=(f-32)*5/9 
# print(c)
                                                      #sorting a list

# arr=list(map(int,input("enter a number:").split()))
# arr.sort()
# print(arr)   
                                                # Duplicate values in list:

# a=list(map(int,input().split())) 
# res=[]
# for val in a:
#     if val not in res:
#         res.append(val)
# print(res) 

                                               #Second largest Number in list:


# a=[23,54,34,67,87,99]
# max1=max2= float('-inf')
# for val in a:
#     if val>max1:
#         max2=max1 
#         max1=val
#     elif val>max2 and val!=max1:
#         max2=val 
# print(max2)  


                                  # Multiplication Table of Given Number: 

# n=5
# i=1 
# while i<=20:
#     result=n*i 
#     i+=1
#     print(result)

                                             #GCD in range of given number
# n1=int(input("enter a number:"))
# m1=int(input("enter a number:"))
# gcd=1 
# for i in range(1,min(n1,m1)):
#     if n1%i==0 and m1%i==0:
#         gcd=i 
# print(gcd) 


                                             # given number is prime are not

# n=int(input("enter a user number:"))
# flag=0

# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break 
# if flag==1:
#     print("not prime")
# else:
#     print("prime") 



                                                        #Reaverse a string..
# name=input("enter a name:")
# rev=""
# for i in name:
#     rev=i+rev  
# print(rev) 

                                                          #palindrome or not a string  
# name=input("enter a name:")
# rev=""
# for i in name:
#     rev=i+rev  
# if rev==name:
#     print("palindrome") 
# else:
#     print("not palindrome") 

                                                            #Number reverse are not
# name=int(input("enter a name:"))
# name1=str(name)
# rev=""
# for i in name1:
#     rev=i+rev  
# print(rev)  

                                                        #number palindrome are not

# name=int(input("enter a name:"))
# name1=str(name)
# rev=""
# for i in name1:
#     rev=i+rev 
# if rev==name1:
#     print("palindrome") 
# else:
#     print("not palindrome")  

                         # minimum number in list
# arr=list(map(int,input().split()))  
# min=arr[0]
# for i in arr:
#     if i>min:
#         min=i  
# print(min)



                                           #sum of list
# arr=list(map(int,input().split()))  
# sum=0
# for i in arr:
#     sum+=i 
# print(sum) 

                                            #No.OF vowels IN string:

# name=input("enter a string:")
# count=0 
# for i in name:

#     if i=="a" or i=="e" or i=="o" or i=="u":
#         count+=1 
# print(count) 

                                                          # fABNOCCI SERIES
# n=int(input("enter a nth term:"))
# n1,n2=1,2 
# print(n1,n2,end=" ")
# for val in range(2,n+1):
#     n3=n1+n2
#     n1=n2
#     n2=n3 
#     print(n3,end=" ")  



# n=int(input("enter a number:"))
# fact=1
# if n<=0:
#     print("number is negitive or zero")
# else:
#     for i in range(1,n+1):
#         fact*=i 
# print(fact) 


                                                    # largest three digit number 

# user_first_number=int(input("enter a number:"))
# user_second_number=int(input("enter a number:"))
# user_third_number=int(input("enter a number:"))
# if (user_first_number>=user_second_number) and (user_first_number>=user_third_number):
#     print(user_first_number,"is High")
# elif (user_second_number>=user_first_number) and (user_second_number>=user_third_number):
#     print(user_second_number,"is high")
# else:
#     print(user_third_number,"is high")  
















'''                                                                       Print Numbers 1 to 100 using loop
FOR LOOPS

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


# i=1
# while i<=100:
#     if i%2==0:
#         print("even")
#         i+=1

# user_intial_number=int(input("enter a number"))
# user_ended_number=int(input("enter a number"))
# for n in range(user_intial_number,user_ended_number+1):
#     if n%2==0:
#         print(n)
                                                                   ''' 
                           # NESTED LOOPS

# 1 TO 10:
 
# lines=int(input("enter a number:"))  #3
# for i in range(lines+1):
#     total=""


















   
    
# class students:  #creating class
#     name="surendra"    # class attribute
# a=students()           #creating object
# print(a.name)          # object accessing class attribute


# class laptop:  #creating a class
#     name="HP I5"
#     color="silver"   # name,color,cost these are all attribute of the class
#     cost="50,00"
# a=laptop()    #creating  an object from class

# print("name of the laptop:",a.name,"color of the laptop:",a.color,"cost of the laptop:",a.cost)  # access the class attribute 


# class Greeter:                        # class creating greeter 
#     def greet(self,name):              # method using print name      
#         print(f"Hello,{name}!")
# s1=Greeter()                            #object creating
# s1.greet("surendra")


# YOUR task creating chocolates and print chocolate name and price 



# class shop:
#     # name="one touch" 
#     def __init__(self,name,shopnumber,phonenumber):
#         self.shopnumber=shopnumber
#         self.phonenumber=phonenumber
#         self.name=name
# name1=shop("one touh",326,3456789)
# print(name1.name)
# print(name1.shopnumber)
# print(name1.name)    




# class students:
#     def __init__(self,name,age,village):
#         self.name=name
#         self.age=age
#         self.village=village 
#     def __str__(self):
#         return f"{self.name} is {self.age} years old.He lives in {self.village}"
# student1=students("surendra",23,"akkayapalem")
# student2=students("ravi",24,"bapatla")
# print(student2)
        
# class college:   #creating class
#     college_name="st anns college"   #class attribute
#     def __init__(self,location,strength,yearlyfess):
#         self.location=location
#         self.strength=strength
#         self.yearlyfees=yearlyfess
#     def __str__(self):
#         return f"{self.college_name}located in {self.location}strength is{self.strength}from yearly {self.yearlyfees}"

# details=college("chirala",40000,90000)  #creating object from class
# print(details)   #acessing class attribute  


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks  
#     def get_avg(self):
#         sum=0  
#         length=len(self.marks)                 # avg= sum of numbers/total number of numbers
#         for i in self.marks:
#             sum+=i 
#         print("hii",self.name,"your final marks avg is",sum/length,"your performance is very good")


# s1=student("surendra",[99,98,97])
# s1.get_avg()

# list=[99,98,97] 
# sum=0  
# length=len(list)                 # avg= sum of numbers/total number of numbers
# for i in list:
#     sum+=i 
# print(sum/length)


# class Account:
#     def __init__(self,balance,account):
#         self.balance=balance
#         self.account_no=account
#     def debit(self,amount):
#         self.balance-=amount
#         print("In your banck balnance was debited RS.", amount, "now your final bank blance is:", self.get_balance())
#     def credit(self,amount):
#         self.balance += amount
#         print("In your banck balnance was credited RS.", amount,"now your final bank blance is:", self.get_balance())
#     def get_balance(self):
#         return self.balance 

# s1=Account(10000,179620)
# s1.debit(500)



# class Greeter:
#     name="surendra!"
# s1=Greeter()
# print("Hello",s1.name)  


# class Greeter:
#     def greet(self,name):
#         print(f"Hello,{name}!")
# s1=Greeter()
# s1.greet("surendra")


