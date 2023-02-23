#QUIZGAME

#Modules used
import colorama
from colorama import Back, Fore, Style
from math import trunc

#Automatically resets the background,forground, and style of color of the line and won't color the whole line
colorama.init(autoreset=True)


def quizGame():
    #initialization
    SCORE = 0
    QUIZ_ITEMS = 15

    print("IDENTIFICATION\n\n")
    ANSWER_1 = ["Guido Rossum","Guido Van Rossum"]
    print("Question 1. Who developed the Python language?")
    if input().title() in ANSWER_1:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_2 = "1991"
    print("Question 2. What year was Python first released?")
    if input() == ANSWER_2:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_3 = ["if","if statement"]
    print("Question 3. A program called BaChek checks if the applicant is eligible for taking out a loan.\nThe program will only allow the loan if the applicant has good credit and no criminal record/s.\nWhich statement will the program run given the input from the applicant?")
    print("""
    goodCredit = True
    criminalRecord = True

    if goodCredit and not criminalOffense
        print("Applicant is eligible for loan")
    else:
        print("Applicant is not eligible for a loan. Please have the applicant check with their state department about their current status.)
    """)
    if input().lower() in ANSWER_3:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_4 = "Parameter"
    print("Question 4. It's the variable listed inside the parentheses in the function definition.")
    if input().title() in ANSWER_4:
         print(Fore.GREEN + Style.BRIGHT+ "Correct!")
         SCORE += 1
    else:
         print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    print("True or False\n\n")
    ANSWER_5 = ["False","F"]
    print("Question 5. In this line of code:\n\ni_am_value = 'Im a string variable'\n╚--------╝    ╚------------------╝\n    ↑                        ↑\nThis is a value declaration,", "This is a variable.\nIs the above statement True or False?")
    if input().title() in ANSWER_5:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_6 = ["True","T"]
    print("Question 6. JavaScript, CSS, and Python are programming languages")
    if input().title() in ANSWER_6:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_7 = ["False","F"]
    print('Question 7. Comparison operators are used to compare values; "and" "or" "not" are examples of comparison operators.')
    if input().title() in ANSWER_7:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_8 = ["False","F"]
    print("Question 8. The abs() function returns the absolute value of a number and the math.fabs() function from the math module also returns the absolute value of a number.\nHowever, abs() will always return as a floating point number and math.fabs() will depend on the argument")
    if input().title() in ANSWER_8:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    print("Multiple Choice")
    ANSWER_9 = "C"
    print("Question 9. Software is defined as _______\na)A game engine that can run Crysis\nb)Documentation and Configuration of data\nc)Set of programs, documentation & configuration of data\nd)A series of coded instructions to control the operation of a comptuer")
    if input().title() == ANSWER_9:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
         print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_10 =  "A"
    print("Question 10. _____ is a datatype that represent's the truth value of an expression and only has two possible values\na)Bool/Boolean\nb)Python Dictionary\nc)type()\nd)isinstance()")
    if input().title() == ANSWER_10:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()

    
    ANSWER_11 = "C"
    print("Question 11. You can check the version of your Python on the console/terminal using _____\na)python show version\nb)python -version\nc)python --version\nd)python --showVersion")
    if input().title() in ANSWER_11:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_12 = "D"
    print("Question 12. What is the correct way to create a function in Python?\na)create_function myfunction():\nb)function = my_function()\nc)def myfunction: \nd)def myFunction():")
    if input().title() == ANSWER_12:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    print("Enumeration(?)")
    ANSWER_13 = ["casino = '22',int(casino)","casino = '22', int(casino)",
                 "casino = '22' ,int(casino)","casino = '22' , int(casino)",
                 "casino='22',int(casino)","casino='22', int(casino)",
                 "casino='22' ,int(casino)","casino='22' , int(casino)",
                 'casino = "22",int(casino)','casino = "22", int(casino)',
                 'casino = "22" ,int(casino)','casino = "22" , int(casino)',
                 'casino="22",int(casino)','casino="22", int(casino)',
                 'casino="22" ,int(casino)','casino="22" , int(casino)']
    print('Question 13. Declare a variable named "casino" and assign the string "22" then cast it into the integer 22.\nSeparate your answer with a comma')
    if input() in ANSWER_13:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()
    

    ANSWER_14 = ['print("Hello World")',"print('Hello World')"]
    print("Question 14. Create a line of code that will output ' Hello World '")
    if input() in ANSWER_14:
        print(Fore.GREEN + Style.BRIGHT+ "Correct!")
        SCORE += 1
    else:
        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()


    ANSWER_15 = "Pseudocode"
    print("!!RIDDLE QUESTION!!\nI'm a language for everything yet I have no real identity of my own. Good luck trying to compile me. What am I?")
    if input().title() == ANSWER_15:
         print(Fore.GREEN + Style.BRIGHT+ "Correct!")
         SCORE += 1
    else:
         print(Fore.LIGHTRED_EX + Style.BRIGHT + "Wrong!")
    print()

    print(f"You finished the test {Fore.CYAN}{PLAYER_NAME}{Fore.RESET}!\nLet's tally your scores\nTOTAL SCORE: {SCORE}/{QUIZ_ITEMS}\nGRADE: {trunc((SCORE/QUIZ_ITEMS)*100)}%")



    print("❤THANK YOU FOR PARTICIPATING❤")
#Welcoming title and getting player name
print()
print(f"{Fore.RED}{Style.BRIGHT}|||||||||{Fore.YELLOW}{Style.BRIGHT}||||||||{Fore.GREEN}{Style.BRIGHT}||||||||{Fore.CYAN}{Style.BRIGHT}||||||||{Fore.BLUE}{Style.BRIGHT}||||||||{Fore.MAGENTA}{Style.BRIGHT}||||||||||")
print(f"    {Style.BRIGHT}{Back.LIGHTBLACK_EX}WELCOME TO Campbell Ol' Dean Emporium QUIZ!")
print(f"{Fore.RED}{Style.BRIGHT}|||||||||{Fore.YELLOW}{Style.BRIGHT}||||||||{Fore.GREEN}{Style.BRIGHT}||||||||{Fore.CYAN}{Style.BRIGHT}||||||||{Fore.BLUE}{Style.BRIGHT}||||||||{Fore.MAGENTA}{Style.BRIGHT}||||||||||\n\n\n")

PLAYER_NAME = input("Welcome welcome! uhm... err.. What was your name again? ").title()

print(f"Right! {Fore.CYAN}{PLAYER_NAME}{Fore.RESET} what an interesting name.\nSettle in {Fore.CYAN}{PLAYER_NAME}{Fore.RESET} for it's QUIZTIME!\n")

START = input('Please enter "Y" if you want to begin: ').upper()

if START == "Y":
    print("Awesome! Quiz has started!\n\n")
    quizGame()
else:
    print("Oh okay I see how it is then, quiz start! 😈\n\n")
    quizGame()