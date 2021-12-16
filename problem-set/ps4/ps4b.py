# Problem Set 4B
# Name: Vikram S. Negi
# Collaborators: None
# Time Spent: 02:30

import string
from copy import deepcopy

### HELPER CODE ###
def load_words(file_name):
  '''
  file_name (string): the name of the file containing 
  the list of words to load    

  Returns: a list of valid words. Words are strings of lowercase letters.

  Depending on the size of the word list, this function may
  take a while to finish.
  '''
  # print("Loading word list from file...")
  # inFile: file
  inFile = open(file_name, 'r')
  # wordlist: list of strings
  wordlist = []
  for line in inFile:
    wordlist.extend([word.lower() for word in line.split(' ')])
  # print("  ", len(wordlist), "words loaded.")
  return wordlist

def is_word(word_list, word):
  '''
  Determines if word is a valid word, ignoring
  capitalization and punctuation

  word_list (list): list of words in the dictionary.
  word (string): a possible word.

  Returns: True if word is in word_list, False otherwise

  Example:
  >>> is_word(word_list, 'bat') returns
  True
  >>> is_word(word_list, 'asdf') returns
  False
  '''
  word = word.lower()
  word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
  return word in word_list

def get_story_string():
  """
  Returns: a story in encrypted text.
  """
  f = open("story.txt", "r")
  story = str(f.read())
  f.close()

  return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
  def __init__(self, text):
    '''
    Initializes a Message object
            
    text (string): the message's text

    a Message object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    self.message_text = text
    self.valid_words = load_words(WORDLIST_FILENAME)

  def get_message_text(self):
    '''
    Used to safely access self.message_text outside of the class

    Returns: self.message_text
    '''
    return self.message_text

  def get_valid_words(self):
    '''
    Used to safely access a copy of self.valid_words outside of the class.
    This helps you avoid accidentally mutating class attributes.

    Returns: a COPY of self.valid_words
    '''
    return self.valid_words[:]

  def build_shift_dict(self, shift):
    '''
    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to a
    character shifted down the alphabet by the input shift. The dictionary
    should have 52 keys of all the uppercase letters and all the lowercase
    letters only.        

    shift (integer): the amount by which to shift every letter of the 
    alphabet. 0 <= shift < 26

    Returns: a dictionary mapping a letter (string) to 
              another letter (string). 
    '''
    assert shift >= 0 and shift < 26, "Can't shift more than 25 number!"

    all_alpha = [alpha for alpha in string.ascii_lowercase]

    mapped_alpha_dict = {}
    # print(all_alpha)
    for i, alpha in enumerate(all_alpha):
      mapped_alpha_dict[alpha] = all_alpha[(i+shift)%len(all_alpha)]

    return mapped_alpha_dict

  def apply_shift(self, shift):
    '''
    Applies the Caesar Cipher to self.message_text with the input shift.
    Creates a new string that is self.message_text shifted down the
    alphabet by some number of characters determined by the input shift        

    shift (integer): the shift with which to encrypt the message.
    0 <= shift < 26

    Returns: the message text (string) in which every character is shifted
          down the alphabet by the input shift
    '''
    shift_dict = self.build_shift_dict(shift)

    shifted_text = ""

    for alpha in self.message_text:
      upperCase = False
      if alpha in string.ascii_uppercase:
        alpha = alpha.lower()
        # print(alpha)
        upperCase = True
      try:
        changed_letter = shift_dict[alpha]
        if upperCase:
          changed_letter = changed_letter.upper()
        shifted_text += changed_letter
      except KeyError:
        shifted_text += alpha
      except:
        print("Something went wrong!")

    return shifted_text


# hello = Message("Hello, World!")
# print(hello.build_shift_dict(4))
# print(hello.apply_shift(4))
# print(hello.get_message_text())

class PlaintextMessage(Message):
  def __init__(self, text, shift):
    '''
    Initializes a PlaintextMessage object        

    text (string): the message's text
    shift (integer): the shift associated with this message

    A PlaintextMessage object inherits from Message and has five attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
        self.shift (integer, determined by input shift)
        self.encryption_dict (dictionary, built using shift)
        self.message_text_encrypted (string, created using shift)

    '''
    super().__init__(text)
    self.shift = shift
    self.encryption_dict = super().build_shift_dict(self.shift)
    self.message_text_encrypted = super().apply_shift(self.shift)

  def get_shift(self):
    '''
    Used to safely access self.shift outside of the class

    Returns: self.shift
    '''
    return self.shift

  def get_encryption_dict(self):
    '''
    Used to safely access a copy self.encryption_dict outside of the class

    Returns: a COPY of self.encryption_dict
    '''
    return deepcopy(self.encryption_dict)

  def get_message_text_encrypted(self):
    '''
    Used to safely access self.message_text_encrypted outside of the class

    Returns: self.message_text_encrypted
    '''
    return self.message_text_encrypted[:]

  def change_shift(self, shift):
    '''
    Changes self.shift of the PlaintextMessage and updates other 
    attributes determined by shift.        

    shift (integer): the new shift that should be associated with this message.
    0 <= shift < 26

    Returns: nothing
    '''
    self.shift = shift
    self.encryption_dict = Message.build_shift_dict(self.shift)
    self.message_text_encrypted = Message.apply_shift(self.shift)


class CiphertextMessage(Message):
  def __init__(self, text):
    '''
    Initializes a CiphertextMessage object
            
    text (string): the message's text

    a CiphertextMessage object has two attributes:
        self.message_text (string, determined by input text)
        self.valid_words (list, determined using helper function load_words)
    '''
    super().__init__(text)

  def decrypt_message(self):
    '''
    Decrypt self.message_text by trying every possible shift value
    and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift)
    on the message text. If s is the original shift value used to encrypt
    the message, then we would expect 26 - s to be the best shift value 
    for decrypting it.

    Note: if multiple shifts are equally good such that they all create 
    the maximum number of valid words, you may choose any of those shifts 
    (and their corresponding decrypted messages) to return

    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value
    '''
    # Rule: s >= 0 and s < 26
    # List of tuples (guess_shift, score)
    track_best = []

    # s is a guess of shift int
    for s in range(26):
      decipher_message_list = super().apply_shift(s).split()
      score = 0

      for word in decipher_message_list:
        if is_word(self.valid_words, word):
          score += 1

      track_best.append((s, score))

    # print(sorted(track_best, key=lambda x:x[1], reverse=True))
    track_best.sort(key=lambda x: x[1], reverse=True)
    best_guess = track_best[0][0]

    # Best shift value to decrypt the message and the message probably.
    return (best_guess, super().apply_shift(best_guess))

# test1 = Message("This is the greatest day of me life!")
# encrypted_message = test1.apply_shift(19)
# cipher = CiphertextMessage(encrypted_message)
# print(cipher.decrypt_message())

if __name__ == '__main__':

  #TODO: WRITE YOUR TEST CASES HERE
  #Test case (PlaintextMessage)
  plaintext1 = PlaintextMessage('hello', 2)
  print("\n---PlainTest 1---")
  print('Expected Output: jgnnq')
  print('Actual Output:', plaintext1.get_message_text_encrypted())

  plaintext2 = PlaintextMessage('Hello World, this is me Vikram!', 12)
  print("\n---PlainTest 2---")
  print('Expected Output: Tqxxa Iadxp, ftue ue yq Huwdmy!')
  output2 = plaintext2.get_message_text_encrypted()
  print('Actual Output:', output2)

  print("\n---PlainTest 3---")
  plaintext3 = PlaintextMessage('Would you like to go on a date with me?', 17)
  print('Expected Output: Nflcu pfl czbv kf xf fe r urkv nzky dv?')
  output3 = plaintext3.get_message_text_encrypted()
  print('Actual Output:', output3)

  #Test case (CiphertextMessage)
  ciphertext1 = CiphertextMessage('jgnnq')
  print("\n---CiperTest 1---")
  print('Expected Output:', (24, 'hello'))
  print('Actual Output:', ciphertext1.decrypt_message())

  ciphertext2 = CiphertextMessage(output2)
  print("\n---CiperTest 2---")
  print('Expected Output:', (26-12, 'Hello World, this is me Vikram!'))
  print('Actual Output:', ciphertext2.decrypt_message())

  ciphertext3 = CiphertextMessage(output3)
  print("\n---CiperTest 3---")
  print('Expected Output:', (26-17, 'Would you like to go on a date with me?'))
  print('Actual Output:', ciphertext3.decrypt_message(), end="\n\n")


  #TODO: best shift value and unencrypted story 
  story_text = get_story_string()
  cipherStory = CiphertextMessage(story_text)
  print("Output:", cipherStory.decrypt_message())