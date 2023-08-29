import random as r


def password_generate(long = 16):


    Tokens = [ "a","b","c","d","e","f","g","k","l","m","n","h","x","z","y","p","i","o","u","j","s","w","v","r","t","q","1","2","3","4","5","6","7","8","9",".",",","/","?","*","-","_","^","#","!","q",
                "A","B","C","D","E","F","G","K","L","M","N","H","X","Z","Y","P","I","O","U","J","S","W","V","R","T","Q" ]


    Selected_tokens = []
    Password= ''

    for count in range(int(long)):

        Selected_tokens.append(r.choices(Tokens))


    for token in Selected_tokens:
        Password += token[0]

    return Password
