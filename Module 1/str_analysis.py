def str_analysis():
    answer = input("Enter a word or integer: ")
    while True:
        if answer.isalpha() == True:
            print(answer, "is all alphabetical characters!")
            break

        elif answer.isdigit() == True:
            if int(answer) > 0 and int(answer) <= 99:
                print(answer, "that's a smaller number than expected!")
                break
            elif int(answer) >= 100:
                print(answer, "that's a pretty big number!")
                break
        elif answer == "":
            return str_analysis()
        elif answer.isalpha() == False:
            print(answer, "is a surprise! It's neither all alpha or all digit characters!")
            break

str_analysis()