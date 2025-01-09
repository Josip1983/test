class Ucenik() : 
    def __init__(self, name):
     self._name=name
     self._uspjeh=''

    def get_name(self) :
        return self._name
    
    def get_uspjeh(self) :
        return self._uspjeh
    
    def set_uspjeh (self, novi_uspjeh) :
        if novi_uspjeh <=5 and novi_uspjeh>0 :
            self._uspjeh= novi_uspjeh
        else : 
            print(f"Unijeti uspjeh {novi_uspjeh} nije validan")

ucenik1=Ucenik("Josip")

print(f"Ucenik1 ime : {ucenik1.get_name()}.")

ucenik1.set_uspjeh(4.9)

print(f"Ucenik1 ime : {ucenik1.get_name()}, ima uspjeh {ucenik1.get_uspjeh()}.")