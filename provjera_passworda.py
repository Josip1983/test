lozinka = input("Unesite password")

def provjera_password(password) :
    if (len(password))<8 :
        print(f"Pogresan unos lozinke")
    else :
        print("Unesena lozinka je prihvacena")

provjera_password(lozinka)

