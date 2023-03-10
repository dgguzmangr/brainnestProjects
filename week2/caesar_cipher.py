"""
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by a certain number of places in the alphabet. We call the length of shift the key. For example, if the key is 3, then A becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.
When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
"""

#1. Create a input for message
#1. Create a input for key (number of spaces that letter is ogint to change)
#3. Create an empty string where the encryted message is going to be stored
#4. Fist if conditional. If the character is a letter in the alphabet happens an nested condition. Else the character is added to the message_encryted string.

def caesarCipher(message, key, mode):

    if message == message.upper():
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        alphabet = "abcdefghijklmnopqrstuvwxyz"

    message_encrypted = ""

    for letter in message:
        if letter in alphabet:
            if mode == "e":
                message_encrypted += alphabet[(alphabet.index(letter)+key%(len(alphabet)))]
            elif mode == "d":
                message_encrypted += alphabet[(alphabet.index(letter)-key%(len(alphabet)))]
        else:
            message_encrypted +=letter

    return message_encrypted

mode = input("Do you want to (e)ncrypt or (d)ecrypt?")
message = input("Entrer the message to encrypt: ")
key = int(input("Please enter the key (0 to 25) to use: "))

print(caesarCipher(message, key, mode))