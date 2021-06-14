from simple_term_menu import TerminalMenu
import sys
import os
import operator
import datetime

print ('''
█▀█ █░█░█ █░░ █▀▀   
█▀▀ ▀▄▀▄▀ █▄▄ █▄█   
''')
print("\n[*] Welcome. Please follow the instructions bellow: ")
print("[*] Select the desired elements you would like to include in your wordlist.")
print("[*] For maximmum efficiency, please include as much information as possible about your target.")
print("[*] Should you not possess any of the requested information, you can skip it by pressing [ENTER]\n")

wife = ("")
wifeb = ("")
wifen = ("")
kid = ("")
kidb = ("")
kidn = ("")
pet = ("")
kids = ("")
kid1 = ("")
kid1b = ("")
kid1n = ("")
kid2 = ("")
kid2b = ("")
kid2n = ("")
kid3 = ("")
kid3b = ("")
kid3n = ("")
company = ("")
companyd = ("")
school = ("")
schoold = ("")
schoold1 = ("")

name = input("> Target's name: ")

if len(name) == 0 or name == " " or name == "  " or name == "   ":
    print("\n[X] You must include a name.")
    print("\n[X] Closing...\n")
    sys.exit()

surname = input("> Surname: ")
nick = input("> Target's nickname: ")
birthdate = input("> Target's birthday (DDMMYYYY): ")
wife = input("> Partner's name: ")
wifen = input("> Partner's nickname: ")
wifeb = input("> Partner's date of birth (DDMMYYYY): ")

kids = input("> How many kids would you like to include? ")
    
if kids == "1":
    kid = input("> Kid's name: ")
    kidn = input("> Kid's nickname: ")
    kidb = input("> Kid's date of birth (DDMMYYYY): ")

if kids == "2":
    kid = input("> Kid's name: ")
    kidn = input("> Kid's nickname: ")
    kidb = input("> Kid's date of birth (DDMMYYYY): ")

    kid1 = input("> Second Kid's name: ")
    kid1n = input("> Second Kid's nickname: ")
    kid1b = input("> Second Kid's date of birth (DDMMYYYY): ")

if kids == "3":
    kid = input("> Kid's name: ")
    kidn = input("> Kid's nickname: ")
    kidb = input("> Kid's date of birth (DDMMYYYY): ")
    
    kid1 = input("> Second Kid's name: ")
    kid1n = input("> Second Kid's nickname: ")
    kid1b = input("> Second Kid's date of birth (DDMMYYYY): ")

    kid2 = input("> Third Kid's name: ")
    kid2n = input("> Third Kid's nickname: ")
    kid2b = input("> Third Kid's date of birth (DDMMYYYY): ")

if kids == "4":
    kid = input("> Kid's name: ")
    kidn = input("> Kid's nickname: ")
    kidb = input("> Kid's date of birth (DDMMYYYY): ")
    
    kid1 = input("> Second Kid's name: ")
    kid1n = input("> Second Kid's nickname: ")
    kid1b = input("> Second Kid's date of birth (DDMMYYYY): ")

    kid2 = input("> Third Kid's name: ")
    kid2n = input("> Third Kid's nickname: ")
    kid2b = input("> Third Kid's date of birth (DDMMYYYY): ")

    kid3 = input("> Fourth Kid's name: ")
    kid3n = input("> Fourth Kid's nickname: ")
    kid3b = input("> Fourth Kid's date of birth (DDMMYYYY): ")

pet = input("> Pet's name: ")
company = input("> Company name: ")
companyd = input("> Year joined: ")
school = input("> School/University: ")
schoold = input("> Year of entry: ")
schoold1 = input("> Year of graduation: ")

words = ['']
oth = input("> Would you like to add any additional keywords? [Y/N]: ")
if oth == "y" or oth == "Y":
    words = input("> Please insert desired keywords separated by commas [e.g.:Air, Fire, Water]: ").split(", ")


print("\n[*] Please wait. Generating wordlist.")

