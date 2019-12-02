'''
Created on Oct 24, 2019

@author: Tonirel
'''
from Service import sv_add_tz,sv_sum_gr8_than,sv_b4_day_gr8_than,sv_tz_anumit_tip,sv_el_tz_tip,sv_sum_tip,sv_sold,sv_tz_tip_ord,sv_del_tz_zi,sv_del_tz_per,sv_del_tz_tip,\
    sv_el_tz_small_and_type,sv_undo, add_undo
from Cautari import get_suma
from Adaugare import create_state, lenght
def new_UI_help():
    print("")
    print("--------------------MENIU--------------------")
    print("")
    print("adaugare - adaugarea unei tranzactii in lista")
    print("print - afisarea listei tranzactiilor")
    print("cautari - sectiunea de cautari(1 suma,2 suma zi,3 tip)")
    print("stergeri - sectiune de stergeri")
    print("rapoarte - sectiunea de rapoarte")
    print("filtrari - sectiunea de filtrari")
    print("undo - reface ultima operatie")
    print("exit - iesire din aplicatie")
    print("")
    
def new_UI_add_tz(s,us,x):
    while True:
        try:
            zi=x[1]
            suma=x[2]
            tip=x[3]
            if tip!='intrare' and tip!='iesire':
                    raise Exception("Tip incorect!")
            else:
                sv_add_tz(s,zi,suma,tip)
                '''s2=create_state()
                s2=s.copy()
                us.append(s2.copy())'''
                add_undo(s,us)
                print("")
                print("Tranzactia a fost adaugata cu succes!")
            break
        except Exception as ex:
            print(ex)
            
def new_UI_print(s,us,x):
    if lenght(s)==0:
        print("Nu exista tranzactii!")
    else:
        print("Lista este: ")
        for tz in s:
            print("zi:",tz['zi'],", suma:",tz['suma'],", tipul:",tz['tip']) 
def UI_help_cautari_section():
    print("")
    print("--------------------MENIU SECTIUNE CAUTARI--------------------")
    print("")
    print("1 - Tipareste tranzactiile cu sume mai mari decat o suma data")
    print("2 - Tipareste tranzactiile efectuate inainte de o zi si mai mari decat o suma")
    print("3 - Tipareste tranzactiile de un anumit tip")
    print("return - Iesire din sectiunea de cautari")
    print("")   
def UI_sum_gr8_than(s,us,x):
    while True:
        S=x[2]
        try:
            S=float(S)
            break
        except Exception as ex:
            print(ex)
    s2=sv_sum_gr8_than(S,s)
    
    if s2==[]:
        print("Nu exista astfel de tranzactii")
    else:
        print("Lista tranzactiilor cu suma mai mare decat",S,"este:")
        print("")
        new_UI_print(s2,us,x)

def UI_b4_day_gr8_than(s,us,x):
    while True:
        Z=x[3]
        S=x[2]
        try:
            S=float(S)
            Z=int(Z)
            break
        except Exception as ex:
            print(ex)
    s2=sv_b4_day_gr8_than(S,Z,s)
    if s2==[]:
        print("Nu exista astfel de tranzactii")
    else:
        print("Lista tranzactiilor cu suma mai mare decat",S,"si efectuate inainte de ziua",Z,"este:")
        print("")
        new_UI_print(s2,us,x)
def UI_tz_anumit_tip(s,us,x):
    while True:
        try:
                T=x[2]
                if T!='intrare' and T!='iesire':
                    raise Exception("Tip incorect!")
                break
        except Exception as ex:
            print(ex)
    s2=sv_tz_anumit_tip(T,s)
    if s2==[]:
        print("Nu exista astfel de tranzactii")
    else:
        print("Lista tranzactiilor de tipul",T,"este:")
        print("")
        new_UI_print(s2,us,x)
def new_UI_cautari_section(s,us,x):
    if s==[]:
        print("Lista este goala")
        return
    commands={
        "1":UI_sum_gr8_than,
        "2":UI_b4_day_gr8_than,
        "3":UI_tz_anumit_tip
        }
    while True:
        UI_help_cautari_section()
        for i in range(1,len(x),1):
            if i==len(x)-1:
                return
            if x[i]=="return":
                print("Iesire din sectiunea de cautari...")
                return
            if x[i] in commands:
                commands[x[i]](s,us,x)
            else:
                print("Comanda invalida")
        
