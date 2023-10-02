import string

def decrypt(message_crypte):
    caracteres = string.ascii_letters + string.punctuation + string.digits + " "
    message_decrypte = ""

    for lettre_crypte in message_crypte:
        if lettre_crypte in caracteres:
            index = caracteres.index(lettre_crypte)
            lettre_decryptee = caracteres[(index - 1) % len(caracteres)]
            message_decrypte += lettre_decryptee
        else:
            message_decrypte += lettre_crypte

    return message_decrypte

message_crypte = "Tbmvuadbawba"
message_decrypte = decrypt(message_crypte)
print(message_decrypte)