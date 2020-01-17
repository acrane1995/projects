count = 1
x = 1000 * 1 // 2 ^ count
print("Pick a number between 1 and 1000")
print(x)
print("Is this correct?")
result = input()

if result == "yes":
    print("I GUESSED IT!")
else:
    print("Greater or less than?")
    result2 = input()

count =+ 1

if result2 == "greater":
    print(x)
else:
    print(x // 2)

print("Is this correct?")
result3 = input()

if result3 == "yes":
    print("I GUESSED IT")
else:
    print("Greater or less than?")
    result4 = input()

if result4 == "greater":
    print("Yeet")