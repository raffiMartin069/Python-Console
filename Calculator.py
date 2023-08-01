# Basic Calculator Program
# By: Rafael D. Martinez

userPicker = 0


def addition(f_Num, s_Num):
    return f_Num + s_Num


def subtraction(f_Num, s_Num):
    return f_Num - s_Num


def multiplication(f_Num, s_Num):
    return f_Num * s_Num


def division(f_Num, s_Num):
    return f_Num / s_Num


while userPicker != 5:

    print("Enter a number")

    f_Num = int(input())
    s_Num = int(input())

    print("First number: ", f_Num)
    print("Second number: ", s_Num)

    print("\nSelect an operation!")

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    userPicker = int(input())

    if userPicker == 1:
        result = addition(f_Num, s_Num)
        print('You have selected addtition!')
    elif userPicker == 2:
        result = subtraction(f_Num, s_Num)
        print('You have selected subtraction!')
    elif userPicker == 3:
        result = multiplication(f_Num, s_Num)
        print('You have selected multiplication!')
    else:
        result = division(f_Num, s_Num)
        result = round(result, 2)
        print('You have selected division!')

    # result printed
    print("\n", result, "\n===========\n")