birthdate_yy = birthdate[-2:]
birthdate_yyy = birthdate[-3:]
birthdate_yyyy = birthdate[-4:]
birthdate_xd = birthdate[1:2]
birthdate_xm = birthdate[3:4]
birthdate_dd = birthdate[:2]
birthdate_mm = birthdate[2:4]

wifeb_yy = wifeb[-2:]
wifeb_yyy = wifeb[-3:]
wifeb_yyyy = wifeb[-4:]
wifeb_xd = wifeb[1:2]
wifeb_xm = wifeb[3:4]
wifeb_dd = wifeb[:2]
wifeb_mm = wifeb[2:4]

kidb_yy = kidb[-2:]
kidb_yyy = kidb[-3:]
kidb_yyyy = kidb[-4:]
kidb_xd = kidb[1:2]
kidb_xm = kidb[3:4]
kidb_dd = kidb[:2]
kidb_mm = kidb[2:4]
kid1b_yy = kid1b[-2:]
kid1b_yyy = kid1b[-3:]
kid1b_yyyy = kid1b[-4:]
kid1b_xd = kid1b[1:2]
kid1b_xm = kid1b[3:4]
kid1b_dd = kid1b[:2]
kid1b_mm = kid1b[2:4]

kid2b_yy = kid2b[-2:]
kid2b_yyy = kid2b[-3:]
kid2b_yyyy = kid2b[-4:]
kid2b_xd = kid2b[1:2]
kid2b_xm = kid2b[3:4]
kid2b_dd = kid2b[:2]
kid2b_mm = kid2b[2:4]

kid3b_yy = kid3b[-2:]
kid3b_yyy = kid3b[-3:]
kid3b_yyyy = kid3b[-4:]
kid3b_xd = kid3b[1:2]
kid3b_xm = kid3b[3:4]
kid3b_dd = kid3b[:2]
kid3b_mm = kid3b[2:4]




nameup = name.title()
surnameup = surname.title()
nickup = nick.title()
wifeup = wife.title()
wifenup = wifen.title()
kidup = kid.title()
kidnup = kidn.title()
kid1up = kid1.title()
kid1nup = kid1n.title()
kid2up = kid2.title()
kid2nup = kid2n.title()
kid3up = kid3.title()
kid3nup = kid3n.title()
petup = pet.title()
companyup = company.title()    
companydup = companyd.title()
schoolup = school.title()
schooldup = school.title()
schoold1up = school.title()


wordsup = []
for words1 in words:
    wordsup.append(words1.title())

word = words+wordsup

rev_name = name[::-1]
rev_nameup = nameup[::-1]
rev_nick = nick[::-1]
rev_nickup = nickup[::-1]
rev_wife = wife[::-1]
rev_wifeup = wifeup[::-1]
rev_kid = kid[::-1]
rev_kidup = kidup[::-1]
rev_companydup = companydup[::-1]
rev_schoolup = schoolup[::-1]
rev_schooldup = schoolup[::-1]
rev_schoold1up = schoold1up[::-1]
rev_kid1 = kid1[::-1]
rev_kid1up = kid1up[::-1]
rev_kid2 = kid2[::-1]
rev_kid2up = kid2up[::-1]
rev_kid3 = kid3[::-1]
rev_kid3up = kid3up[::-1]


reverse = [rev_name, rev_nameup, rev_nick, rev_nickup, rev_wife, rev_wifeup, rev_kid, rev_kidup, rev_kid1, rev_kid1up, rev_kid2, rev_kid2up, rev_kid3, rev_kid3up, rev_companydup, rev_schoolup, rev_schooldup, rev_schoold1up]
rev_n = [rev_name, rev_nameup, rev_nick, rev_nickup]
rev_w = [rev_wife, rev_wifeup]
rev_k = [rev_kid, rev_kidup, rev_kid1, rev_kid1up, rev_kid2, rev_kid2up, rev_kid3, rev_kid3up]

bds = [birthdate_yy, birthdate_yyy, birthdate_yyyy, birthdate_xd, birthdate_xm, birthdate_dd, birthdate_mm]

bdss = []

for bds1 in bds:
    bdss.append(bds1)

