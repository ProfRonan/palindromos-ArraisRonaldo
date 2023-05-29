import string as outronome


def is_palindrome(string: str) -> bool:
    limpa = string.lower()
    limpa = limpa.replace(" ", "")
    for char in string.lower():
        if char in outronome.punctuation:
            limpa = limpa.replace(char, "")

    var = limpa.lower()
    var = var[::-1]
    print(var)
    print(limpa)
    if var == limpa:
        return True
    return False
