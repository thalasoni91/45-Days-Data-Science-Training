'''name= " upFlairs pvt "
print(name.upper())
print(name.lower())
print(name.title())#saare words ka first letter capital
print(name.capitalize())# only starting word ka first letter capital
print(name.casefold()) #comparison = har char in lower case
print(name.swapcase())# upper to lower and lower to upper
print(name.strip())#removes white spaces 
print(name.lstrip())
print(name.rstrip())
print(name.replace("pvt","ltd"))
print(name.split("l"))
print(name.partition("l"))
print(name.partition("x"))
print(name.startswith("a"))
print(name.endswith(" "))
print(name.isprintable())
print(name.encode())
print(name.encode("utf-8"))
print(name.encode("ascii"))
print(name.zfill(20))
print(name.center(30,"*"))
print(name.ljust(30,"*"))
print(name.rjust(30,"*"))'''

#INDEXING AND SLICING
#INDEXING: accessing single char from the string
#SLICING: accessing multiple chars from the string

# H E L L O      indexing
# 0 1 2 3 4      positive indexing
# -5-4-3-2-1     negative indexing

'''name= "upFlairs pvt"
print(name[0])
print(name[-1])

#[start:end:step/skip]
print(name[0:8]) # works from n to n-1 so 1-7 is satisfied thus
print(name[-3:])#jaha tak end na hojaye'''

'''# formatted string // f-string
age = 10
# text = "my age is" + age  //// gives error due to different datatypes
text = f"my age is {age}"
print(text)'''

# how to double quote a string inside the string
text = 'my name is "Thala"'
print(text)
text = "my name is \"Thala\""
print(text)