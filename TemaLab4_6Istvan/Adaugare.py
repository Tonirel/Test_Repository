'''
Created on Oct 24, 2019

@author: Tonirel
'''
def create_state():
    s=[]
    return s

def create_tz(zi,suma,tip):
    '''
    Functie ce creeaza o tranzactie cu urm. valori: zi, suma, tip 
    input - zi-int, suma-float, tip-string
    output - tz : o tranzactie
    '''
    tz=({'zi':zi,
        'suma':suma,
        'tip':tip})
    return tz

def get_zi(tz):
    '''
    Functie ce returneaza ziua in care s-a efectuat tranzactia : tz
    input - tranzactie : o tranzactie
    output - zi-int : ziua in care s-a efectuat  tranzactia : tz
    '''
    return int(tz['zi'])

def get_suma(tz):
    '''
    Functie ce returneaza suma tranzactiei : tz
    input - tranzactie : o tranzactie
    output - suma-float : suma tranzactiei : tz
    '''
    return float(tz['suma'])
   
def get_tip(tz):
    '''
    Functie ce returneaza tipul tranzactiei : tz
    input - tranzactie : o tranzactie
    output - tip-strint : tipul tranzactiei : tz
    '''
    return tz['tip']
def valid_tz(tz):
    '''
    Functie ce valideaza ziua, suma, tipul tranzactiei : tz
    input - tz : o tranzactie
    output - -----
    raises:Exception daca zi<=0 atunci print "zi incorecta!"
                     daca suma<0 atunci print "suma incorecta!"
                     daca tip!='intrare or tip!='iesire' print "tip incorect!"
    '''
    if get_zi(tz)<=0:
        raise Exception("zi incorecta!")
    
    if get_suma(tz)<0:
        raise Exception("suma incorecta!")
           
    if get_tip(tz)!='intrare' and get_tip(tz)!='iesire':
        raise Exception('tip incorect!')
    
def add_tz(s,tz):
    '''
    Functie ce adauga tranzactia : tz in lista : s
    input - s : o lista, tz : o tranzactie
    output - -----
    '''
    s.append(tz)
def lenght(s):
    return len(s)