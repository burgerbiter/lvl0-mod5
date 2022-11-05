"""
Write code that can tell if a number is prime.
A prime number is a number that is only divisible by 1 and itself.
"""
from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    # TODO)
    #  1. Ask the user for a number
    #  2. Use a for loop, if statement, and modulo to find if the number
    #     is prime.
    #  3. If the number is divisible by any number other than 1 or itself,
    #     the number is not prime.
    window = Tk()
    window.withdraw()
    num = simpledialog.askinteger(None, prompt="Enter a number")
    for i in range(num-2):
        if num % (i+2) == 0 :
            print("Your number is not prime.")
            exit()
    print("Your number is prime.")
    pass
