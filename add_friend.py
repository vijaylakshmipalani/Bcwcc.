# importing spy and existing friends
from spy_details import Spy, friends
# importing regular expressions for proper validation
import re

# importing termcolor for colorful output
# from termcolor import colored

# function to add new friends.
def add_friend():
    # using class spy
    new_friend = Spy(" ", " ", 0, 0.0)

    # ask user for name and salutation of friend
    new_friend.name = input("Please add your friend's name: ")
    pattern_n = '^[a-zA-Z\s]+$'
    # user validation.
    if(len(new_friend.name) > 0 and re.match(pattern_n,new_friend.name)!=None):
        if(len(new_friend.name)>20):
            print("Your name is too big.")
    else:
        print("Name should be alphabetic")
        return add_friend()

    new_friend.salutation= input("What to call Mr. or Ms.?: ")
    pattern_s = '^[a-zA-Z\s]+$'
    # user validation
    if(len(new_friend.salutation) >0 and re.match(pattern_s,new_friend.salutation) != None):
        if(len(new_friend.salutation)>5):
            print("Your salutation is too big.")
    else:
        print("Salutation should be alphabetic")
        return add_friend()


    # concatination for full name
    new_friend.name = new_friend.salutation + " " + new_friend.name

    # ask for age of friend
    new_friend.age = (input("Age? "))
    pattern_a = '^[0-9]+$'
    # user validation
    if(re.match(pattern_a,new_friend.age)!=None):
        if(12 < new_friend.age < 50):
            True
        else:
            print ("Age should be in beetween 12 to 50")
    else:
        print ("Age should be Numeric.")
        return add_friend()

    #ask for rating of friend, float represents type casting in float
    new_friend.rating = (input("Spy rating? "))
    # user validation.
    pattern_r = '^[0-9]+\.[0-9]+$'
    if(re.match(pattern_r,new_friend.rating)!= None):
        if (new_friend.rating>0.0):
            True
        else:
            print ("Ratting should be more than 0.0")
    else:
        print ("Ratting should be Numeric or Decimal.")
        return add_friend()


    # add friend if conditions satisfies
    friends.append(new_friend)
    print ('Friend Added!')

    # returning total no of friends.
    return len(friends)