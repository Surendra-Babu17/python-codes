   #  Number postive or Negitive
user_input=int(input("enter a number:"))
if user_input<0:
    print(user_input,"is negitive number")
elif user_input>=1:
    print(user_input,"is Positive number")
elif user_input==0:
    print(user_input,"is zero")
elif user_input>0:
    print("is float number")
else:
    print("hey this is invali")


                                              #  if number is divisible by 3 and 5

user_number=int(input("enter a number:"))
if user_number%3==0 and user_number%5==0:
    print("number divisible by both 3&5")
elif user_number%3==0 and user_number%5!=0:
    print("number is only divisible by 3")
elif user_number%3!=0 and user_number%5==0:
    print("number is only divisible by 5")
else:
    print("not divisible by 3 and 5") 
                                            


                                                   #     Maximum of tw0 numbers

user_first_number=int(input("enter a first number:"))
user_second_number=int(input("enter a second number:")) 
if user_first_number>user_second_number:
    print(user_first_number,"is high")
elif user_first_number==user_second_number:
    print("numbers equal")
else:
    print(user_second_number,"is very high")  


                                                  #  vote eligible 
user_age=int(input("enter your age:"))
if user_age>=18:
    print("you are eligible to vote")
else:
    print("sorry your age not eligible")  

                                               #   Marks check


user_marks=int(input("enter your marks:"))
if user_marks>=90 and user_marks<=100:
    print("you are passing with 'A' grade")
elif user_marks>=75 and user_marks<=89:
    print("you are passing with 'B' grade")
elif user_marks>=50 and user_marks<=74:
    print("you are passing with 'c' grade")
else:
       print("sorry you are fail")


                                                #    triangel is valid based are not 

user_enter_side_number=int(input("enter a number:"))
if user_enter_side_number==3:
    print("its triangle")
elif user_enter_side_number==4:
    print("its sqaure")
else:
    print("sorry traingle does not support ",user_enter_side_number,"no.of sides" ) 


                                                #    find between the range 10 to 50

user_number=int(input("enter a number:"))
if user_number>=10 and user_number<=50:
    print(user_number,"is btween the range of 10 to 50")
else:
    print("sorry",user_number,"is not between the range of 10 to 50") 

                                                  #   find number three digit are not
user_number=int(input("enter a number:"))
if user_number>=100 and user_number<=999:
    print("successfully",user_number,"it is three digit number")
else:
    print("sorry",user_number,"it is not three digit number")


n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1==n2 and n1==n3 and n2==n3:
    print("three numbers are equal")
else:
    print("enter your three numbers are equal") 



user_enter=input("enter a character:")
if user_enter=="a":
    print("your character is a vowel") 
elif user_enter=="e":
    print("your character is a vowel") 
elif user_enter=="i":
    print("your character is a vowel") 
elif user_enter=="o":
    print("your character is a vowel") 
elif user_enter=="u":
    print("your character is a vowel") 
else:
    print("sorry! your character is not a vowel its a consonant")


n=input("enter a character or digit")
if n.isdigit():
    print("it is a digit")
else:
    print("it is not a digit sorry its a character")



n=int(input("enter a number:"))
if n>9:
    print("it is  not a singl digit")
elif n<=9 and n>-9:
    print("it is a single digit")
else:
    print("sorry!")  



n=int(input("enter a number"))
if n%2==0 and n%3==0:
    print("your number is divisibile by 2 and 3")
elif n%3==0:
    print("your number is divisibile by 3")
elif n%2==0:
    print("your number is divisibile by both 2")
else:
    print("your number is not divisible by 2 or 3")



n=int(input("enter a number"))
if n%7==0 and n%5==0:
    print("your number is divisibile by 7 and 5")
elif n%7==0and n%5!=0:
    print("your number is divisibile by 7 not 5")
elif n%5==0and n%7!=0:
    print("your number is divisibile by 5 not 7")

else:
    print("your number is not divisible by 7 or 5")




temparature=int(input("enter a your temparature"))
if temparature>0:
    print("your temparature is above freezing point")
else:
    print("your temparature is below freexing point")



n=int(input("enter a number"))
if n>=10 and n<=20:
    print("your number is btween 10 to 20")
else:
    print("your number is not btween 10 to 20")


n=int(input("enter a number"))
if n>0:
    print("your number is absolute number",n)
else:
    
    print("your number is not an absolute number",n)



n=int(input("enter a number:"))
if n>99:
    print("it is a three digit number")
else:
    print("it is not a three digit number")





vijay=int(input("enter a number"))
surendra=int(input("enter a number"))
if vijay>surendra:
    age=vijay-surendra
    print("vijay elder than surendra difference of both ages is:",age)
elif surendra>vijay:
    age=surendra-vijay
    print("surendra elder than vijay difference of both ages is:",age)
else:
    print("Both ages are equal")  






n=int(input("enter a number"))
if n<1000 and n%11==0:
    print("wow! your number is less than 1000 and divisible by 11")
elif n<1000 and n%11!=0:
    print("oops! your number is less than 1000 but not divisible by 11")
else:
    print("sorry! your number is out of range")




n=int(input("enter a month number:"))
if n>=1 and n<=2 and n==12:
    print("woww! its winter season")
elif n>=3 and n<=5:
    print("nice! its spring season") 
elif n>=6 and n<=8:
    print("nice! its summer season")
elif n>=7 and n<=11:
    print("nice! its fall season")
else:
    print("sorry! your number is not a moth number")


n=int(input("enter a month number:"))
result=n**0.5 
if result*result==n:
    
    print("square")
else:
    print("not")
