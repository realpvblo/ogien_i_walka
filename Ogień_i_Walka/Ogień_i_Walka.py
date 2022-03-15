import random
import time
import os

class Rycerz:
  def __init__(self, name, hp, armor, dmg, gold):
    self.name = name
    self.hp = hp
    self.armor = armor
    self.dmg = dmg
    self.gold = gold

p1 = Rycerz("Sir Galahad", 100, 50, 20, 50)

#print(p1.name)
#print(p1.age)

def intro1():
    time.sleep(1)
    print("+-------------------------------------+")
    print('Ogień i Walka - Tekstowa gra przygodowa')
    print("+-------------------------------------+")
    time.sleep(1.5)
    print("      _,.")
    time.sleep(0.4)
    print("    ,` -.)")
    time.sleep(0.4)
    print("   ( _/-\\-._")
    time.sleep(0.4)
    print("  /,|`--._,-^|            ,")
    time.sleep(0.4)
    print("  \_| |`-._/||          ,'|")
    time.sleep(0.4)
    print("    |  `-, / |         /  /")
    time.sleep(0.4)
    print("    |     || |        /  /")
    time.sleep(0.4)
    print("     `r-._||/   __   /  /")
    time.sleep(0.4)
    print(" __,-<_     )`-/  `./  /")
    time.sleep(0.4)
    print("'  \   `---'   \   /  /")
    time.sleep(0.4)
    print("    |           |./  /")
    time.sleep(0.4)
    print("    /           //  /")
    time.sleep(0.4)
    print("\_/' \         |/  /")
    time.sleep(0.4)
    print(" |    |   _,^-'/  /")
    time.sleep(0.4)
    print(" |    , ``  (\/  /_")
    time.sleep(0.4)
    print("  \,.->._    \X-=/^")
    time.sleep(0.4)
    print("  (  /   `-._//^`")
    time.sleep(0.4)
    print("   `Y-.____(__}")
    time.sleep(0.4)
    print("    |     {__)")
    time.sleep(0.4)
    print("          ()")
    print()
    time.sleep(3)


def intro2():
    time.sleep(0.5)
    print("- Witaj odważny rycerzu!")
    time.sleep(2.5)
    print()
    print("- Nazywasz się Sir Galahad...")
    time.sleep(2.5)
    print()
    print("- Pochodzisz z Królestwa Vaborg...")
    time.sleep(2.5)
    print()
    print(
        "- Twój Król, Jego Wysokość Galeran Uczciwy wysyła Cię na misję pokonania smoka Sumed’a nazywanego przez mieszkańców królestwa Niszczycielem Życia, albowiem od wielu lat plądruje on wioski należące do Jego Królewskiej Mości oraz morduje poddanych...")
    time.sleep(15)
    print()
    print(
        "- Twoim celem jest dostać się na Niespokojne Góry znajdujące się na północ królestwa. Tam według opowiadań znajduje się gniazdo smoka. Będziesz musiał pokonać Wolny Las Jesionowy, przedostać się przez rzekę zwaną Turkusowy Kanał oraz na koniec przedrzeć się przez Pustkowia Grozy...")
    time.sleep(15)
    print()
    print(
        "- Twoja wyprawa nie będzie łatwa, ale jeśli będziesz podejmować mądre decyzje w czasie swojej podróży uda Ci się bezpiecznie dotrzeć do groty smoka i pokonać go, po czym zostaniesz obsypany królewskim złotem oraz okrzyknięty wybawicielem Vaborg’u...")
    time.sleep(15)
    print()
    print("Czy jesteś gotowy do drogi?")
    time.sleep(1)
    print()
 #   print("Wpisz: \n[1] - jesli Tak\n[2] - jesli Nie")


#def sciezka():
#    path = ""
#    while path != "1" and != "2":  # input validation
#        path = input("")

