import random
import string
# A function do shuffle all the characters of a string
def shuffle(string):
    templiist = list(string)
    random.shuffle(templiist)
    return ''.join(templiist)

# Main program starts here
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
lowercaseLetter3=chr(random.randint(97,122))
lowercaseLetter4=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
digit3=chr(random.randint(48,57))
digit4=chr(random.randint(48,57))
punctuationSign1=chr(random.randint(33,64))
punctuationSign2=chr(random.randint(33,64))
punctuationSign3=chr(random.randint(123,126))
punctuationSign4=chr(random.randint(91,96))


# Generate password using all the characters in random order
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseLetter1 + lowercaseLetter2 + lowercaseLetter3 + lowercaseLetter4 + digit1 + digit2 + digit3 + digit4 + punctuationSign1 + punctuationSign2 + punctuationSign3 + punctuationSign4
password = shuffle(password)

# Output
print(password)