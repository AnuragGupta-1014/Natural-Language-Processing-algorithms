import re
chat1='Me: Hello, I am having an issue with my order # 412889912'
chat2='Me: I have a problem with my order number 412889912'
chat3='Me: My orderd fsfhjsflkjsdfjklsdflkfkf 412889912 is having an issue, I was charged 300$ when online it says 280$'

# now matching- order with id

pattern = 'order[^\d]*\d*'              # \d* give digits and ^\d* gives all other character than digit
print(re.findall(pattern,chat1))
print(re.findall(pattern,chat2))
print(re.findall(pattern,chat3))
print("-"*44)

# now for olny digit after order[^\d]
ptt= 'order[^\d]*(\d*)'   
print(re.findall(ptt,chat1))
print(re.findall(ptt,chat2))
print(re.findall(ptt,chat3))
print("-"*44)



# matching some detail like age, name etc

text='''
Born	Elon Reeve Musk
June 28, 1971 (age 50)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa (1971–present)
Canada (1971–present)
United States (2002–present)
Education	University of Pennsylvania (BS, BA)
Title	
Founder, CEO and Chief Engineer of SpaceX
CEO and product architect of Tesla, Inc.
Founder of The Boring Company and X.com (now part of PayPal)
Co-founder of Neuralink, OpenAI, and Zip2
Spouse(s)	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''

patt = 'age (\d+)'                  #if we assign th ( ) it will giv the resul only under ()
patte = 'age \d+'                  #if we assign th ( ) it will giv the resul only under ()
print(re.findall(patt,text))
print(re.findall(patte,text))

p1 = 'Born(.*)'                    # \n give upto the n line
p11 = re.findall(p1,text)
p11[0].strip()
print(p11)


