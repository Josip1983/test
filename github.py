class Ucenik() :
    def __init__(self, ime, godine, uspjeh, karakter) :
        self.ime=ime
        self.godine=godine
        self.uspjeh=uspjeh
        self.karakter=karakter

ucenik1=Ucenik("Josip", 15, 10)
print(f"Ucenik {ucenik1.name} ima {ucenik1.godine} godina i uspjeh {ucenik1.uspjeh}")