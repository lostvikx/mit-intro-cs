# Problem Set 2, hangman.py
# Name: Vikram Singh Negi
# Collaborators: None
# Time spent: 2:30 hrs

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
  """
  Returns a list of valid words. Words are strings of lowercase letters.
  
  Depending on the size of the word list, this function may
  take a while to finish.
  """
  print("Loading word list from file...")
  # inFile: file
  inFile = open(WORDLIST_FILENAME, 'r')
  # line: string
  line = inFile.readline()
  # wordlist: list of strings
  wordlist = line.split()
  print("  ", len(wordlist), "words loaded.")
  return wordlist



def choose_word(wordlist):
  """
  wordlist (list): list of words (strings)
  
  Returns a word from wordlist at random
  """
  return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
  letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
  returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
  '''

  output = True

  for char in secret_word:

    if not char in letters_guessed:
      output = False
      break

  return output

  # num_check = 0

  # for letter in letters_guessed:
  #   for char in secret_word:
  #     if letter == char:
  #       num_check += 1
  #       # break  # Really important

  # if num_check == len(secret_word):
  #   return True
  # else:
  #   return False

# print(is_word_guessed("apple", ["a", "b", "p", "l", "e"]))



def get_guessed_word(secret_word, letters_guessed):
  '''
  secret_word: string, the word the user is guessing
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
  '''

  word_arr = list()

  for char in secret_word:
    word_arr.append(char)
  
  for i in range(len(secret_word)):

    if not secret_word[i] in letters_guessed:

      word_arr[i] = "_ "

  # return "".join(word_arr)  # Easy way out!

  output_str = ""

  for char in word_arr:
    output_str += char

  return output_str

# print(get_guessed_word("apple", ["p", "e", "q", "v"]))



def get_available_letters(letters_guessed):
  '''
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: string (of letters), comprised of letters that represents which letters have not
    yet been guessed.
  '''
  all_lowercase_letters = string.ascii_lowercase
  output_letters = ""

  for char in all_lowercase_letters:

    if not char in letters_guessed:
      output_letters += char
  
  return output_letters


# print(
#   get_available_letters(['e', 'i', 'k', 'p', 'r', 's']))
  

def hangman(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses

  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Remember to make
    sure that the user puts in a letter!
  
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
  
  Follows the other limitations detailed in the problem write-up.
  '''
  print("Welcome to the game Hangman!")
  print(
    f"I am thinking of a word that is {len(secret_word)} letters long.")
  print("You have 3 warnings left.")


  line = "-"*13
  print(line)

  guesses_left = 6
  guesses = []
  warnings_left = 3
  warn = "warnings"

  while guesses_left > 0:

    # Initial headers
    print(f"You have {guesses_left} guesses left.")
    print(f"Available letters: {get_available_letters(guesses)}")

    # Lowercase the letter guessed
    guess = input("Please guess a letter: ").lower()

    # If input letter is not an alpha
    if not str.isalpha(guess):

      # Init warnings_left = 3
      warnings_left -= 1

      # Considering this
      if warnings_left < 0:
        guesses_left -= 1
        print(
          f"Oops! That is not a valid letter. You have no warnings left: {get_guessed_word(secret_word, guesses)}")
        
        print(line)
        continue
        
      # Fixing plural
      if warnings_left == 1:
        warn = "warning"

      print(
        f"Oops! That is not a valid letter. You have {warnings_left} {warn} left: {get_guessed_word(secret_word, guesses)}")

      print(line)
      continue

    # If already guessed.
    if guess in guesses:
      warnings_left -= 1

      if warnings_left >= 0:

        print(
          f"Oops! You've already guessed that letter. You have {warnings_left} {warn} left: {get_guessed_word(secret_word, guesses)}")
        print(line)
      else:
        guesses_left -= 1
        print(
          f"Oops! You've already guessed that letter. You have no warnings left: {get_guessed_word(secret_word, guesses)}")
        print(line)

      continue

    guesses.append(guess)

    if guess in secret_word:
      print(
        f"Good guess: {get_guessed_word(secret_word, guesses)}")
      
      # If correct ans, no guesses were lost.
      guesses_left += 1
    else:
      # Letter not in word
      print(
        f"Oops! That letter is not in my word: {get_guessed_word(secret_word, guesses)}")

      vowels = "aeiou"
      # User guess was a vowel, double penalty. 
      if guess in vowels:
        guesses_left -= 1

    print(line)

    # Won the game!
    if is_word_guessed(secret_word, guesses):
      print("Congratulations, you won!")

      unique_letters = []
      for char in secret_word:
        if not char in unique_letters:
          unique_letters.append(char)

      score = (guesses_left - 1) * len(unique_letters)

      print(f"Your total score for this game is: {score}")
      break

    guesses_left -= 1

  # Lost the game :(
  if not is_word_guessed(secret_word, guesses):
    print(
      f"Sorry, you ran out of guesses. The word was {secret_word}.")

# hangman("regrets")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

def rm_underscore(my_word):
  """
  my_word: string with "_ " characters, current guess of the secret word

  info: replaces "_ " with "_" in a string

  returns: my_word with "_"
  """
  word = ""
  for char in my_word:
    word += char.strip()

  return word



