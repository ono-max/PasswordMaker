import string

alphabet = string.printable
alphabet_list = []
for i in alphabet:
    alphabet_list.append(i)

def encrypt(message,password):
    encryptedMessage = ''
    new = []
    index = 0
    for _ in range(len(message)):
        if index < len(password):
            new.append(password[index])
        else:
            index = 0
            new.append(password[index])
        index += 1
    for i in range(len(message)):
        FindMessage = message[i]
        FindPassword = new[i]
        for n in range(len(alphabet_list)):
            if alphabet_list[n] == FindMessage:
                indexMessage = n
        for c in range(len(alphabet_list)):
            if alphabet_list[c] == FindPassword:
                indexPassword = c
        encryptedMessage += alphabet_list[(indexMessage + indexPassword) % len(alphabet)]
    return encryptedMessage


def decrypt(message,password):
    decryptedMessage = ''
    new = []
    index = 0
    for _ in range(len(message)):
        if index < len(password):
            new.append(password[index])
        else:
            index = 0
            new.append(password[index])
        index += 1
    for i in range(len(message)):
        FindMessage = message[i]
        FindPassword = new[i]
        for n in range(len(alphabet_list)):
            if alphabet_list[n] == FindMessage:
                indexMessage = n
        for c in range(len(alphabet_list)):
            if alphabet_list[c] == FindPassword:
                indexPassword = c
        decryptedMessage += alphabet_list[(indexMessage - indexPassword) % len(alphabet)]
    return decryptedMessage



print(encrypt('This is my message','My#1Secret Password'))
print(decrypt(encrypt('This is my message','My#1Secret Password'),'My#1Secret Password'))
