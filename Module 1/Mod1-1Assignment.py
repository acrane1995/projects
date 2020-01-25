input_test = input("Please enter the food categories you've consumed in the last 24 hours (Nuts/Chocolate/Dairy/Starches/Seafood/Etc.): ")
if "dairy" in input_test.lower():
    print("True")
else:
    print("False")

if "nuts" in input_test.lower():
    print("True")
else:
    print("False")

if "seafood" in input_test.lower() :
    print("Seafood was present in your diet in the last 24 hours")
else:
    print()

if "chocolate" in input_test.lower():
    print("Chocolate was present in your diet in the last 24 hours")
else:
    print()