def UI_sum_tip(s,us):

    while True:
        try:
                T=input("Introduceti tipul: ")
                if T!='intrare' and T!='iesire':
                    raise Exception("Tip incorect!")
                break
        except Exception as ex:
            print(ex)
    S=sv_sum_tip(T,s)
    if lenght(s)>0:
        print('Suma tranzactiilor de tipul '+T+' este:')
        print(S) 
    else:
        print(S)   
        
def UI_sold(s,us):
    
    while True:
        Z=input("Introduceti ziua: ")
        try:
                Z=int(Z)
                break
        except Exception as ex:
            print(ex)
    S=sv_sold(Z,s)
    if lenght(s)>0:
        print('Soldul de la data ',Z,' este: ',S)
    else:
        print(S)
        
def UI_tz_tip_ord(s,us,x):
    while True:
        try:
                T=input("Introduceti tipul: ")
                if T!='intrare' and T!='iesire':
                    raise Exception("Tip incorect!")
                break
        except Exception as ex:
            print(ex)
    new_UI_print(sv_tz_tip_ord(T,s),us,x)
def UI_help_rapoarte_section():
    print("")
    print("--------------------MENIU SECTIUNE RAPOARTE--------------------")
    print("")
    print("1 - Suma tranzactiilor de un anumit tip")
    print("2 - Soldul contului la o data specificata")
    print("3 - Tipareste toate tranzactiile de un anumit tip ordonate dupa suma")
    print("return - Iesire din sectiunea de rapoarte")
    print("")  
def new_UI_rapoarte_section(s,us,x):
    s2=create_state()
    if s==s2:
        print("Lista este goala")
        return
    commands={
        "1":UI_sum_tip,
        "2":UI_sold,
        "3":UI_tz_tip_ord
        }
    while True:
        UI_help_rapoarte_section()
        command=input("Dati comanda: ")
        if command=="return":
            print("Iesire din sectiunea de rapoarte...")
            return
        if command in commands:
            commands[command](s,us)
        else:
            print("Comanda invalida!")
def UI_del_tz_zi(s,us):
    while True:
        Z=input("Introduceti ziua: ")
        try:
                Z=int(Z)
                break
        except Exception as ex:
            print(ex)
    s=sv_del_tz_zi(s,Z)
    add_undo(s,us)
    print('Tranzactiile au fost sterse cu succes!')
    
def UI_del_tz_per(s,us):
    while True:
        Z1=input("Introduceti prima zi: ")
        Z2=input("Introduceti a doua zi: ")
        try:
                Z1=int(Z1)
                Z2=int(Z2)
                break
        except Exception as ex:
            print(ex)
    s=sv_del_tz_per(s,Z1,Z2)
    add_undo(s,us)
    print('Tranzactiile au fost sterse cu succes!')
def UI_del_tz_tip(s,us):
    while True:
        try:
                T=input("Introduceti tipul: ")
                if T!='intrare' and T!='iesire':
                    raise Exception("Tip incorect!")
                break
        except Exception as ex:
            print(ex)
    s=sv_del_tz_tip(s,T)
    add_undo(s,us)
    print('Tranzactiile au fost sterse cu succes!')
def UI_help_stergeri_section():
    print("")
    print("--------------------MENIU SECTIUNE STERGERI--------------------")
    print("")
    print("1 - Sterge tranzactiile la o zi specificata")
    print("2 - Sterge tranzactiile dintr-o perioada specificata")
    print("3 - Sterge toate tranzactiile de un anumit tip")
    print("return - Iesire din sectiunea de rapoarte")
    print("")  
def new_UI_stergeri_section(s,us,x):
    s2=create_state()
    if s==s2:
        print("Lista este goala!")
        return
    commands={
        "1":UI_del_tz_zi,
        "2":UI_del_tz_per,
        "3":UI_del_tz_tip
        }
    while True:
        UI_help_stergeri_section()
        command=input("Dati comanda: ")
        if command=="return":
            print("Iesire din sectiunea de stergeri...")
            return
        if command in commands:
            commands[command](s,us)
        else:
            print("Comanda invalida!")
def new_UI_undo(s,us,x):
    if lenght(s)==0:
        print("Can't undo!")
    else:
        del s[:]
        s+=sv_undo(s,us).copy()
        print("Undo efectuat cu succes!")
    