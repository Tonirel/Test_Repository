'''
Created on Oct 24, 2019

@author: Tonirel
'''
from Adaugare import get_suma, get_zi,get_tip

def sum_gr8_than(S,tz):
    '''
    Functia preia o tranzactie si o compara cu suma data
    input - S : suma cu care trebuie comparata tranzactia, tz : o tranzactie
    output - True : daca tz[suma] e mai mare decat suma/False : daac tz[suma] e mai mica decat suma
    '''
    if S<get_suma(tz):
        return True
    else:
        return False
def b4_day_gr8_than(S,Z,tz):
    '''
    Functia preia o tranzactie si o compara cu o suma data si o zi data
    input - S : suma cu care trebuie comparata tranzactia, Z : ziua cu care trebuie comparata tranzactia,
    tz : o tranzactie
    output - True : daca ziua este mai mare decat ziua tranzactiei si suma este mai mica decat suma tranzactiei
    False : daca una dintre cele doua conditii de la True este falsa
    '''
    #if sum_gr8_than(S,tz)==True:
    if S<get_suma(tz):
        if Z>get_zi(tz):
            return True
        else:
            return False
    else:
        return False
def tz_anumit_tip(tz,tip):
    '''
    Functia verifica daca o anumita tranzactie este de tipul : tip, dat ca parametru
    input - tz: o tranzactie, tip : un tip
    output - True : daca tranzactia este de tipul : tip / False : in caz contrar
    '''
    if tip==get_tip(tz):
        return True
    else:
        return False