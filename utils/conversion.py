# function permet de transformer un char en int
def conversion_int(x):
    if len(x) > 1:
        return 0
    else:
        x = x.lower()
        output = ord(x) - 96 #ord renvoie la valeur ASCII d'un caractère
        return output

# function permet de transformer un int en str
def conversion_str(x):
    x = x + 96
    output = chr(x)
    output = output.upper()
    return output
