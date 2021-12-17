# Problem Set 4C
# Name: Vikram S. Negi
# Collaborators: None
# Time Spent: 02:00

import string
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
  def __init__(self, text):
    '''
    Initializes a SubMessage object
        
    text (string): the message's text

    A SubMessage object has two attributes:
    self.message_text (string, determined by input text)
    self.valid_words (list, determined using helper function load_words)
    '''
    self.message_text = text
    self.valid_words = load_words("./words.txt")

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

  def build_transpose_dict(self, vowels_permutation) -> dict:
    '''
    vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

    Creates a dictionary that can be used to apply a cipher to a letter.
    The dictionary maps every uppercase and lowercase letter to an
    uppercase and lowercase letter, respectively. Vowels are shuffled 
    according to vowels_permutation. The first letter in vowels_permutation 
    corresponds to a, the second to e, and so on in the order a, e, i, o, u.
    The consonants remain the same. The dictionary should have 52 
    keys of all the uppercase letters and all the lowercase letters.

    Example: When input "eaiuo":
    Mapping is a->e, e->a, i->i, o->u, u->o
    and "Hello World!" maps to "Hallu Wurld!"

    Returns: a dictionary mapping a letter (string) to 
            another letter (string). 
    '''

    sub_trans_dict = {}
    vowels = "aeiou"

    for i, alpha in enumerate([a for a in vowels]):
      sub_trans_dict[alpha] = vowels_permutation[i]

    for letter in string.ascii_lowercase:
      if not letter in vowels:
        sub_trans_dict[letter] = letter

    return sub_trans_dict


  def apply_transpose(self, transpose_dict):
    '''
    transpose_dict (dict): a transpose dictionary

    Returns: an encrypted version of the message text, based 
    on the dictionary
    '''

    encrypted_message = ""

    for letter in self.message_text:
      upper = False

      if letter in string.ascii_uppercase:
        # print(string.ascii_uppercase, "Letter:", letter)
        # breakpoint()
        upper = True

      try:
        change_letter = transpose_dict[letter.lower()]
        
        if upper:
          encrypted_message += change_letter.upper()
        else:
          encrypted_message += change_letter
      except KeyError:
        encrypted_message += letter
      except:
        print("Something went wrong!")

    return encrypted_message


class EncryptedSubMessage(SubMessage):
  def __init__(self, text):
    '''
    Initializes an EncryptedSubMessage object

    text (string): the encrypted message text

    An EncryptedSubMessage object inherits from SubMessage and has two attributes:
    self.message_text (string, determined by input text)
    self.valid_words (list, determined using helper function load_words)
    '''
    super().__init__(text)

  def decrypt_message(self):
    '''
    Attempt to decrypt the encrypted message 

    Idea is to go through each permutation of the vowels and test it
    on the encrypted message. For each permutation, check how many
    words in the decrypted text are valid English words, and return
    the decrypted message with the most English words.

    If no good permutations are found (i.e. no permutations result in 
    at least 1 valid word), return the original string. If there are
    multiple permutations that yield the maximum number of words, return any
    one of them.

    Returns: the best decrypted message    

    Hint: use your function from Part 4A
    '''
    # List of (guess:str, score)
    # score == no. of valid words
    track_best_guess = []

    for sequence in get_permutations("aeiou"):
      trans_dict = super().build_transpose_dict(sequence)
      decrypted_message = super().apply_transpose(trans_dict)

      score = 0
      for word in decrypted_message.split(" "):
        if is_word(self.valid_words, word):
          score += 1
      
      track_best_guess.append((decrypted_message, score, sequence))

    track_best_guess.sort(key=lambda x: x[1], reverse=True)

    # return track_best_guess # For Debugging
    if track_best_guess[0][1] == 0:
      return self.message_text
    else:
      return track_best_guess[0][0]




if __name__ == '__main__':

# Example test case
  # message = SubMessage("Hello World!")
  # permutation = "eaiuo"
  # enc_dict = message.build_transpose_dict(permutation)
  # print("Original message:", message.get_message_text(), "Permutation:", permutation)
  # print("Expected encryption:", "Hallu Wurld!")
  # print("Actual encryption:", message.apply_transpose(enc_dict))
  # enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
  # print("Decrypted message:", enc_message.decrypt_message())

  #TODO: WRITE YOUR TEST CASES HERE
  # Test 1
  print("\n---SubMessage Test 1---")
  test_message1 = SubMessage("Anime is the greatest thing happened to humanity.")
  perm1 = "eioua"
  enc_dict1 = test_message1.build_transpose_dict(perm1)
  print(f"Original message: {test_message1.get_message_text()} Permutation: {perm1}")
  print("Expected encryption: Enomi os thi grietist thong heppinid tu hamenoty.")
  print(f"Actual encryption: {test_message1.apply_transpose(enc_dict1)}")
  print("\n---EncryptedSubMessage Test 1---")
  enc_mess = EncryptedSubMessage(test_message1.apply_transpose(enc_dict1))
  print(f"Decrypted message: {enc_mess.decrypt_message()}", end="\n\n")

  # Test 2
  print("\n---SubMessage Test 2---")
  test_message2 = SubMessage("To find something new, one must have the courage to lose sight of the shore.")
  perm2 = "uioae"
  enc_dict2 = test_message2.build_transpose_dict(perm2)
  print(f"Original message: {test_message2.get_message_text()} Permutation: {perm2}")
  print("Expected encryption: Ta fond samithong niw, ani mest huvi thi caerugi ta lasi soght af thi shari.")
  print(f"Actual encryption: {test_message2.apply_transpose(enc_dict2)}")
  print("\n---EncryptedSubMessage Test 2---")
  enc_mess = EncryptedSubMessage(test_message2.apply_transpose(enc_dict2))
  print(f"Decrypted message: {enc_mess.decrypt_message()}", end="\n\n")
