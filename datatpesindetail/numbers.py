x=2
y=3
z=9
#Math operations
addition = x + y
subtraction = z - y
multiplication = x * y
division = z / x
exponentiation = x ** y
modulus = z % y
print("Addition:", addition) #Output: Addition: 5
print("Subtraction:", subtraction) #Output: Subtraction: 6
print("Multiplication:", multiplication) #Output: Multiplication: 6
print("Division:", division) #Output: Division: 4.5
print("Exponentiation:", exponentiation) #Output: Exponentiation: 8
print("Modulus:", modulus) #Output: Modulus: 0
# error ="mani"+5 # This will raise a TypeError: unsupported operand type(s) for +: 'str' and 'int'
# opereator overloading
concatenation = "mani" + "simha"
print("Concatenation:", concatenation) #Output: Concatenation: manisimha
changedtupples=x,x+y,y+z
print(changedtupples) #Output: (2, 5, 12)
# to print as it is
str('mani') #Output: 'mani'
repr('mani') #Output: "'mani'"
# we have and or operators as well and not symbols like other languages
a=True
b=False
print(a and b) #Output: False
print(a or b) #Output: True
# tricker question
print(1==2<3) # false because 1==2 is false and false<3 is true but overall false
# Floor and ceil functions 
import math
print(math.floor(2.9)) #Output: 2
print(math.ceil(2.1)) #Output: 3
# truncate function
print(math.trunc(2.9)) #Output: 2

