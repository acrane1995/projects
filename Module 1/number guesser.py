x = 500
print("Pick a number between 1 and 1000")
print(x)
print("Is this correct?")
result = input()

if result == "yes":
    print("I GUESSED IT!")
else:
    print("Greater or less than?")
    result2 = input()

if result2 == "greater":
    print(x * 1.5)
    x = x * 1.5
else:
    print(x // 2)
    x = x // 2

print("Is this correct?")
result3 = input()

if result3 == "yes":
    print("I GUESSED IT")
else:
    print("Greater or less than?")
    result4 = input()

if result4 == "greater":
    print(x * 1.5)
else:
    print(x // 2)

print("Is this correct?")
result5 = input()

if result5 == "yes":
    print("I GUESSED IT!")
else:
    print("Greater or less than?")
    result6 = input()

if result6 == "greater":
    print(x)



