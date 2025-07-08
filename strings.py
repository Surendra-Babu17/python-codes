                                               #---STEP1-BASIC PROGRAMMS OF STRINGS
                   

# name="surendra" 
# print(name)

# name="surendra" #get last character of string 
# print(name[-1])  # method1 find last character in string
# print(len(name)-1)   # method2 find last character in string


# name1="surendra"
# name2="gollapolu" 
# name3="babu"
# result=name2+" "+name1+" "+name3     #concatenate two strings
# print(result) 


# name="surendra" 
# print(name*3)   #output: surendrasurendrasurendra

# '''in between the space of name  from repeating 5 times''' 
# name="surendra " 
# print(name*5)


# name="surendra" 
# print(name[:5])  #slicing first 5 characters in string 


# name="surendra" 
# print(name[::-1])   #reverse method by using slicing only 


# user_full_name="gollapolu surendra babu" 
# name="surendra" 
# last_name="gollapolu" 
# print(name in user_full_name)   # simple method to check substring in sring


                                     # method 2 using if condition.
# user_full_name="gollapolu surendra babu" 
# name="surendra" 
# if name in user_full_name:
#     print("yh!",name,"is in your name") 
# else:
#     print("sorry!",name,"is not your name")  


# name="surendra" 
# print(len(name))  


# name="surendra" 
# print(name.upper()+" "+name.lower())  #string convert upper and lower case  


# name="surendra" 
# print(name.capitalize()) # capital from only first character 


# user_full_name="GollapolU SureNdra babU" 
# print(user_full_name.capitalize()) # first character capital 
# print(user_full_name.title()) # all first character in sentence is capital 
# print(user_full_name.swapcase())



# user_full_name="   gollapolu surendra babu   " 
# print(user_full_name) # print name with spacing
# print(user_full_name.lstrip())            # print name but remove spacing 



# name="surendra"
# print(name.rstrip())                      # print space of name like:   surendra  
 


# user_full_name="gollapolu surendra babu" 
# print(user_full_name.replace("","_"))     ''' use "",this string each character betwwen space  like :  _g_o_l_l_a_p_o_l_u_ _s_u_r_e_n_d_r_a_ _b_a_b_u_'''
# print(user_full_name.replace(" ","_"))    # use "",this string each character between space like: gollapolu_surendra_babu 




# user_full_name="gollapolu surendra babu" 
# print(user_full_name.count("a")) 
# print(user_full_name.count("u"))            ''' count of each character in a string.'''
# print(user_full_name.count("s"))    



# user_full_name="gollapolu surendra babu" 
# print(user_full_name.find("a"))            ''' find keyword use to find index value of character in a string.''' 
# print(user_full_name.find("p"))
# print(user_full_name.find("e")) 
# print(user_full_name.find("surendra"))
# print(user_full_name.find("babu"))
# print(user_full_name.find("gollapolu"))  



# user_full_name="gollapolu surendra babu" 
# result=user_full_name.split()              '''split the string'''
# print(result)  
# print("".join(user_full_name))



# greetings="hello world"
# print(greetings.startswith("hello"))

# greetings1="hello surendra welcome to my world hub"
# print(greetings1.endswith("world"))   #cae-sensitive

# number="surenrdra"
# print(number.isalpha()) 

# values="23456"
# print(values.isdigit())
 
# charchters="surendra017" 
# print(charchters.isalnum())


# print(ord('A'))   #ASCII VALUES TO FIND orders
# print(chr(70))    #ASCII VALUES TO FIND characters.  


# number="surenrdra"
# count=0
# for i in range(1,len(number)):
#     count+=1 
# print(count)  


# sentence="my name is surendra i from chirala"    #method 1
# reuslt=sentence.split() 
# print(reuslt) 
# print(len(reuslt))      #using keywords len


# sentence="my name is surendra i from chirala"     #method2
# sentence_spilit=sentence.split()
# length=len(sentence_spilit)
# count=0
# for i in range(length):
#     count+=1 
# print(count)
 



# '''string to list of characters''' 
# name="surendra"
# print(list(name))   
# ''' output: ['s', 'u', 'r', 'e', 'n', 'd', 'r', 'a']'''


# '''Pad string to the left with * to length 10.''' 
# # name="surendra"
# # padded=name.rjust(20,"7")      #rjust keword used lef side of the *  
# # print(padded)
# '''output: 777777777777surendra'''  

# name="surendra" 
# print(name.center(20,"-")) #center keyword
# '''output:------surendra------'''



# '''Format string with variables using f-string''' 

# # name="surendra"
# # age=24 
# # state="AP"
# # education="Btech" 
# # #f-string 
# # print(f"my name is {name}. i am from {state}. i am completed {education} and my age is{age}")


# '''Use % operator to format a string.''' 
# name="surendra"
# age=24 
# state="AP"
# education="Btech" 
# #f-string 
# print(f"my name is %s. i am from %s . i am completed %s and my age is %d"%(name,state,education,age))



                                        #STEP2  MEDIUM PROBLEMS ON STRINGS 

''' Count number of vowels in a string.'''
# name="surendra" 
# count=0
# for i in range(len(name)):
#     vowels=name[i]
#     if vowels=="a" or vowels=="e" or vowels=="i" or vowels=="o" or vowels=="u":   # count no.of vowels in a string
#         count+=1 
# print(f"in {name} name contain {count} vowels") 
'''in surendra name contain 3 vowels''' 


'''Remove duplicate characters.''' 
# name="mayadhepam"  # duplicate values is "a" in this string 
# res = ""
# for i in name:
#     if i not in res:
#         res+=i
# print(res)
 
'''check if string is palindrome or not''' 
'''method-1'''
# name="surendra" 
# result=name[::-1] 
# if name==result:
#     print(name,"is palindrome") 
# else:
#     print(name,"is not palindrome")  


'''method-2''' 
# name="malayalam"
#temp=int(name) 
#reverse=0
# whiletemp>0:
#     remainder=temp%10
#     reverse=(reverse*10)+remainder
#     temp=temp//10  
# if reverse==name:
#     print("palindrome") 
# else:
#     print("Not palindrome") 

'''method3'''
# name="surendra" 
# res="" 
# for i in name:
#     res=i+res 

# if res==name:
#     print(f"your name is {name}. if reverse your name is {res}. so both are same wow! its palindrome") 
# else:
#     print(f"your name is {name}. if reverse your name is {res}. so both are not same sorry! its not palindrome")


    




# name="surendra" # u e a vowels in surendra name 
# # where vowels are present that palce we assigned * symbol 
# vowel="aeiouAEIOU"  
# res=""
# for i in name: #i=s ,i=u i=r ... 
#     if i in vowel: # i=a i=e... 
#         res+="*" 
#     else:
#         res+=i 
# print(res)

'''check if two strings anargams are not''' 
#anargams means if i give one string that is listen when in string keyword to crate new word that is anargams silent

# name1="liSten" 
# name2="silent" 
# name1=name1.lower()
# name2=name2.lower()
# result1=sorted(name1)
# result2=sorted(name2)
# if result1==result2:
#     print("anargam") 
# else:
#     print("not anargam") 


'''Each and every word is reverse in a sentence''' 
# sentence="my name is surendra"
# "split the sentence first"
# list_word=sentence.split()  #['my', 'name', 'is', 'surendra']
# reverse_word=[]
# for word in list_word:
#     reverse=word[::-1] 
#     reverse_word.append(reverse) 
#     result=" ".join(reverse_word)
# print(result)

    