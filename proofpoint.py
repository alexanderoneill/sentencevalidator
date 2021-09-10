
def sentenceCheck(sentence):
  """
  Returns dictionary detailing validity of sentence according to given
  criteria of a 'valid sentence': First character must be capital letter, must 
  contain an even number of quotation marks, final character must be a period, 
  periods must not appear at any other point in the sentence, and any number 
  below 13 must be spelled out in words.
  Dictonary takes the form:
  {'capital': INT,
   'quotes': INT,
   'period': INT,
   'earlyperiods': INT,
   'numbers': INT}
  Where INT is either 0 or 1, 0 meaning invalid, 1 meaning valid
  """

  # Default conditions
  results = {
    "capital": 0, 
    "quotes": 0, 
    "period": 0, 
    "earlyperiods": 0, 
    "numbers" : 0
    }

  # Check first character is capital
  if sentence[0].isupper():
    results["capital"] = 1

  # Check if there is an even number of quotes by totalling number of quotes in 
  # sentence then checking if total is divisble by 2
  quotecount = 0
  for character in sentence:
    if character == '"':
      quotecount += 1
  if quotecount % 2 == 0:
    results["quotes"] = 1

  # Check if last character is a period
  if sentence[-1] == '.':
    results["period"] = 1

  # Check if any periods are present elsewhere other than final character
  if '.' not in sentence[:-1]:
    results["earlyperiods"] = 1

  # Check if any numbers under 13 are spelled out
  numstring = ""
  for i in range(len(sentence)):

    # Append character to string if digit
    if sentence[i].isdigit():
      numstring = numstring + str((sentence[i]))
      # End iteration if on final character in sentence
      if i == len(sentence)-1:
        break
      # Add comma to string if next character is not digit
      if not sentence[i+1].isdigit():
        numstring = numstring + ","

  
  if len(numstring) < 1: # If no numbers in sentence
    results["numbers"] = 1
  else:
    if numstring[-1] == "," : # Remove trailing comma if present
      numstring = numstring[:-1]
    numarray = (numstring.split(",")) # Convert to list
    # Check if any numbers found are under 13
    if any(int(num) < 13 for num in numarray):
      results["numbers"] = 0
    else:
      results["numbers"] = 1

  # Return results
  return results

# We put this in a while loop to allow the user to immediately test another
# sentence if desired, or to exit the program depending on input
using = "y"
fail_reason = ""
while using.lower() in ["y", "ye", "yes"]:
  sentence = str(input("Enter sentence to validate: "))
  results = sentenceCheck(sentence)

  # Give the user an in-depth explanation as to why the sentence is invalid
  if any(result < 1 for result in results.values()):
    if results["capital"] == 0:
      fail_reason = "first character must be a capital letter."
    elif results["quotes"] == 0:
      fail_reason = "must have an even number of quotation marks."
    elif results["period"] == 0:
      fail_reason = "final character must be a period."
    elif results["earlyperiods"] == 0:
      fail_reason = "periods must not appear mid-sentence."
    elif results["numbers"] == 0:
      fail_reason = "all numbers lesser than 13 must be spelled out fully."
    print("Sentence invalid, " + fail_reason)
  
  else:
    print("Sentence valid")
  
  using = str(input("Test another sentence? [y/n]: "))

# Below is code I used to test all given test cases quickly
"""
results = []
test_cases = [
  'The quick brown fox said "hello Mr lazy dog".',
  'The quick brown fox said hello Mr lazy dog.',
  'One lazy dog is too few, 13 is too many.',
  'One lazy dog is too few, thirteen is too many.',
  'The quick brown fox said "hello Mr. lazy dog".',
  'the quick brown dox said "hello Mr lazy dog".',
  '"The quick brown fox said "hello Mr lazy dog."',
  'One lazy dog is too few, 12 is too many.'
]
for case in test_cases:
  results.append(sentenceCheck(case))
if all(result == True for result in list(results)[0:3]) and all(
  result == False for result in list(results)[4:7]):
  print("Code successful")
else:
  print("Code unsuccessful")
"""