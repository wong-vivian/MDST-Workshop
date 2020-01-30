"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if (num%2==0):
        print ("even")
    else:
        print ("odd")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """

    random_number = random.randrange(1,10)    #generate random number
    
    print ("Press exit to quit game")
    guess = ''
    while True:
        guess = str(input("Guess the number: "))
        if (guess.strip()=="exit"):
            break
        elif (int(guess)<random_number):
            print("You have guessed too low")
        elif (int(guess)>random_number):
            print("You have guessed too high")
        elif (int(guess)==random_number):
            print("You have guessed correctly!")
        


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    word = list(string)
    palindrome = True
    for i in range(len(word)):
        if (word[i]!=word[len(word)-i-1]):
            palindrome = False
            break

    if (palindrome == False):
        print ("The word is not a palindrome")
    else:
        print ("The word is a palindrome")

            


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    """ message = "Python is fun"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    """
    with open (filename , 'w') as file:
        file.write(username+"\n")
        password = str.encode(password)
        temp = base64.b64encode(password)
        password = temp.decode ("utf-8")
        file.write(password)
        




def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    username = ""
    passwd = ""

    with open(filename,'r') as file:
        username = file.readline()
        passwd = file.readline()
    b = base64.b64decode((passwd))
    passwd = b.decode("utf-8")
    print(username)
    print(passwd)


if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
