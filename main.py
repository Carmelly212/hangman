
#Hangman game code by Alon Carmelly

def choose_word(path,num):
    """reads a single word from a file and allows user to select one word out 8.
       :param path: path location of file
       :param num: number input by user
       :type path: string
       :type num: int
       :return: function returns one word
       :rtype: str
       """

   # file = open(path,'r')
   # read1 = file.readline()
   # list1 = read1.split(' ')
#
#
   # new_set = set(list1)
    unique_list = [sorted((list(new_set)))]

    index = (num+1) % 8
    return unique_list[index]

def open_screen():
    """opening screen Ascii graphix.
           :rtype: str
           """
    HANGMAN_ASCII_ART = """         _    _
        | |  | |
        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_  \ \

        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                             __/ |
                            |___/"""
    print(HANGMAN_ASCII_ART)




def try_update_letter_guessed(letter_guessed,history):
    """function appends letter picked by user into a list named History
           :param letter_guessed: one letter that was input by user
           :param history: a list of letters that was guessed already
           :type letter_guessed: string
           :type history: string
           :return: word added to History list and presented
           :rtype: str
           """
    if is_valid_input(letter_guessed,history) and letter_guessed not in history:#letter_guessed_history = history
        history.append(letter_guessed.lower())
        alterd_history = ' --> '.join(sorted(history))
        print('---------------------------')
        print('GUESSED: -->', alterd_history.upper())

    else:

        print("\n")
        print('-->',letter_guessed,'<--', 'ALREADY USED')
        print('GUESSED: -->', ' --> '.join(sorted(history)).upper())







def picture(num_trys):
    """function presents Ascii figure of the Hangman when int is entered.
               :param num_trys: one letter that was input by user
               :type num_trys: int
               :return: word added to History list and presented
               :rtype: dict
               """
    HANGMAN_PHOTOS = {1: '\x1b[1;34m' + "x-------x" + '\x1b[0m',
                      2: '\x1b[1;34m' + "x-------x" + '\x1b[0m\n|\n|\n|\n|\n|',
                      3: '\x1b[1;34m' + "x-------x" + '\x1b[0m\n|    |\n|\n|\n|\n|',
                      4: '\x1b[1;34m' + "x-------x" + '\x1b[0m\n|    |\n|    @\n|\n|\n|',
                      5: '\x1b[1;34m' + "x-------x" + '\x1b[0m\n|    |\n|    @\n|   /|\\\n|\n|',
                      6: '\x1b[1;34m' + "x-------x" + '\x1b[0m\n|    |\n|    @\n|   /|\\\n|   / \\\n|',
                      7: '\x1b[1;34m' + "x-------x" + '\x1b[0m\n|    |\n|    @\n|   /|\\\n|   / \\\n|   DEAD !  ' }

    print(HANGMAN_PHOTOS[num_trys])





def is_valid_input(letter_guessed, history):
    """function checks if input by user is valid
               :param letter_guessed: one letter that was input by user
               :param history: a list of letters that was guessed already
               :type letter_guessed: string
               :type history: string
               :return: word added to History list and presented
               :rtype: str
               """
    chk = letter_guessed.isalpha()
    if (len(letter_guessed) > 1) or chk != True:
        return False
    else:
        if chk:

            return True

def check_win(secret_word, history):
    """function checks if user guessed all letters and won.
                   :param secret_word: the word that has to be guessed
                   :param history: a list of letters that was guessed already
                   :type secret_word: string
                   :type history: string inside a list
                   :return: True or False
                   :rtype: bool
                   """

    for char in secret_word:
        if char not in history:
            return False
    return True


new_word = []

def show_hidden_word(secret_word, history):
    """function appends history to new list and letters not guessed as '_'
                       :param secret_word: the word that has to be guessed
                       :param history: a list of letters that was guessed already
                       :type secret_word: string
                       :type history: string inside a list
                       :return: list appended
                       :rtype: str
                       """
    new_word.clear()
    for x in secret_word:
        if x in history:
            new_word.append(x)

        else:
            new_word.append('_')





def main():
    CRED = '\033[91m' #open red color
    CRED_END = '\033[0m'#close red color
    CBlue = '\033[96m'#open blue color
    CBlue_END = '\033[0m'#close blue color
    CYel = '\033[33m'#open yellow color
    CYel_END = '\033[0m'#close yellow color
    print(CRED + "Welcome to!" + CRED_END)
    open_screen()
    while True: #checks input is int only
        try:
            word_pick_num = int(input('Index :'))
            break
        except:
            print("whole numbers only !")
    path = input("enter Path:") #user input text file path containing words - '/py/words.txt'
    MAX_TRIES = 6 # number of turns in the game
    count = 1 #counts the number of turns that was played
    turns_left_counter = MAX_TRIES #turn counter for user display
    secret_word = choose_word(path, word_pick_num)#the word that has to be gueesd inmported from file by a function
    history = [] #empty list to populate the guessed letters
    picture_count = 1 #turn counter for the hangman picture
    print('\n')
    print('You are allowd',CBlue,MAX_TRIES,CBlue_END, 'turns')#display of allowd turns
    show_hidden_word(secret_word, history)#function creates blank undescores for every letter in seceret word
    print('\x1b[0;30;44m' + ")()()()()()()()()()()()()()()()()()()()()" + '\x1b[0m')
    print('\n')
    picture(picture_count)#the hangman picture first initial state
    print(CYel, " ".join(new_word).upper(), CYel_END)#print list created by 'show_hidden_word' function.






    while count < MAX_TRIES + 1:#while loop to keep asking for input up to max turns allowed.

        letter_guessed = input('Enter Letter: ')#ask user to input a letter

        if is_valid_input(letter_guessed,history) and letter_guessed in secret_word or letter_guessed in history:#if statment makes sure turn is not added nor updated
            try_update_letter_guessed(letter_guessed, history)
            show_hidden_word(secret_word, history)
            picture(picture_count)#prints hangman without any change


        elif is_valid_input(letter_guessed,history):#if worng but valid answer
            try_update_letter_guessed(letter_guessed,history)
            show_hidden_word(secret_word, history)
            count += 1 #adds one count to the turns played
            turns_left_counter -= 1 #reduces number of turns left
            print(CBlue,"You have", turns_left_counter, "left to try",CBlue_END)
            picture_count += 1#adds one count to the hangman picture
            picture(picture_count)

        else: #in case input is invalid
            print(CRED,"Invalid input - Try again !",CRED_END)
            picture(count)

        if check_win(secret_word, history): #breaks the while loop if user guesses all letters in word
            print(CYel,'YOU WIN!', 'The word is',CRED, " ".join(new_word).upper(),CRED_END,CYel_END)
            break

        print(CYel," ".join(new_word).upper(),CYel_END)

    if count == MAX_TRIES + 1:#if all turns played and no win it prints message to user
       print('\x1b[0;30;44m' + " -> GAME OVER  - OuT Of GUESSES  (you killed the Stick Man)" + '\x1b[0m')

if __name__ == "__main__":
    main()