for bds2 in bds:
    if bds.index(bds1) != bds.index(bds2):
        bdss.append(bds1+bds2)
        for bds3 in bds:
            if bds.index(bds1) != bds.index(bds2) and bds.index(bds2) != bds.index(bds3) and bds.index(bds1) != bds.index(bds3):
                bdss.append(bds1+bds2+bds3)

wbds = [wifeb_yy, wifeb_yyy, wifeb_yyyy, wifeb_xd, wifeb_xm, wifeb_dd, wifeb_mm]

wbdss = []

for wbds1 in wbds:
    wbdss.append(wbds1)
for wbds2 in wbds:
    if wbds.index(wbds1) != wbds.index(wbds2):
        wbdss.append(wbds1+wbds2)
        for wbds3 in wbds:
            if wbds.index(wbds1) != wbds.index(wbds2) and wbds.index(wbds2) != wbds.index(wbds3) and wbds.index(wbds1) != wbds.index(wbds3):
                wbdss.append(wbds1+wbds2+wbds3)


kbds = [kidb_yy, kidb_yyy, kidb_yyyy, kidb_xd, kidb_xm, kidb_dd, kidb_mm, kid1b_yy, kid1b_yyy, kid1b_yyyy, kid1b_xd, kid1b_xm, kid1b_dd, kid1b_mm, kid2b_yy, kid2b_yyy, kid2b_yyyy, kid2b_xd, kid2b_xm, kid2b_dd, kid2b_mm, kid3b_yy, kid3b_yyy, kid3b_yyyy, kid3b_xd, kid3b_xm, kid3b_dd, kid3b_mm]

kbdss = []

for kbds1 in kbds:
    kbdss.append(kbds1)
for kbds2 in kbds:
    if kbds.index(kbds1) != kbds.index(kbds2):
        kbdss.append(kbds1+kbds2)
        for kbds3 in kbds:
            if kbds.index(kbds1) != kbds.index(kbds2) and kbds.index(kbds2) != kbds.index(kbds3) and kbds.index(kbds1) != kbds.index(kbds3):
                kbdss.append(kbds1+kbds2+kbds3)



kombinaac = [pet, petup, company, companyup, school, companyd, schoold, schoold1]

kombina = [name, surname, nick, nameup, surnameup, nickup]

kombinaw = [wife, wifen, wifeup, wifenup, surname, surnameup]

kombinak = [kid, kidn, kidup, kidnup, kid1, kid1n, kid1up, kid1nup, kid2, kid2n, kid2up, kid2nup, kid3, kid3n, kid3up, kid3nup, surname, surnameup]

kombinaa = []
for kombina1 in kombina:
    kombinaa.append(kombina1)
for kombina2 in kombina:
    if kombina.index(kombina1) != kombina.index(kombina2) and kombina.index(kombina1.title()) != kombina.index(kombina2.title()):
        kombinaa.append(kombina1+kombina2)

kombinaaw = []
for kombina1 in kombinaw:
    kombinaaw.append(kombina1)
for kombina2 in kombinaw:
    if kombinaw.index(kombina1) != kombinaw.index(kombina2) and kombinaw.index(kombina1.title()) != kombinaw.index(kombina2.title()):
        kombinaaw.append(kombina1+kombina2)

kombinaak = []
for kombina1 in kombinak:
    kombinaak.append(kombina1)
for kombina2 in kombinak:
    if kombinak.index(kombina1) != kombinak.index(kombina2) and kombinak.index(kombina1.title()) != kombinak.index(kombina2.title()):
        kombinaak.append(kombina1+kombina2)


date = datetime.datetime.today().year
years = ([date - i for i in range(150)])


def concats(seq, start, stop):
    for mystr in seq:
        for num in range(start, stop):
            yield mystr + str(num)



def komb(seq, start):
    for mystr in seq:
        for mystr1 in start:
            yield mystr + str(mystr1)

komb1 = list(komb(kombinaa, bdss))
komb2 = list(komb(kombinaaw, wbdss))
komb3 = list(komb(kombinaak, kbdss))
komb4 = list(komb(kombinaa, years))
komb5 = list(komb(kombinaac, years))
komb6 = list(komb(kombinaaw, years))
komb7 = list(komb(kombinaak, years))
komb8 = list(komb(word, bdss))
komb9 = list(komb(word, wbdss))
komb10 = list(komb(word, kbdss))
komb11 = list(komb(word, years))