def start():
    droga = ""
    droga = input("Wpisz: \n[1] - jesli Tak\n[2] - jesli Nie\n")
    if droga == "1":
        print("Zaczynajmy!")
    elif droga == "2":
        print("Krolestwo zostało skazane na wieczna kleske")
        exit()
    else:
        print("Bledna odpowiedz")
        exit()
    print()

def kontynuuj():
    wpisz1 = ""
    wpisz1 = input("- Wcisnij [enter], aby kontynuowac -\n")
    if wpisz1 == "1":
        pass
    else:
        pass
    print()

def statystyki():
    print("Twoje Statystyki: ")
    time.sleep(0.5)
    print("Imie: ", p1.name)
    time.sleep(0.5)
    print("Zycie: ", p1.hp)
    time.sleep(0.5)
    print("Zbroja: ", p1.armor)
    time.sleep(0.5)
    print("Obrazenia: ", p1.dmg)
    time.sleep(0.5)
    print("Złoto: ", p1.gold)
    print()



intro1()
#os.system('clear')
#os.system('CLS')
intro2()
start()


time.sleep(1)

print("+-----------------------+")
print("Opuszczasz bramy zamku...")
print("+-----------------------+")
time.sleep(1)

print("")

statystyki()

kontynuuj()

time.sleep(1)
print("+--------------------------+")
print("Spotykasz ulicznego kupca...")
print("+--------------------------+")
time.sleep(1.5)

print()
print("Masz przy sobie 50szt zlota. Pamietaj aby dokonywac madrych zakupow. Pieniadze moga Ci sie przydac pozniej")
print()
time.sleep(4)

zakupy = ''
zakupy = input("Sklep:\n[1] Mikstura Zycia (+10 zycia) - 15szt zlota\n[2] Tarcza Barbarzyncy (+15 pancerza) - 20szt zlota\n[3] Sztylet ze Smoczego Pazura (+10 obrazen) - 20szt zlota\n[4] Nie kupuj nic\n")
print()
if zakupy == "1":
    p1.hp = 110
    p1.gold = 35
elif zakupy == "2":
    p1.armor = 65
    p1.gold = 30
elif zakupy == "3":
    p1.dmg = 30
    p1.gold = 30
else:
    pass


print("W kieszeni zostalo: ",p1.gold,"szt zlota\n")
statystyki()

kontynuuj()

time.sleep(1)
print("+-----------------------------------+")
print("Docierasz do 'Wolny Las Jesionowy'...")
print("+-----------------------------------+")
time.sleep(1)
print()

print("Przed sobą masz wejscie do lasu, jednak ono rozchodzi sie w 3 kierunkach, ktory wybierasz?")

