###########################

# 1- In Robert McCloskey’s book Make Way for Ducklings, the names
#of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and
#Quack. Write a loop that will output these names in order.

###########################
prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
    if p == 'O' or p == 'Q':
        print(p + "u" + suffix)
    else:
        print(p + suffix)
###########################

# 2- Print out a neatly formatted multiplication table, up to 12 x 12

###########################
def draw_table(n):
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            result = str(r * c)
            if len(result) == 2:
                end = "  "
            elif len(result) == 3:
                end = " "
            else:
                end = "   "
            print(result, end = end)
        print()


draw_table(12)
##########################

# 3 - Write a function reverse that receives a string argument, and returns a
#reversed version of the string

##########################
def reverse(text):
    backwards = ''
    for char in text:
           backwards = char + backwards
    return backwards
###########################
# tests and expected results
def main():
    print(reverse("happy")) # "yppah"
    print(reverse("Python")) # "nohtyP"
    print(reverse(""))  # ""

main()
###########################

# 4 - Write a function that recognizes palindromes, and returns True or False.

###########################
def reverse(text):
    reverse = ''
    for char in text:
           reverse = char + reverse
    return reverse

def is_palindrome(text):
       return reverse(text) == text
###########################
# tests and expected results
def main():
    print(is_palindrome('abba')) # True
    print(is_palindrome('abab')) # False
    print(is_palindrome('straw warts')) # True
    print(is_palindrome('a')) #True
    print(is_palindrome('')) # True

main()
###########################

# 5 - Write a function that removes the first occurrence of a string
#from another string.

############################
def remove(substr,theStr):
    return theStr.replace(substr, '', 1)
#############################
#tests and expected results
remove('an', 'banana') # 'bana'
remove('cyc', 'bicycle') #'bile'
remove('iss', 'Mississippi') # 'Missippi'
remove('egg', 'bicycle') #'bicycle'
##############################

# 6 - Write a function that removes all occurrences of a string from
# another string.

##############################
def remove_all(substr,theStr):
    return theStr.replace(substr, '')
##############################
# tests and expected results
remove_all('an', 'banana') # 'ba'
remove_all('cyc', 'bicycle') # 'bile'
remove_all('iss', 'Mississippi') # 'Mippi'
remove_all('eggs', 'bicycle') #'bicycle'
###############################

# 7 - Write a function that implements a substitution cipher. In a substitution
#cipher one letter is substituted for another to garble the message.

###############################
def encrypt(message, cipher):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    enc_message = ''
    for i in range(len(message)):
        if message[i] == " ":
            enc_message += message[i]
        else:
            currentidx = alpha.find(message[i])
            enc_message += cipher[currentidx]
    return enc_message

cipher = "qwertyuiopasdfghjklzxcvbnm"
################################

# 8 - Write a function that decrypts the message from the previous exercise.
#It should also take two parameters. The encrypted message, and the
#mixed up alphabet. The function should return a string that is the same as
#the original unencrypted message.

################################
def decrypt(encrypted, cipher):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for char in encrypted:
        if char == " ":
            decrypted += char
        else:
            index = cipher.find(char)
            decrypted += alpha[index]
    return decrypted

encrypted = sub_cipher("here is my secret message", cipher)
print(encrypted)

decrypted = decrypt(encrypted, cipher)
print(decrypted)
################################

################################
#9 - Write a function called removeDups that takes a string and
#creates a new string by only adding those characters that are not
#already present. In other words, there will never be a duplicate
#letter added to the new string.

##############################
def removeDups(astring):
    newstr = ''
    for i in range(len(astring)):
        if newstr.find(astring[i]) == -1:
            newstr += astring[i]
    return newstr
###############################
#tests and expected results
removeDups("mississippi") #misp
removeDups("bookkeeping") #bokeping
################################

# 10- Write a function called rot13 that uses the Caesar cipher to
#encrypt a message by a rotation of 13.

################################
def rot13(mess):
    encrypt_mess = ''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(mess)):
        if mess[i].isalpha() == False:
            encrypt_mess += mess[i]
        else:
            index = alpha.find(mess[i])
            encrypt_mess += alpha[(index + 13) % 26]
    return encrypt_mess
#################################
# tests and expected outcomes
print(rot13('abcde')) # nopqr
print(rot13('nopqr')) # abcde
print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
##################################