komb12 = list(concats(word, 0, 1000))
komb13 = list(concats(kombinaa, 0, 1000))
komb14 = list(concats(kombinaac, 0, 1000))
komb15 = list(concats(kombinaaw, 0, 1000))
komb16 = list(concats(kombinaak, 0, 1000))
komb17 = list(komb(reverse, years))
komb18 = list(komb(rev_w, years))
komb19 = list(komb(rev_k, kbdss))
komb20 = list(komb(rev_n, bdss))
komb21 = list(concats(reverse, 0, 1000))
komb22 = list(komb(school, years))
komb23 = list(komb(company, years))
komb24 = list(komb(school, schoold))
komb25 = list(komb(school, schoold1))

komb_unique1 = list(dict.fromkeys(komb1).keys())
komb_unique2 = list(dict.fromkeys(komb2).keys())
komb_unique3 = list(dict.fromkeys(komb3).keys())
komb_unique4 = list(dict.fromkeys(komb4).keys())
komb_unique5 = list(dict.fromkeys(komb5).keys())
komb_unique6 = list(dict.fromkeys(komb6).keys())
komb_unique7 = list(dict.fromkeys(komb7).keys())
komb_unique8 = list(dict.fromkeys(komb8).keys())
komb_unique9 = list(dict.fromkeys(komb9).keys())
komb_unique10 = list(dict.fromkeys(komb10).keys())
komb_unique11 = list(dict.fromkeys(komb11).keys())
komb_unique12 = list(dict.fromkeys(komb12).keys())
komb_unique13 = list(dict.fromkeys(komb13).keys())
komb_unique14 = list(dict.fromkeys(komb14).keys())
komb_unique15 = list(dict.fromkeys(komb15).keys())
komb_unique16 = list(dict.fromkeys(komb16).keys())
komb_unique17 = list(dict.fromkeys(komb17).keys())
komb_unique18 = list(dict.fromkeys(komb18).keys())
komb_unique19 = list(dict.fromkeys(komb19).keys())
komb_unique20 = list(dict.fromkeys(komb20).keys())
komb_unique21 = list(dict.fromkeys(komb21).keys())

komb_unique22 = list(dict.fromkeys(komb21).keys())
komb_unique23 = list(dict.fromkeys(komb21).keys())
komb_unique24 = list(dict.fromkeys(komb21).keys())
komb_unique25 = list(dict.fromkeys(komb21).keys())

komb_unique01 = list(dict.fromkeys(kombinaa).keys())
komb_unique02 = list(dict.fromkeys(kombinaac).keys())
komb_unique03 = list(dict.fromkeys(kombinaaw).keys())
komb_unique04 = list(dict.fromkeys(kombinaak).keys())
komb_unique05 = list(dict.fromkeys(word).keys())

uniqlist = bdss + wbdss + kbdss + reverse + komb_unique01 + komb_unique02 \
+komb_unique03 + komb_unique04 + komb_unique05 + komb_unique1 + komb_unique2 \
+komb_unique3 + komb_unique4 + komb_unique5 + komb_unique6 + komb_unique7 + komb_unique8 \
+komb_unique9 + komb_unique10 + komb_unique11 + komb_unique12 + komb_unique13 + komb_unique14 \
+komb_unique15 + komb_unique16 + komb_unique17 + komb_unique18 + komb_unique19 + komb_unique20 + komb_unique21 \
+komb_unique22 + komb_unique23 + komb_unique24 + komb_unique25

unique_list = list(dict.fromkeys(uniqlist).keys())

print("\n[*] Please wait...")


f = open ( name+'.txt', 'w' )
f.write (os.linesep.join(unique_list))
f.close()

lines = 0
fcount = open ( name+'.txt', 'r' )
for line in fcount:
    lines += 1

fcount.close()

print("\n[*] Wordlist created. Saved at the present directory as: " + name + ".txt\n")