las = ""
while (las != "1" and las != "2" and las != "3"):
    las = input("Wybierz droge: \n[1] - Idz prosto\n[2] - Idz w lewo\n[3] - Idz w prawo\n")
    if las == "1":
     print("Idziesz prosto")
     print()
     time.sleep(1)
     las2 = ""
     while (las2 != "1" and las2 != "2" and las2 != "3"):
         las2 = input("Znowu trafiasz na rozwidlenie drog, w ktora strone idziesz?: \n[1] - Idz prosto\n[2] - Idz w lewo\n[3] - Idz w prawo\n")
         if las2 == "1":
             print("Idziesz prosto")
             print()
             time.sleep(1)
             print()
             print("Trawiasz do obozowiska przyjaznych ludzi lasu")
         elif las2 =="2":
             print("Idziesz w lewo")
             print()
             time.sleep(1)
             orkowie2 = ""
             while (orkowie2 != "1" and orkowie2 != "2"):
                 orkowie2 = input("Trafiasz na siedzibe orków, jaka podejmujesz decyzje?\n[1] - Zaatakuj (-30zycia, +20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
                 if orkowie2 == "1":
                     print("Zaatakowales osiedlisko orków, pomimo wielu odniesionych ran udało Ci się zebrac ich złoto")
                     p1.hp = p1.hp - 30
                     p1.gold = p1.gold + 20
                     print()
                     statystyki()
                     print("Wracasz na rozwidlenie dróg, w którą stronę chcesz isc?")
                     trasa1 = ""
                     while (trasa1 != "1" and trasa1 != "2"):
                         trasa1 = input("[1] - Idz prosto\n[2] - Idz w prawo")
                         if trasa1 == "1":
                             print("Idziesz prosto")
                             print()
                             time.sleep(1)
                             print()
                             print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                         elif trasa1 == "2":
                             print("Idziesz w prawo")
                             print()
                             time.sleep(1)
                             czarodziej2 = ""
                             while (czarodziej2 != "1" and czarodziej2 != "2"):
                                 czarodziej2 = input(
                                     "Trafiasz do wiezy czarodzieja, jaka podejmujesz decyzje?\n[1] - Odwiedz (+20 ataku, -20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
                                 if czarodziej2 == "1":
                                     print("Czarodziej częstuje Cię specjalną miksturą która wzmacnia Twoją siłę")
                                     p1.dmg = p1.dmg + 20
                                     p1.gold = p1.gold - 20
                                     print()
                                     statystyki()
                                     print("Wracasz na rozwidlenie dróg, jedyna droga jaka pozostała to na przód")
                                     print()
                                     time.sleep(1)
                                     kontynuuj()
                                     print("Trawiasz do obozowiska przyjaznych ludzi lasu")

                                 elif czarodziej2 == "2":
                                     print("Zostawiasz czarodzieja w spokoju i cofasz się na rozwidlenie dróg")
                                     print("Jedyna droga jaka pozostała to na przód")
                                     print()
                                     time.sleep(1)
                                     kontynuuj()
                                     print("Trawiasz do obozowiska przyjaznych ludzi lasu")

                                 else:
                                     print("Bledna odpowiedz")
                         else:
                             print("Bledna odpowiedz")


                     #
                 elif orkowie2 == "2":
                     print("Wracasz na rozwidlenie dróg, w którą stronę chcesz isc?")
                     trasa2 = ""
                     while (trasa2 != "1" and trasa2 != "2"):
                         trasa2 = input("[1] - Idz prosto\n[2] - Idz w prawo")
                         if trasa2 == "1":
                             print("Idziesz prosto")
                             print()
                             time.sleep(1)
                             print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                         elif trasa2 == "2":
                             print("Idziesz w prawo")
                             print()
                             time.sleep(1)
                             czarodziej3 = ""
                             while (czarodziej3 != "1" and czarodziej3 != "2"):
                                 czarodziej3 = input(
                                     "Trafiasz do wiezy czarodzieja, jaka podejmujesz decyzje?\n[1] - Odwiedz (+20 ataku, -20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
                                 if czarodziej3 == "1":
                                     print("Czarodziej częstuje Cię specjalną miksturą która wzmacnia Twoją siłę")
                                     p1.dmg = p1.dmg + 20
                                     p1.gold = p1.gold - 20
                                     print()
                                     statystyki()
                                     print("Wracasz na rozwidlenie dróg, jedyna droga jaka pozostała to na przód")
                                     print()
                                     time.sleep(1)
                                     kontynuuj()
                                     print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                                 elif czarodziej3 == "2":
                                     print("Zostawiasz czarodzieja w spokoju i wracasz na rozwidlenie dróg, pozostało Ci iść prosto")
                                     print()
                                     time.sleep(1)
                                     kontynuuj()
                                     print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                                 else:
                                     print("Bledna odpowiedz")
                                     print()
                         else:
                             print("Bledna odpowiedz")
                             print()

                     #
                 else:
                     print("Bledna odpowiedz")
                     print()

    elif las == "2":
      print("Idziesz w lewo")
      print()
      time.sleep(1)
      orkowie = ""
      while (orkowie != "1" and orkowie != "2"):
        orkowie = input("Trafiasz na siedzibe orków, jaka podejmujesz decyzje?\n[1] - Zaatakuj (-30zycia, +20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
        if orkowie == "1":
         print("Zaatakowales osiedlisko orków, pomimo wielu odniesionych ran udało Ci się zebrac ich złoto")
         p1.hp = p1.hp - 30
         p1.gold = p1.gold + 20
         print()
         statystyki()
         print("Wracasz na rozwidlenie dróg, w którą stronę chcesz isc?")
         trasa4 = ""
         while (trasa4 != "1" and trasa4 != "2"):
             trasa4 = input("[1] - Idz prosto\n[2] - Idz w prawo")
             if trasa4 == "1":
                 print("Idziesz prosto")
                 print()
                 time.sleep(1)
                 print("Trawiasz do obozowiska przyjaznych ludzi lasu")
             elif trasa4 == "2":
                 print("Idziesz w prawo")
                 print()
                 time.sleep(1)
                 czarodziej3 = ""
                 while (czarodziej3 != "1" and czarodziej3 != "2"):
                     czarodziej3 = input(
                         "Trafiasz do wiezy czarodzieja, jaka podejmujesz decyzje?\n[1] - Odwiedz (+20 ataku, -20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
                     if czarodziej3 == "1":
                         print("Czarodziej częstuje Cię specjalną miksturą która wzmacnia Twoją siłę")
                         p1.dmg = p1.dmg + 20
                         p1.gold = p1.gold - 20
                         print()
                         statystyki()
                         print("Wracasz na rozwidlenie dróg, jedyna pozostała droga to prosto")
                         print()
                         time.sleep(1)
                         kontynuuj()
                         print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                     elif czarodziej3 == "2":
                         print("Cofasz się do rozwidlenia dróg, jedyna pozostała trasa to naprzód")
                         print()
                         time.sleep(1)
                         kontynuuj()
                         print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                     else:
                         print("Bledna odpowiedz")
                         print()



             else:
                 print("Bledna odpowiedz")
                 print()
         # dokonczyc

        elif orkowie == "2":
         print("Wracasz na rozwidlenie dróg, w którą stronę chcesz isc?")

        else:
            print("Bledna odpowiedz")
            print()

    elif las == "3":
      print("Idziesz w prawo")
      print()
      time.sleep(1)
      czarodziej = ""
      while (czarodziej != "1" and czarodziej != "2"):
        czarodziej = input("Trafiasz do wiezy czarodzieja, jaka podejmujesz decyzje?\n[1] - Odwiedz (+20 ataku, -20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
        if czarodziej == "1":
         print("Czarodziej częstuje Cię specjalną miksturą która wzmacnia Twoją siłę")
         p1.dmg = p1.dmg + 20
         p1.gold = p1.gold - 20
         print()
         statystyki()
         print("Wracasz na rozwidlenie dróg, w którą stronę chcesz isc?")
         trasa4 = ""
         while (trasa4 != "1" and trasa4 != "2"):
             trasa4 = input("[1] - Idz prosto\n[2] - Idz w lewo")
             if trasa4 == "1":
                 print("Idziesz prosto")
                 print()
                 time.sleep(1)
                 print("Trawiasz do obozowiska przyjaznych ludzi lasu")
             elif trasa4 == "2":
                 print("Idziesz w lewo")
                 orkowie = ""
                 while (orkowie != "1" and orkowie != "2"):
                     orkowie = input(
                         "Trafiasz na siedzibe orków, jaka podejmujesz decyzje?\n[1] - Zaatakuj (-30zycia, +20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
                     if orkowie == "1":
                         print(
                             "Zaatakowales osiedlisko orków, pomimo wielu odniesionych ran udało Ci się zebrac ich złoto")
                         p1.hp = p1.hp - 30
                         p1.gold = p1.gold + 20
                         print()
                         statystyki()
                         print("Wracasz na rozwidlenie dróg, pozostało Ci już tylko iść prosto")
                         print()
                         time.sleep(1)
                         kontynuuj()
                         print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                     elif orkowie == "2":
                         print("Wracasz na rozwidlenie dróg, w którą stronę chcesz isc?\n")

                     else:
                         print("Bledna odpowiedz")
                         print()
                 else:
                     print("Bledna odpowiedz")
                     print()
         # dokonczyc orkowie
        elif czarodziej == "2":
            print("Cofasz się do rozwidlenia dróg, którą drogę wybierasz?\n")
            #prosto lub w lewo
            trasa4 = ""
            while (trasa4 != "1" and trasa4 != "2"):
                trasa4 = input("[1] - Idz prosto\n[2] - Idz w lewo")
                if trasa4 == "1":
                    print("Idziesz prosto")
                    print()
                    time.sleep(1)
                    print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                elif trasa4 == "2":
                    print("Idziesz w lewo")

                    #orkowie

                    trasa4 = ""
                    while (trasa4 != "1" and trasa4 != "2"):
                        trasa4 = input("[1] - Idz prosto\n[2] - Idz w lewo")
                        if trasa4 == "1":
                            print("Idziesz prosto")
                            print()
                            time.sleep(1)
                            print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                        elif trasa4 == "2":
                            print("Idziesz w lewo")
                            orkowie = ""
                            while (orkowie != "1" and orkowie != "2"):
                                orkowie = input(
                                    "Trafiasz na siedzibe orków, jaka podejmujesz decyzje?\n[1] - Zaatakuj (-30zycia, +20szt zlota)\n[2] - Zostaw i cofnij sie do lasu\n")
                                if orkowie == "1":
                                    print(
                                        "Zaatakowales osiedlisko orków, pomimo wielu odniesionych ran udało Ci się zebrac ich złoto")
                                    p1.hp = p1.hp - 30
                                    p1.gold = p1.gold + 20
                                    print()
                                    statystyki()
                                    print("Wracasz na rozwidlenie dróg, pozostało Ci już tylko iść prosto")
                                    print()
                                    time.sleep(1)
                                    kontynuuj()
                                    print("Trawiasz do obozowiska przyjaznych ludzi lasu")
                                elif orkowie == "2":
                                    print("Wracasz na rozwidlenie dróg, jedyna droga jaka została to naprzód")
                                    print()
                                    time.sleep(1)
                                    kontynuuj()
                                    print("Trawiasz do obozowiska przyjaznych ludzi lasu")

                                else:
                                    print("Bledna odpowiedz")
                                    print()
                            else:
                                print("Bledna odpowiedz")
                                print()

        else:
            print("Bledna odpowiedz")
            print()

    else:
        print("Bledna odpowiedz")
print()

time.sleep(1)

print("+----------------------+")
print("Obozowisko Ludzi Lasu...")
print("+----------------------+")
time.sleep(1)

ludzieLasu = ''
print("Znajdujesz sie w obozowisku przyjaznych ludzi lasu. Masz do wyboru dwie opcje: \n[1] - Ogrzej sie przy ognisku i odpocznij (-20szt zlota za pobyt/regeneracja zdrowia do 100%)\n[2] - Idz dalej\n")

while (ludzieLasu != "1" and ludzieLasu != "2"):
    ludzieLasu = input()
    if ludzieLasu == '1':
        print("Zregenerowales sily i jestes gotowy do dalszej drogi.")
        print()
        time.sleep(1)
        p1.hp = 110
        statystyki()
    elif ludzieLasu == '2':
        print("Kontynuujesz swoja podroz..")
        print()
        time.sleep(1)
        statystyki()
    else:
        print("Bledna odpowiedz.")


time.sleep(1)
kontynuuj()
print("+-------------------------------------+")
print("Wędrujesz przez piaszczyste wybrzeże...")
print("+-------------------------------------+")
time.sleep(1)
kontynuuj()

print("Po drodze trafiasz na opuszczoną wioskę...")
time.sleep(1)
print("Według legend jest ona opętana..")
time.sleep(1)
print("Czy odważysz się wejść w poszukiwaniu skarbów?\n[1] - Szukaj skarbów\n[2] - Lepiej nie kusić losu, kontynuuj podroz")
opuszczonaWioska = ''
while (opuszczonaWioska != "1" and opuszczonaWioska !="2"):
    opuszczonaWioska = input()
    if opuszczonaWioska == '1':
        print("Niczego nie udało się znaleść, ale zacząłeś czuć się dziwnie")
        print()
        time.sleep(1)
        print("...")
        time.sleep(1)
        print()
        print("Na wioskę dawno temu została rzucona klątwa, jestes oslabiony i tracisz 20pkt do ataku..")
        p1.dmg = p1.dmg - 10
    elif opuszczonaWioska == "2":
        print("Spokojnie kontynuujesz droge")
        print()
        time.sleep(1)
    else:
        print("Bledna odpowiedz.")
        print()
        time.sleep(1)

kontynuuj()
print("+------------------------------------------+")
print("Docierasz do mostu nad Turkusowym Kanałem...")
print("+------------------------------------------+")
time.sleep(1)
kontynuuj()

print("+-------------------+")
print("-- Pustkowia Grozy --")
print("+-------------------+")
time.sleep(1)
kontynuuj()

print("Jestes juz blisko konca swojej przygody, przed Tobą ostatnia decyzja do podjęcia..")
print("Mozesz od razu isc na przod i zmierzyc się ze Smokiem Sumed'em - Niszczycielem Życia,..\n..lub odwiedzic Nieznaną Osadę, pamietaj ze nie wiesz co Cie tam czeka..\n")
time.sleep(1)
print("[1] - Zaatakuj Smoka\n[2] - Idz do Nieznanej Osady")

SmokLubOsada = ''

sumastatystyk = p1.hp + p1.dmg + p1.armor

while(SmokLubOsada != "1" and SmokLubOsada != "2"):
    SmokLubOsada = input()
    if SmokLubOsada == "1":
        if sumastatystyk>150:
            print("Po ciezkiej podrozy mimo wszystko wystarczylo Ci sil i udalo Ci sie zabic smoka! Zostales Wybawicielem Vaborgu! Gratulacje!")
        else:
            print("Podroz wycienczyla Cie tak bardzo, ze nie starczylo Ci sil na walke ze smokiem.. Niestety zostales pokonany tak jak wielu innych smialkow..")
    elif SmokLubOsada == "2":
        print("Osada okazala sie byc zamieszkana przez agresywnye Elfy Śnieżne..")
        print()
        time.sleep(1)
        print("Udalo Ci się z nimi wygrać, ale w bitwie straciles polowe swojej zbroi..")
        print()
        time.sleep(1)
        p1.armor = (p1.armor * 1/2)
        statystyki()
        time.sleep(1)
        print("Jestes gotowy zmierzyc się ze smokiem?")
        print()
        kontynuuj()
        print("Ruszyles do walki z Niszczycielem Życia")
        if sumastatystyk>150:
            print("Po ciezkiej podrozy mimo wszystko wystarczylo Ci sil i udalo Ci sie zabic smoka! Zostales Wybawicielem Vaborgu! Gratulacje!")
        else:
            print("Podroz wycienczyla Cie tak bardzo, ze nie starczylo Ci sil na walke ze smokiem.. Niestety zostales pokonany tak jak wielu innych smialkow..")
    else:
        print("Bledna odpowiedz.")



#obozowisko = ''
#             while (obozowisko != "1" and obozowisko != "2"):
#                 obozowisko = input("Trawiasz do obozowiska przyjaznych chłopów")