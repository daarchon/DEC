#Lib for Encrypd/Decrypt functions

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

