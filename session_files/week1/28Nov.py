a = 1 * 3 / 4 - 5 + 7
a = 3 / 4 - 5 + 7
a = 0.75 - 5 + 7
a = -4.25 + 7
a = 2.75
# print(a)


# not equal to operator

#print(2 != 4)



# integer dision operator: //

# print(4 // 2) # 2
# print(5 / 2) # 2.5
# print(5 // 2) # 2 because // gives the quotient

# print(5.0 / 3)
# print(5.0 // 3)  # still gives the quotient but in float
# print(5 // 3)

# remainder operator / modulus operator : %

# print(5 % 2) # remainder of 1
# print(5.0 % 2) # 1
# print(5 % 2.0) # 1.0

# Exponent operator

# print(2**5)
# print(2**5.0)
# print(2.0**5)
# print(2**True) # 2**1 = 2
# print(2**False) # 2**0 = 1

# # print(2**"5")
# print("5"**2)

# print("Hello")


# Logical Operators

# and, or, not
# and

a = 1==3 and 2==4 # False
a = "" and 2 == 2 # False


# print("Hello",type(a))
# print("string" and False and 1)
# print("string" and 0 and 1)
# print("string" and 1 and 0)

# print("string" and 1 and ["2",5,6])
# print(0.0 and "string" and 1 and ["2",5,6])

# print(int(0.0) and "string" and 1 and ["2",5,6])

# print(0 and ["2",5,6] and "string" and 1 )

# a  = bool("") and 2==2

# print(a)



# or operator

# b = (2==2) or (1==0)
# b = True or False
# print(b)

# b= 1==0 or 2==2 
# print(b)

# when operands are not boolean

# b = "" or 1
# b = bool("String" or 0 or False)
# print(b)


# ["" ,0 , False,"String"]

# ("" and 0 and False) or "String"
# "" or "String"
# "String"

# bool("asdhk" and 1 and True and "String")


# a is a r.v. with values 0 , 1

# a = 1
# b = 4 # binomial
# c = 3 # binomial
# d = 2 # binomiall

# print(bool(a and b and c and d))

# # print

# print("fdask","fadsfasd")

# a = "Hello"
# b = "World"


# print(a+b)
# print(a,b)


# # formatted strings

# print("the value of a is",a)

# c = f"the value of a is {a == b}" # inside curly braces there can be any valid python expression

# print(c)



# not


a = not False # True
b = not True # False

c = not "" # always results in bool value
c = not "bfadskfhas"
#d = not "bfadskfhas" not 1 # not operator can not be chained unlike or , and

# no of nots is odd and operand in truthy => False
d =  not not not 1 # False

e =  0 # => False

print(e)


# print(a,b)
# print(c)







