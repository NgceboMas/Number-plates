# generating number plates in Azania..

import random

def menu():
    print("=====MENU=====")
    print("1. Mpumalanga")
    print("2. Limpopo")
    print("3. Gauteng")
    print("4. North West")
    print("5. Free sate")
    print("6. KwaZulu Natal")
    print("7. Eastern Cape")
    print("8. Western Cape")
    print("9. Northen Cape")

def Mpumalanga():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(66, 90))
        let3 = chr(random.randint(66, 90))
        print(f"Your new plate is [{first_latter.upper()}{let2}{let3} {num1}{num2}{num3} MP]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} MP")

        else:
            print(f"{name} MP")

def Limpopo():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(66, 90))
        let3 = chr(random.randint(66, 90))
        print(f"Your new plate is [{first_latter.upper()}{let2}{let3} {num1}{num2}{num3} L]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} L")

        else:
            print(f"{name} L")
    
def Gauteng():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(66, 90))
        let3 = chr(random.randint(66, 90))
        let4 = chr(random.randint(66, 90))
        let5 = chr(random.randint(66, 90))

        print(f"Your new plate is [{first_latter.upper()}{let2} {num1}{num2} {let3}{let4} GP]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} GP")

        else:
            print(f"{name} GP")

def KwaZulu_Natal():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(66, 90))
        let3 = chr(random.randint(66, 90))
        let4 = chr(random.randint(66, 90))
        let5 = chr(random.randint(66, 90))

        print(f"Your new plate is [{first_latter.upper()}{let2} {num1}{num2} {let3}{let4} ZN]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} ZN")

        else:
            print(f"{name} ZN")

def North_West():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(65, 90))
        let3 = chr(random.randint(65, 90))
        print(f"Your new plate is [{first_latter.upper()}{let2}{let3} {num1}{num2}{num3} NW]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} NW")

        else:
            print(f"{name} NW")


def Free_State():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(65, 90))
        let3 = chr(random.randint(65, 90))
        print(f"Your new plate is [{first_latter.upper()}{let2}{let3} {num1}{num2}{num3} FS]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} FS")

        else:
            print(f"{name} FS")


def Eastern_Cape():
    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(65, 90))
        let3 = chr(random.randint(65, 90))
        print(f"Your new plate is [{first_latter.upper()}{let2}{let3} {num1}{num2}{num3} EC]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} EC")

        else:
            print(f"{name} EC")


def Northern_Cape():

    # personalized plate

    null = input("Do you want to personalize your plate? (y/n): ")

    if null == "n":

        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)

        first_latter = input("Enter the first letter of current year: ")

        let2 = chr(random.randint(65, 90))
        let3 = chr(random.randint(65, 90))
        print(f"Your new plate is [{first_latter.upper()}{let2}{let3} {num1}{num2}{num3} NC]")

    else:
        name = input("Write your personalized details: ")
        jek = input("make it all caps? (y/n): ")
        if jek == "y":
            print(f"{name.upper()} NC")

        else:
            print(f"{name} NC")


def Western_Cape():
    pass
    
def main():
    select = ""
    #menu()
    while select != "0":
        print("WELCOME TO AZANIA PROVINCE REGISTRATIONS OF PLATES....")
        menu()
        select = input("\nSelect an option to continue: ")

        if select == "1":
            Mpumalanga()

        elif select == "2":
            Limpopo()

        elif select == "3":
            Gauteng()

        elif select == "4":
            North_West()

        elif select == "5":
            Free_State()

        elif select == "6":
            KwaZulu_Natal()

        elif select == "7":
            Eastern_Cape()

        elif select == "8":
            pass

        elif select == "9":
            Northern_Cape()

        else:
            print("invalid option: choose (1 - 9)")

    print("BYE!, Thank you.[*_*]")


if __name__ == "__main__":
    main()