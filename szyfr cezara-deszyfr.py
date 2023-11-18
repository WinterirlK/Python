klucz = 3
tekst = input("podaj tekst do szyfrowania: ")
def szyfrowanie(tekst):
    global zaszyfrowany 
    zaszyfrowany =""
    for i in range(len(tekst)):
        if((ord(tekst[i])>122-klucz)):
            zaszyfrowany += chr((ord(tekst[i])) + klucz - 26)
        else:
            zaszyfrowany += chr((ord(tekst[i])) + klucz)
    print("zaszyfrowany wygląda tak:", zaszyfrowany)

def lamanie_szyfru(zaszyfrowany):
    global odszyfrowany 
    odszyfrowany =""
    kluc = klucz % 26
    for i in range(len(zaszyfrowany)):
        if (ord(zaszyfrowany[i]) - kluc < 97):
            odszyfrowany += chr(ord(zaszyfrowany[i]) - kluc + 26)
        else:
            odszyfrowany += chr(ord(zaszyfrowany[i]) - kluc)
    print("odszyfrowany wygląda tak:", odszyfrowany)

szyfrowanie(tekst)
lamanie_szyfru(zaszyfrowany)
