#(number should be between 1 and 1000)
intervalMin = 1
intervalMax = 1000

def get_computers_guess(intervalMin, intervalMax):
    return int((intervalMin + intervalMax) / 2)
    # return int( intervalMin + (intervalMax - intervalMin) / 2 )  # just for full correctness, google it
#650

while(True):
    #ask a number
    number = get_computers_guess(intervalMin, intervalMax)
    c = input("My guess is " + str(int(number)) + ". Is it correct, greater, or lesser than the number you thought of C/L/G?" )
    if (c == "C"):
        print("Yay!")
        break
    if (c == "L"):
        intervalMax = number - 1
    elif (c == "G"):
        intervalMin = number + 1

#  7