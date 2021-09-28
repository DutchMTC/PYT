import time

print("Eet je in de ochtend ontbijt? (j/n)")
x = input()
if x == "j":
    print("Nice, eet je wel genoeg? (j/n)")
    y = input()
    if y == "j":
        print("Goedzo!")
    if y == "n":
        print("Wel genoeg eten he >:(")
elif x == "n":
    print("Ik ook niet tbh...")
else:
    print("Dat was geen optie >:(")

time.sleep(2)

print("")
print("Krijg je genoeg slaap in de nacht? (j/n)")
a = input()
if a == "j":
    print("Beter ook maar, slapen is belangrijk.")
elif a == "n":
    print("What can I say except studenten...")
else:
    print("Dat was geen optie >:(")

time.sleep(2)

print("")
print("Geef jij ook veels te veel geld uit aan eten? (j/n)")
b = input()
if b == "j":
    print("welja.. je leeft maar 1 keer.")
elif b == "n":
    print("I'm proud of u. I could never.")
else:
    print("broer dat was geen antwoord")

time.sleep(2)

print("")
print("Wat is 9+10?")
c = input()
if c == "21":
    print("A true memer I see...")
elif c == "19":
    print("disappointed...")
else:
    print("ben je dom")

time.sleep(2)

print("")
print("Hoe laat ga je meestal slapen? (20:00, 21:00, 22:00, etc.)")
d = input()
if d == "19:00":
    print("serieus?? zo")
elif d == "20:00":
    print("waarom zo vroeg.")
elif d == "21:00":
    print("vroeg, maar opzich acceptabel.")
elif d == "22:00":
    print("not too bad")
elif d == "23:00":
    print("opzich wel te doen, weinig slaap tho")
elif d == "00:00":
    print("ok... op t nippertje dan")
elif d == "1:00":
    print("wat doe je met je leven")
elif d == "2:00":
    print("why, just why.")
else:
    print("ga slapen")