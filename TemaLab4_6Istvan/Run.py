#2
#timisrazvanvasile@gmail.com
#arhiva cu nume, prenume, grupa, extensia (doar codul)
'''
Created on Oct 24, 2019

@author: Tonirel
'''
from Tests import run_all_tests
from UI import UI_help,UI_add_tz,UI_print,UI_cautari_section,UI_filtrari_section,UI_rapoarte_section,UI_stergeri_section,UI_undo
from Adaugare import create_state
from new_UI import new_UI_add_tz,new_UI_cautari_section,new_UI_rapoarte_section,new_UI_stergeri_section,new_UI_print,new_UI_undo,new_UI_help
def what_to_run():
    while True:
        x=input("Alegeti meniul(nou/vechi): ")
        if x=='nou':
            run_new()
            break
        elif x=='vechi':
            run()
            break
        else:
            print("Am zis nou sau vechi!: ")
def run_new():
    s=create_state()
    us=create_state()
    commands={'adaugare':new_UI_add_tz,
              'print':new_UI_print,
              'stergeri':new_UI_stergeri_section,
              'cautari':new_UI_cautari_section,
              'rapoarte':new_UI_rapoarte_section,
              'undo':new_UI_undo
        }
    while True:
        new_UI_help()
        command=input("Dati comanda: ")
        x=command.split(' ')
        cmd=x[0]
        if cmd=='exit':
            print("Iesire din aplicatie...")
            return 
        if cmd in commands:
            try:
                commands[cmd](s,us,x)
            except ValueError as ex:
                print(str(ex))
        else:
            print("Comanda invalida")
def run():
    s=create_state()
    us=create_state()
    commands={'adaugare':UI_add_tz,
              'print':UI_print,
              'stergeri':UI_stergeri_section,
              'cautari':UI_cautari_section,
              'filtrari':UI_filtrari_section,
              'rapoarte':UI_rapoarte_section,
              'undo':UI_undo
        }
    while True:
        UI_help()
        command=input("Dati comanda: ")
        if command=='exit':
            print("Iesire din aplicatie...")
            return 
        if command in commands:
            try:
                commands[command](s,us)
            except ValueError as ex:
                print(str(ex))
        else:
            print("Comanda invalida")

run_all_tests()
what_to_run()