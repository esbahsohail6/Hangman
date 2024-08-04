from string import ascii_lowercase #import ascii_lowercase from string library
import random #import random function
import time #import time function


def highscore():
    """Takes no argument and keep track of the highscore"""
    file1 = open("highscore.txt", "a+")
    file1.seek(0)
    read = file1.read().split()#read the highscore file and convert it in to list
    bestscore = 0
    highscorer_name = ""
    for i in read:
        #Since the score can be one or two digit number, therefore using if else statements
        if "=" in i[-2:]:#if score is one digit number, then this statement becomes true
            if bestscore  < int(i[-1:]):
                highscorer_name = i[:-2]
                bestscore  = int(i[-1:])
        elif '=' in i[-3:]: #if score is two digit number, then this statement becomes true
            if bestscore < int(i[-2:]):
                highscorer_name = i[:-3]
                bestscore  = int(i[-2:])
    print(f"Highscore is {bestscore} achieved by {highscorer_name}")


def admin_mode(choice):
    ("""Allow user to write a word in the text file, reset the highscore and to play the game""")
    if choice == 1: #if this statement becomes true, admin is allowed to enter one or multiple words
        file1 = open('words.txt', 'a+')
        f = file1.read().split()
        new_word = input('Enter all the words with comma seperation: ').split(",")
        for word in new_word:
            if word not in f:
                file1.write(word + " ")
        print("The words are added successfully")
    elif choice == 2: #if this statement becomes true , admin is allowed to reset the highscore
        open('highscore.txt', 'w').close()
        print("Scores are reset")
    elif choice == 3: #This statement allow the user to play game
        game()
    elif choice == 4: #To exit the admin mode
        return None
    else:
        print("Invalid Option")

    print('1=Want to Add more words in the text file\n2=Reset the Highscore\n3=To play the game\n4=To Exit')
    choice = int(input('Enter your choice: '))
    admin_mode(choice)


def Secret_word():
    """Takes no argument and import a random word from the word file"""
    file1 = open("words.txt")
    f = (file1.read()).split()
    file1.close()
    return random.choice(f)


def user_score(word, guess, username):
    """Write player's name along with the score in the highscore file and prints the score of the user"""
    score = guess * len(set(word)) #score of the player is the multiplication of no of guess left and length of the word
    file1 = open("highscore.txt", "a")
    file1.write(f"{username}={str(score)} ")
    file1.close()
    print("Your score is", score)
    highscore()


def game():
    """Takes no argument,import a random word from text file on which user plays a game"""
    word = Secret_word()
    secret_word = '_' * len(word)  #the letters of the word are replaced by '_'
    time.sleep(1)
    print(f'Welcome to the Game Hangman!\nI am thinking of a word that is {len(word)} letters long\nYou have 6 '
          f'Guesses and 3 Warnings')
    time.sleep(1)
    available_letters = list(ascii_lowercase) #compile all the lowercase alphabets in a string
    print('available letters =', " ".join(available_letters))
    print(secret_word)
    warn = warning = 3 #assigning two variables to a value so that warning does not become less than zero
    guess = 6
    guessed_letters = []

    while guess > 0:
        letter = input('Enter a Guess : ').lower()
        if len(letter) < 2:
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        secret_word = secret_word[:i] + letter + secret_word[i + 1:]
            elif letter not in word:
                if letter in ('a', 'e', 'o', 'i', 'u') and letter in available_letters: #if a vowel is not in word and is in available letters then the user loses 2 guess
                    guess -= 2
                if letter not in ('a', 'e', 'o', 'i', 'u'): #if a letter is not a vowel and is not in word the user loses a guess
                    guess -= 1
            if letter in guessed_letters or not letter.isalpha(): #if a letter is already guessed or if it is not an alphabet the user loses a warning
                warn -= 1
                if warn >= 0:
                    warning -= 1 #if warn is greater than 1, player loses a warning
                if warn < 0:
                    warning = 0
                    guess -= 1 #if warn is less than zero, player loses a guess
            print(secret_word)
            try:
                available_letters.remove(letter) #remove the guessed letter from the available letters
                guessed_letters.append(letter) #append the letter in the list of guessed letters
            except ValueError: #if try fails this statement becomes true
                pass
            print(f'you have {guess} guesses and {warning} warnings left')
            print('available letters =', " ".join(available_letters))
            if secret_word == word:
                break
        else:
            print('Please Enter a single character')
    if secret_word == word:
        print('CONGRATULATION!! YOU GUESSED CORRECTLY\nThe word is',word)
        user_score(secret_word, guess, user_name) #calls the user_score function
    else:
        print('OOPS SORRY YOU GUESSED WRONG\nThe correct word is ', word)
        highscore() #calls the highscore function
    time.sleep(1)
    choose = input("To Play Again : Press 1\nTO Exit : Press any key except 1 : ")
    if choose == "1":
        game()
    else:
        return None


print('1=User\n2=Admin')
time.sleep(1)
option = int(input('You are playing as: '))
time.sleep(1)
if option == 1:
    user_name = input('Enter your name : ')
    game()
elif option == 2:
    print('1=Add a word in the text file\n2=Reset the Highscore\n3=To play the game\n4=To Exit')
    time.sleep(1)
    choice = int(input('Enter your choice: '))
    admin_mode(choice)
else:
    print("******Invalid Option******")