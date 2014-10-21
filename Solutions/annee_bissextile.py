#!usr/bin/python2
#Public Domain 2014 - Created by N07070
annee_user = input("Please enter a year in the YYYY format >> " )
print("Thanks, and your year is...")
annee_user = int(annee_user)
if annee_user % 4 == 0:
    if annee_user % 100 == 0:
        print("Well, nothing special...")
    else:
        print("Bissextile !")
elif annee_user % 400 == 0:
    print("Bissextile !")
else:
    print("Well, nothing special...")
