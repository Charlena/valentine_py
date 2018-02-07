import time
import sys
from textwrap import dedent

class love_song():
    def song (self):
        print("""
        Cause after all this time
        I'm still into you
        I should be over all the butterflies but I'm into you, I'm into you
        And even baby our worst nights
        I'm into you, I'm into you
        Let 'em wonder how we got this far,
        'Cause I don't really need to wonder at all
        Yeah, after all this time
        I'm still into you""")

class other_love_song():
    def next_song(self):
        
        print("""Together can never be close enough for me
        Feel like I am close enough to you
        You wear white and I'll wear out the words I love you
        And you're beautiful
        Now that the wait is over
        And love and has finally shown her my way
        Marry me
        Today and every day
        Marry me
        If I ever get the nerve to say hello in this cafe
        Say you will
        Mm-hmm
        Say you will
        Mm-hmm""")
        

print("Ready to find your true love?")

# wait for 5 seconds
time.sleep(5)

print("How much do you care about looks? On a scale of 1 to 10.")
scale = int(input("> "))

if scale <= 7:
    print(f"So your in this for the right reasons I see, you said {scale}.")
    print("Door 1 has been opened for you")
elif scale == 5:
    print(f"Hmm interesting...You chose {scale}")
    print("Door 1 has been opened for you")
else:
    if scale >= 8:
        print(f"I see you're very shallow you chose {scale}, but I wont judge.")
        print("Door 2 has been opened for you.")
        print("The mystery woman behind the doors doesn't believe you're attractive enough..")
        print("I guess you should both come back  when you're more mature.")
    else:
        print("It's really not hard just pick a number from 1 to 10 man!")

    sys.exit(0)

print("You have entered door 1")
print("Door 1 holds two very attractive women")
print("""The first woman is very smart not as attractive but still beautiful
 loves sports but has a addiction to shopping and owns her own
 business and never wants to have kids""")
print(dedent("""
    The second woman is also very smart very attractive hates sports is 
    not interested in long term relationship but looking for
    for something new also owns her own business and has a 2 year old son"""))
print("Please pick either the first or second number")
woman = int (input("> "))
if woman == 1:
    print("Great she's seems like a match for you!")
    print("Go on a first date")
    print("You fall in love")
    print("Then she kisses your bestfriend......")
    print("What do you do?")
    print("Stay with her, leave, kiss her bestfriend, forgive and forget?")
    choice = input("> ")
    if choice == "stay":
        print("You're a trooper and stupid but good luck cause she's pregnant by your cousin....")
    elif choice == "kiss":
        print("You sneaky bastard but good choice, you guys break up soon after..")
    elif choice == "forgive":
        print("Everything works out you guys live happily ever after")
        love_song().song()
    else:
        print("Now your single. See don't")
        sys.exit(0)

if woman == 2:
    print("You don't click right away but you decide to go on a date.")
    print("Your first date goes well")
    print("Do you decide to invite her to your house")
    print("Type yes or no")
    answer = input("> ")
    if answer == "yes":
        print("""You cook dinner for her she loves the meal and 
        ask to have a glass of wine with you""")
        print("Do you say yes or no?")
        des = input("> ")
        if des == "yes":
            print("""You have a glass a wine and you start get 
            a bit more relaxed""")
            print("She ends up spending the night")
            print("""You wake up next to each other and realize 
            you want to wake up next to each other like this forever...""")
        elif des == "no":
            print("""You dummy! But a gentleman you lead her to
            her car and send her off for the night""")
            print("You have your first kiss")
            print("You guys continue to date and fall in love ")

        other_love_song().next_song()

    elif answer == "no":
        print("Ok, well you just missed out on the love of your life..")
    else:
        print("Thanks, Goodbye now.")
