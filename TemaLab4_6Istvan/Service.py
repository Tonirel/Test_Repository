'''
Created on Oct 24, 2019

@author: Tonirel
'''
#adaug ceva random
from Adaugare import create_tz,valid_tz,add_tz,get_suma,get_zi,get_tip, create_state,\
    lenght
from Cautari import sum_gr8_than,b4_day_gr8_than,tz_anumit_tip
def add_undo(s,us):
    s2=create_state()
    s2=s.copy()
    us.append(s2.copy())
def sv_add_tz(s,zi,suma,tip):
    '''
    Functie ce creeaza o tranzactie pe baza parametrilor,
    o valideaza si o adauga in lista : s
    '''
    tz=create_tz(zi,suma,tip)
    valid_tz(tz)
    add_tz(s,tz)
    
def sv_sum_gr8_than(S,s):
    '''
    Functie ce creeaza o lista cu tranzactii din lista : s care
    are tranzactii mai mari decat suma : S
    input - S : suma cu care trebuie comparate tranzactiile, s : lista de tranzactii
    output - gr_list : lista cu tranzactii mai mari decat suma : S
    '''
    if S<0:
        raise ValueError("Suma trebuie sa fie un numar pozitiv!")
    gr8_s=create_state()
    for tz in s:
        if sum_gr8_than(S,tz)==True:
            gr8_s.append(tz)
    return gr8_s
def sv_b4_day_gr8_than(S,Z,s):
    '''
    Functie ce creeaza o lista cu tranzactii din lista : s care
    are tranzactii cu suma mai mare decat suma : S si cu ziua mai mare decat ziua : Z
    input - S : suma cu care trebuie comparate tranzactiile, Z : ziua cu care trebuie comparate tranzactiile,
    s : lista de tranzactii
    output - b4_gr_list : lista care are tranzactii cu suma mai mare decat suma : S si cu ziua mai mare decat ziua : Z
    '''
    if S<0:
        raise ValueError("Suma trebuie sa fie un numar pozitiv!")
    if Z<=0:
        raise ValueError("Ziua trebuie sa fie un numar pozitiv!")
    b4_gr8_s=create_state()
    for tz in s:
        if b4_day_gr8_than(S, Z, tz)==True:
            b4_gr8_s.append(tz)
    return b4_gr8_s
def sv_tz_anumit_tip(T,s):
    '''
    Functie ce creeaza o lista cu tranzactii din lista : s care are
    tranzactii de tipul : T
    input - T : tipul dorit, s : lista tranzactiilor
    output : lista de tranzactii de tipul : T
    '''
    #if T!=str('intrare') or T!=str('iesire'):
    #    raise ValueError("Tipul trebuie sa fie 'intrare' sau 'iesire'!")
    tip_s=create_state()
    for tz in s:
        if tz_anumit_tip(tz,T)==True:
            tip_s.append(tz)
    return tip_s

def sv_el_tz_tip(T,s):
    '''
    Functie ce elimina toate tranzactiile de tipul : T din lista : s
    input - T - tipul dorit, s : lista tranzactiilor
    output : el_list : lista dupa eliminari
    '''
    s2=create_state()
    for tz in s:
        if tz_anumit_tip(tz,T)==False:
            add_tz(s2, tz)
    return s2
def sv_el_tz_small_and_type(S,T,s):
    '''
    Functie ce elimina toate tranzactiile de tipul : T mai mici decat suma : S din lista : s
    input : T - up tip, S - o suma, s - lista tranzactiilor
    output : el_list : lista dupa eliminari
    '''
    s2=create_state()
    for tz in s:
        if tz_anumit_tip(tz,T)==False or get_suma(tz)>=S:
            add_tz(s2,tz)
    return s2
def sv_sum_tip(T,s):
    '''
    Functie ce calculeaza suma tranzactiilor de un anumit tip
    input : T - un tip, s - lista de tranzactii
    output : S - Suma tranzactiilor de un anumit tip
    '''
    if lenght(s)==0:
        return 'Lista este goala!'
    S=0
    for tz in s:
        if tz_anumit_tip(tz, T)==True:
            S+=get_suma(tz)
    return S
def sv_sold(Z,s):
    '''
    Functie ce calculeaza soldul contului la o data specificata
    input : Z - o zi, s - lista tranzactiilor
    iutput : S - soldul contului la o data specificata
    '''
    if lenght(s)==0:
        return 'Lista este goala!' 
    S=0
    for tz in s:
        if get_zi(tz)<=Z:
            if get_tip(tz)=='intrare':
                S+=get_suma(tz)
            elif get_tip(tz)=='iesire':
                S-=get_suma(tz)
    return S
def sv_tz_tip_ord(T,s):
    '''
    Functie ce tipareste toate tranzactiile de un anumit tip, ordonate dupa suma
    input : T - un tip, s - lista tranzactiilor
    output : s3 - lista tranzactiilor de un anumit tip
    '''
    if lenght(s)==0:
        return 'Lista este goala!'
    s2=s.copy() 
    for i in range(0,lenght(s2)-1,1):
        for j in range(i+1,lenght(s2),1):
            if get_suma(s2[i])>get_suma(s2[j]):
                s2[i],s2[j]=s2[j],s2[i]
    s3=create_state()
    for tz in s2:
        if get_tip(tz)==T:
            add_tz(s3, tz)
    return s3
def sv_del_tz_zi(s,Z):
    '''
    Functie ce sterge tranzactiile dintr-o anumita zi
    input : s - lista tranzactiilor, Z - o zi
    output : s - lista dupa stergeri
    '''
    if lenght(s)==0:
        return 'Lista este goala!'
    i=0
    while i<lenght(s):
        if get_zi(s[i])==Z:
            s.pop(i)
        else:
            i+=1
    return s
def sv_del_tz_per(s,Z1,Z2):
    '''
    Functie ce sterge tranzactiile dintr-o anumita perioada
    input : s - lista tranzactiilor, Z1,Z2 - doua zile
    output : s - lista dupa stergeri
    '''
    if lenght(s)==0:
        return 'Lista este goala!'
    i=0
    if Z1>Z2:
        Z1,Z2=Z2,Z1
    while i<lenght(s):
        if get_zi(s[i])>=Z1 and get_zi(s[i])<=Z2:
            s.pop(i)
        else:
            i+=1
    return s
def sv_del_tz_tip(s,T):
    '''
    Functie ce sterge tranzactiile de un anumit tip
    input : s - lista tranzactiilor, T - un tip
    output : lista dupa stergeri
    '''
    if lenght(s)==0:
        return 'Lista este goala!'
    i=0
    while i<lenght(s):
        if get_tip(s[i])==T:
            s.pop(i)
        else:
            i+=1
    return s
def sv_undo(s,us):
    if lenght(us)==0:
        return "Can't undo no more"
    elif lenght(us)==1:
        del s[:]
        return s
    else:
        us.pop(len(us)-1)
        s2=create_state()
        s2+=us[lenght(us)-1]
        del s[:]
        s=s2.copy()
        return s