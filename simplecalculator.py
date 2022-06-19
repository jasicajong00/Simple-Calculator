import re
#JasicaJongs3805999

def taxationMenu():
    while True:
        print("--------- Walters Association Tax Return Calculation: ---------")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Divison (/)")
        print("5. Quit")
        print("---------------------------------------")
        opt = input("Enter Option: ")

        if not re.search("^[-]?[0-9]+$", opt):
            print(
                "Invalid input entered for option: letter(s) and/or special character(s)")
            print("Valid inputs allowed for option: 1, 2, 3, 4 and 5")

        elif int(opt) == 1:
            print("Addition (+) ")
            add1 = (input("Enter 1st Number: "))
            add2 = (input("Enter 2nd Number: "))
            if re.search("^[-]?[0-9]+$", add1) and re.search("^[-]?[0-9]+$", add2):
                addSum = int(add1) + int(add2)
                print("Result", addSum)
            else:
                print("Invalid input. Numbers and certain special characters only (-)")

        elif int(opt) == 2:
            print("Subtraction (-) ")
            sub1 = (input("Enter 1st Number: "))
            sub2 = (input("Enter 2nd Number: "))
            if re.search("^[-]?[0-9]+$", sub1) and re.search("^[-]?[0-9]+$", sub2):
                subSum = int(sub1) - int(sub2)
                print("Result: ", subSum)

            else:
                print("Invalid input. Numbers and certain special characters only (-)")

        elif int(opt) == 3:
            print("Multiplication (*) ")
            mul1 = input("Enter 1st Number: ")
            mul2 = input("Enter 2nd Number: ")

            if re.search("^[-]?[0-9]+$", mul1) and re.search("^[-]?[0-9]+$", mul2):
                mulSum = int(mul1) * int(mul2)
                print("Result: ", mulSum)

            else:
                print("Invalid input. Numbers and certain special characters (-)")

        elif int(opt) == 4:
            print("Division (/) ")
            div1 = input("Enter 1st Number: ")
            div2 = input("Enter 2nd Number: ")

            if div2 == str(0):
                print("Error. Cannot divide by 0")

            elif re.search("^[-]?[0-9]+$", div1) and re.search("^[-]?[0-9]+$", div2):
                divSum = int(div1) / int(div2)
                print("Result", divSum)

            else:
                print("Invalid input. Numbers and certain special characters (-)")

        elif int(opt) == 5:
            print("Closing Calculator...Goodbye!")
            break

        else:
            print(
                "Invalid input entered for option: number less than 1 or number greater than 5")
            print("Valid inputs allowed for option: 1, 2, 3, 4 and 5")


taxationMenu()
