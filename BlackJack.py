# Create Deck and shuffle
import random
import time
deck =[]
player_hand = []
computer_hand = []
total = 0
computer_score = 0

def create_deck(deck):
    suite = ('Spade', 'Hearts','Diamonds','Clubs')
    for a in suite:
        for i in range(1,14):
            deck.append((a,i))
            random.shuffle(deck)    
## Deal player hand (pop, pop)
def deal_cards(player_hand, computer_hand):
    for i in range (1,3):
        player_hand.append(deck.pop())
    
    for i in range(4,6):
        computer_hand.append(deck.pop())
## Display hand
def display_hand(show_hand, name):
    print(name + ' has : ')
    for i in range (0,2):
        if(show_hand[i][1]) == 13:
            print("King of " + str(show_hand[i][0]))
        if(show_hand[i][1]) == 12:
            print("Queen of " + str(show_hand[i][0]))
        if(show_hand[i][1]) == 11:
            print("Jack of " + str(show_hand[i][0])) 
        elif (show_hand [i][1]) < 11:
            print(str(show_hand[i][1]) + " of " + str(show_hand[i][0]))
    time.sleep(.5)
    print('For a total of ' + str(current_score(show_hand)))



def hit(card_hand1, deck, person):
    card_hand1.append(deck.pop())
    print (person + " at "  + str(current_score(card_hand1)))  
## Current Score 
def current_score (card_hand):
    total = 0
    for i in  range((len(card_hand))):
        total +=(int(card_hand[i][1]))
    return(total)
## Check bust (Putting this in the loop not as a function)
##def bust(card_hand2):
  #  if (current_score(card_hand2)) > 22:
   #     print("Bust! ")
#        return 
#   3if (current_score(card_hand2)) < 21:
#   print("Awesome")  
def score(player_hand2, computer_hand2):
	if (current_score(player_hand2) == 21):
		print ("Blackjack.")
	elif (current_score(computer_hand2) == 21):
		print ("Dealer Blackjack.")
	elif (current_score(player_hand2) > 21):
		print ("You busted.")
	elif (current_score(computer_hand2) > 21):
		print ("Dealer buster")
	elif (current_score(player_hand) < current_score(computer_hand)):
		print ("Sorry. You are lowers. You lose.")
	elif (current_score(player_hand) > current_score(computer_hand)):
		print ("Congrats you won")
        
## Evaulate dealers hand (Stand on 17)
## Evaluate winner, show hands
## Play again or notsss

def game():
    choice =""
    create_deck(deck)
    deal_cards(player_hand, computer_hand)
    display_hand(player_hand, "Player")
    display_hand(computer_hand, "Dealer")
    while choice != "q" :
        print('Do you want to Hit , Stand , or Quit?')
        choice = input()
        if choice == "h" :
            hit(player_hand,deck, "you")
            while current_score(computer_hand) < 17:
                hit(computer_hand, deck, "dealer")
            display_hand(player_hand, "Player")
            display_hand(computer_hand, "Dealer")
            score(player_hand,computer_hand)
            exit()
        elif choice == "s":
            while current_score(computer_hand) < 17:
                hit(computer_hand, deck, "dealer")
            display_hand(player_hand, "Player")
            display_hand(computer_hand, "Dealer")
            score(player_hand,computer_hand)
            exit()
        elif choice == "q":
            exit()

    


game()