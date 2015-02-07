#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

def days_limit():
    jour = 1
    jour_lim = int(input("Please input how many days you would like to cycle. >> "))
    nbr_friends = 2
    nbr_nvx_friends = 2
    while jour <= jour_lim:
        nbr_friends = nbr_nvx_friends*2
        nbr_nvx_friends = nbr_nvx_friends*2
        jour += 1
        print("On the "+str(jour)+" th day, John has "+str(nbr_friends)+" friends.")

def friends_limit():
    jour = 1
    friends_lim = int(input("How many friends would you like John to have ? >> "))
    nbr_friends = 2
    nbr_nvx_friends = 2
    while nbr_friends <= friends_lim:
        nbr_friends = nbr_nvx_friends*2
        nbr_nvx_friends = nbr_nvx_friends*2
        jour += 1
    print("It would take "+str(jour)+" days for John to have "+str(friends_lim)+" friends.")

def friends_10():
    jour = 1
    friends_lim = int(input("How many friends would you like John to have ? >> "))
    nbr_friends = 2
    nbr_nvx_friends = 2
    while nbr_friends <= friends_lim:
        nbr_friends = nbr_nvx_friends*10
        nbr_nvx_friends = nbr_nvx_friends*10 
        jour += 1
    print("It would take "+str(jour)+" days for John to have "+str(friends_lim)+" friends.")
    
def main():
    user_choice = int(input("Would you to know : \n 1 - How many friend John will have in X days ? \n 2 - How many days will it take John to have X friends ? \n 3 -How many days will it take John to have X friends by gaining 10 friends per new friend ? \nPlease enter a number >> "))

    if user_choice == 1:
        days_limit()
    elif user_choice == 2:
        friends_limit()
    elif user_choice == 3:
        friends_10()
    else:
        print("Okay then...")

if __name__ == '__main__':
    main()