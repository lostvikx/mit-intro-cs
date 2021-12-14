# Problem Set 4A
# Name: Vikram S. Negi
# Collaborators: None
# Time Spent: 03:00 hrs

def get_permutations(sequence):
  '''
  Enumerate all permutations of a given string

  sequence (string): an arbitrary string to permute. Assume that it is a
  non-empty string.  

  You MUST use recursion for this part. Non-recursive solutions will not be
  accepted.

  Returns: a list of all permutations of sequence

  Example:
  >>> get_permutations('abc')
  ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

  Note: depending on your implementation, you may return the permutations in
  a different order than what is listed here.
  '''

  if len(sequence) == 1:
    return [sequence]
  else:
    first_letter = sequence[0]
    # Last scope would get us the last letter.
    rest_letters = get_permutations(sequence[1:])
    # Final Output
    result = []
    for alpha in rest_letters:
      # These helped to visualize the output values.
      # rest_letters
      # ["bc", "cb"]
      # ["c"]
      add_letter_times = len(alpha) + 1
      i = 0
      while add_letter_times > i:
        # These helped to visualize the output values.
        # Expected output
        # "abcd", "bcd", "bcad", "bcda"
        # "abc", "bac", "bca"
        # "ac", "ca"

        # Nothing is impossible!
        if i == 0:
          new_word = first_letter + alpha
        elif i == len(alpha):
          new_word = alpha + first_letter
        else:
          new_word = alpha[:i] + first_letter + alpha[i:]

        # Sweet debug!
        # print(new_word)

        # Makes sure every arrangement is unique.
        if not new_word in result:
          result.append(new_word)

        i += 1

    return result


if __name__ == '__main__':

#   example_input = 'abc'
#   all_possible_arrangements = get_permutations(example_input)
#   print('Input:', example_input)
# #  print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#   print('Actual Output:', all_possible_arrangements)
#   print("Output Length:", len(all_possible_arrangements))
  
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

  def perm_test(words:list) -> None:

    for i, word in enumerate(words):
      all_arrangements = get_permutations(word)
      print(f"\n---Test #{i+1}---")
      print("Input:", word)
      print("Output:", all_arrangements)
      print("Output Lenght:", len(all_arrangements))

  perm_test(["cat", "doge", "free", "props"])