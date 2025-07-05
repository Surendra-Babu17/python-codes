                                #BASICS OF STRINGS
'''
name="surendra"  # In between of single and double codes is string
print(name)          # print name
print(type(name))     # type name 
print(len(name))       #length of name

'''

# string slicing....

'''
word="surendra is very good boy"
print(word[0])   # first index of word is s
print(word[1])
print(word[2])  
print(word[3])       
print(word[0:9])
print(word[:8])
print(word[8:]) 
print(word[::-1]) #reverse order of string 
print(word[-2])  # last second digit od the string
length=len(word)-1   # last index of word is y  
length1=len(word)   
print(word[length])  
print(length) 


'''
# advance slicing methods:
# username="gollapolu surendra babu"
# print(username[9:])  #after 9th index characters to print
# print(username[:9])
# print(username[::2]) # 2 indicates posisition or step 
# word="surendra"
# print(word in username)

#example:1 
#input=gollapolu surendra babu ---- output: index value of each character

# user_name=input("enter your name:")
# length=len(user_name)
# count=0
# for i in range(0,length):
#     if user_name[i]!=" ":
#         count+=1 
# print(count)


#Basic string problems    

#input= jagadhesh ....output=3 .....explination= print(vowels count)

# user_name=input("enter a name:")
# count=0
# length=len(user_name)
# for i in range(length):
#     v=user_name[i]
#     if v=="a" or v=="e" or v=="i" or v=="o" or v=="u" :
#         count+=1 
# print("vowels count in",user_name,"is",count) 











