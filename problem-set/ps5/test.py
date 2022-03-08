import string

class PhraseTrigger():

  def __init__(self, phrase):
    self.phrase = phrase.lower().strip()

  def is_phrase_in(self, text):
    """
    Removes all the punctuations from a sentence and if phrase matches text, return True. Else False.
    """
    result = False

    cleanText = text.lower()

    for punctuation in string.punctuation:

      if punctuation in cleanText:
        cleanText = cleanText.replace(punctuation, " ")

    # return " ".join(cleanText.split())

    textList = cleanText.split()
    # print(textList)

    phraseList = self.phrase.split()
    # print(phraseList)

    phraseIndexFound = []
    phraseFoundCount = 0

    for phraseWord in phraseList:
      i = 0
      while i < len(textList):

        if phraseWord == textList[i]:
          phraseFoundCount += 1
          phraseIndexFound.append(i)

        i += 1

    if len(phraseIndexFound) == len(phraseList) and len(phraseIndexFound) > 0:

      # print(phraseIndexFound)

      if len(phraseIndexFound) == 1:
        result = True
      else:
        if phraseIndexFound[-1] == max(phraseIndexFound):

          gotIndex = None
          resultsList = []
          for index in phraseIndexFound:
            if gotIndex == None:
              gotIndex = index
            else:
              
              if index - gotIndex == 1:
                resultsList.append(True)
              else:
                resultsList.append(False)

              gotIndex = index

          if False in resultsList:
            result = False
          else:
            result = True

    # print(result)
    # print("------\n")
    return result

# print(string.punctuation)
testPhrase = PhraseTrigger("Purple Cow")
# Pass
print("---Pass---")
testPhrase.is_phrase_in("PURPLE COW")
testPhrase.is_phrase_in("The purple cow is soft and cuddly.")
testPhrase.is_phrase_in("The farmer owns a really PURPLE cow.")
testPhrase.is_phrase_in("Purple!!! Cow!!!")
testPhrase.is_phrase_in("purple@#$%cow")
testPhrase.is_phrase_in("Did you see a purple    cow?")

# Fail
print("\n---Fail---")
testPhrase.is_phrase_in("Purple cows are cool!")
testPhrase.is_phrase_in("The purple blob over there is a cow.")
testPhrase.is_phrase_in("How now brown cow.")
testPhrase.is_phrase_in("Cow!!! Purple!!!")
testPhrase.is_phrase_in("purplecowpurplecowpurplecow")

