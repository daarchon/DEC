#Lib for Encrypd/Decrypt functions

import string

#Cezar
def encrypt_c(key, text):

    return encrypted_text
    
def decrypt_c(key, text):

    return decrypted_text
#Hofmann
def encrypt_h(key, text):

    return encrypted_text
    
def decrypt_h(key, text):

    return decrypted_text

#Alphabet
def alphanet_autodetect(string_to_detect):
#Try to avtomaticly key creafte. Input string samle to analyze.
#Out string - key    
    detected_alphabet = ''
    whitesp = False
    lowerc = False
    upperc = False
    digit = False
    punct = False
#    for i in range(0, len(string.whitespace)):
#        if string.whitespace[i] in string_to_detect:
    if ' ' in string_to_detect:
            whitesp = True
    
    for i in range(0, len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] in string_to_detect:
            lowerc = True
            
    for i in range(0, len(string.ascii_uppercase)):
        if string.ascii_uppercase[i] in string_to_detect:
            upperc = True

    for i in range(0, len(string.digits)):
        if string.digits[i] in string_to_detect:
            #detected_alphabet += string.digets
            digit = True
            
    for i in range(0, len(string.punctuation)):
        if string.punctuation[i] in string_to_detect:
            punct = True

    if whitesp:
        print('Detect whitespace. Onle SPACE added')
        detected_alphabet += ' ' #string.whitespace
        
    if lowerc:
        print('Detect lowercase')
        detected_alphabet += string.ascii_lowercase
        
    if upperc:
        print('Detect uppercase')
        detected_alphabet += string.ascii_uppercase
    
    if digit:
        print('Detect digits')
        detected_alphabet += string.digits
           
    if punct:
        print('Detect punctution. Only ",.:;" added')
        detected_alphabet += ',.:;' #string.punctuation
    print('Final alphabet : {0}'.format(detected_alphabet)), 
    print('Length = {0}'.format(len(detected_alphabet)))
    
    return detected_alphabet
    
def alphabet_manual():
    # Forming alphabet in string s

    s = ''
    print('Now defining alphabet:')

    if input('Add whitespace(yes/no only space)?:') in ACC:
        s = s + string.whitespace
    else:
        s = s + string.whitespace[0] #only space added 
    print('Alphabet: {0}'.format(s))

    if input('Add lowercase(yes/no)?:') in ACC:
        s = s + string.ascii_lowercase
    print('Alphabet: {0}'.format(s))

    if input('Add uppercase(yes/no)?:') in ACC:
        s = s + string.ascii_uppercase
    print('Alphabet: {0}'.format(s))

    if input('Add digits(yes/no)?:') in ACC:
        s = s + string.digits
    print('Alphabet: {0}'.format(s))

    if input('Add punctuation(yes/no)?:') in ACC:
        s = s + '.,:' #string.punctuation ##not full define
    print('Alphabet: {0}'.format(s))

    print('END forming alphabet.')
    
    return s # Forming alphabet in string s

inp = input('Input test Alphabet: ')
alphanet_autodetect(inp)
