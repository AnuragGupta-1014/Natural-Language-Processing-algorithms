import re         #regular expression....that is use for pattern matching 

chat1 = 'Me: you ask a lot of question $ 1545231245,1545231245 6525231247 15452312r45 acd@xuz.com'
chat2 = 'Me: here it is: (154)-523-1245,acd@xuz.com'
chat3 = 'Me: phone: 1545231245 email: acd@xuz.com'


pattern1 = '\d{10}'                 #gives the 10 regualer digit    /d is for one digit and /d{10} for 10 digit
match1 = re.findall(pattern1,chat1)
print(match1)

# now for (154) we can't use ('\d{3}') ,we have to use    \(\d{3}\)
pattern2 = '\(\d{3}\)-\d{3}-\d{3}'
match1 = re.findall(pattern2,chat2)   
      #OR  
match2 = re.findall('\(\d{3}\)-\d{3}-\d{3}', chat2)
print(match1,match2)

# we can use both pattern in one by usin or operator = |

pattern = '\d{10}|\(\d{3}\)-\d{3}-\d{3}'
print(re.findall(pattern,chat2))

# for email  abc@xyx.com =  [a-z]@ it will give one digit before @   and [a-z]*@ gives all sequence of character

email = '[a-z0-9A-Z]*@[a-z0-9A-Z]*\.[a-zA-Z]*'            # we cannot use . direclty as @ because in re . have special meaning so \.
# always use * to choose sequence of char
print(re.findall(email,chat1))


all = '\d{10}|\(\d{3}\)-\d{3}-\d{3}|[a-zA-Z0-9]*@[a-zA-Z0-9]*\.[a-zA-Z]*'
print("all detail", re.findall(all,chat2))