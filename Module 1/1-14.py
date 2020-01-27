i = 'potato'

print(i)

i = 100

print(i)
j = 2
k = 3
i = j+k
print(i)

i = True
if (i == True):
    print('it is true')

i = False
if (i == True):
    print('it is true')

# asdf
color = "blue"
number = 2
if (color == "red" or color == "blue"):
    print( "I'm \"Happy\"")
elif (color == "blue"):
    print("I'm moderately happy")
else:
    print('it is false')

logic = True
if (not logic):
    print("I'm \"happy\"")
else:
    print('I\'m not quite as happy')



if (number < 1):
    print("good")
else:
    print("bad")

number_errors = 0
print("An Integer of", 14, "combined with strings causes",number_errors, "TypeErrors in comma formatted print!")

#collection = ['a', 'b', 'c']
#print(collection[1])

#for i in collection:
#   print(i)

i = 0
while (i < 5):
    i = i+1
    print(i)

collection1 = ['a', 'b', 'c']
collection2 = ['d', 'e', 'f']

collection3 = collection1 + collection2


collection1[2].__add__('x')
print(collection1[2])

collection4 = ['x']
collection3 = collection1 + collection4
print(collection3[3])

number = number ** 10
print(number)

def greet(name):
    print("Hello ",name)
greet("Hans")

def square(number):
    return number **2
x = square(3)

print("I have ",x," potatoes")

#specification: print "even" if it's even, "odd" if it's odd

def evenorodd(number):
    if (number % 2 == 0):
        print("even")
    else:
        print("odd")

evenorodd(5)