def match_with_gaps(my_word, other_word):
  '''
  my_word: string with _ characters, current guess of secret word
  other_word: string, regular English word
  returns: boolean, True if all the actual letters of my_word match the 
      corresponding letters of other_word, or the letter is the special symbol
      _ , and my_word and other_word are of the same length;
      False otherwise: 
  '''

  result = False
  word = rm_underscore(my_word)

  # If the two strings don't have the same length, don't continue.
  if not len(word) == len(other_word):
    return result

  # Important to check if the characters guessed are not in the other_word as _
  alpha_equal_pass = 0

  for i in range(len(word)):
    # Declare char as the word character.
    char = word[i]

    # It char not equal to _
    if char != "_":
      # Check if its equal with other_word letter at postion i.
      if char == other_word[i]:
        alpha_equal_pass += 1
    else:
      # The _
      # The other_word letter should not be repeated in word, if an alpha is guessed correctly, all characters are revealed.
      if not other_word[i] in word:
        alpha_equal_pass += 1
  
  # True that!
  if alpha_equal_pass == len(word):
    result = True
  
  return result
  
# print(match_with_gaps("t_ st_ ", "taste"))



def show_possible_matches(my_word):
  '''
  my_word: string with _ characters, current guess of secret word
  returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

  '''
  # # Regex solution
  # result = ""
  # word = rm_underscore(my_word)

  # reg_str = ""
  # for char in word:
  #   if char == "_":
  #     reg_str += "\w"
  #   else:
  #     reg_str += char
  
  # for word in wordlist:
  #   if bool(re.search(f"^{reg_str}$", word.strip())):
  #     result += word + " "

  # if len(result) == 0:
  #   print("No matches found")
  # else:
  #   print(result.rstrip())

  # Just do it!
  result = ""

  for word in wordlist:
    if match_with_gaps(my_word, word):
      result += word.strip() + " "

  if len(result) == 0:
    print("No matches found")
  else:
    print(result.rstrip())

# show_possible_matches("te_ _ t_ r")


def hangman_with_hints(secret_word):
  '''
  secret_word: string, the secret word to guess.
  
  Starts up an interactive game of Hangman.
  
  * At the start of the game, let the user know how many 
    letters the secret_word contains and how many guesses s/he starts with.
    
  * The user should start with 6 guesses
  
  * Before each round, you should display to the user how many guesses
    s/he has left and the letters that the user has not yet guessed.
  
  * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    
  * The user should receive feedback immediately after each guess 
    about whether their guess appears in the computer's word.

  * After each guess, you should display to the user the 
    partially guessed word so far.
    
  * If the guess is the symbol *, print out all words in wordlist that
    matches the current guessed word. 
  
  Follows the other limitations detailed in the problem write-up.
  '''
  print("Welcome to the game Hangman!")
  print(
    f"I am thinking of a word that is {len(secret_word)} letters long.")
  print("You have 3 warnings left.")

  line = "-"*13
  print(line)

  guesses_left = 6
  guesses = []
  warnings_left = 3
  warn = "warnings"

  while guesses_left > 0:

    # Initial headers
    print(f"You have {guesses_left} guesses left.")
    print(f"Available letters: {get_available_letters(guesses)}")

    # Lowercase the letter guessed
    guess = input("Please guess a letter: ").lower()

    # If input letter is not an alpha
    if not str.isalpha(guess):

      # * to show possible matches
      # I have tried the game, this is a really broken feature.
      if guess == "*":
        print("Possible word matches are:")
        show_possible_matches(get_guessed_word(secret_word, guesses))
        print(line)
        continue

      # Init warnings_left = 3
      warnings_left -= 1

      # Considering this
      if warnings_left < 0:
        guesses_left -= 1
        print(
          f"Oops! That is not a valid letter. You have no warnings left: {get_guessed_word(secret_word, guesses)}")

        print(line)
        continue

      # Fixing plural
      if warnings_left == 1:
        warn = "warning"

      print(
        f"Oops! That is not a valid letter. You have {warnings_left} {warn} left: {get_guessed_word(secret_word, guesses)}")

      print(line)
      continue

    # If already guessed.
    if guess in guesses:
      warnings_left -= 1

      if warnings_left >= 0:

        print(
          f"Oops! You've already guessed that letter. You have {warnings_left} {warn} left: {get_guessed_word(secret_word, guesses)}")
        print(line)
      else:
        guesses_left -= 1
        print(
          f"Oops! You've already guessed that letter. You have no warnings left: {get_guessed_word(secret_word, guesses)}")
        print(line)

      continue

    guesses.append(guess)

    if guess in secret_word:
      print(
        f"Good guess: {get_guessed_word(secret_word, guesses)}")

      # If correct ans, no guesses were lost.
      guesses_left += 1
    else:
      # Letter not in word
      print(
          f"Oops! That letter is not in my word: {get_guessed_word(secret_word, guesses)}")

      vowels = "aeiou"
      # User guess was a vowel, double penalty.
      if guess in vowels:
        guesses_left -= 1

    print(line)

    # Won the game!
    if is_word_guessed(secret_word, guesses):
      print("Congratulations, you won!")

      unique_letters = []
      for char in secret_word:
        if not char in unique_letters:
          unique_letters.append(char)

      score = (guesses_left - 1) * len(unique_letters)

      print(f"Your total score for this game is: {score}")
      break

    guesses_left -= 1

  # Lost the game :(
  if not is_word_guessed(secret_word, guesses):
    print(
      f"Sorry, you ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
  # pass

  # To test part 2, comment out the pass line above and
  # uncomment the following two lines.
  
  # secret_word = choose_word(wordlist)
  # hangman(secret_word)

###############
  
  # To test part 3 re-comment out the above lines and 
  # uncomment the following two lines. 
  
  secret_word = choose_word(wordlist)
  hangman_with_hints(secret_word)
