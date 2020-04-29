# class Card - lists cards and suits required for generating all cards in the deck.
# class Chips - lists the amount of chips the player has
# class Deck - creates and shuffles the cards in the deck (needs the card class).
# class Player - contains the player's name, win count, and current drawed cards(2). 
# class Game - contains the game's rules, dealers plays and keeps scores on the bets (needs the player, deck class).

from random import shuffle
import re

class Card:
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'] #values = number; figures = 10; ace = 1 or 10
    def __init__ (self, value, suit):
        self.suit = suit
        self.value = value
    def __repr__ (self):
            return self.values[self.value] + ' of ' + self.suits[self.suit] 
    def __lt__ (self,other): 
        if self.value < other.value:
            return True
        return False
    def __gt__ (self,other):
        if self.value > other.value:
            return True
        return False
        
class Deck:
    def __init__ (self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def remove_card (self):
        if len (self.cards) == 0:
            return None
        return self.cards.pop()
    def card_print(self):
        self.spades = ['┏━━━━━━━┓','┃ ♠   ♠ ┃','┃       ┃', '┃   {}  ┃', '┃       ┃', '┃ ♠   ♠ ┃', '┗━━━━━━━┛']
        self.hearts = ['┏━━━━━━━┓','┃ ♥   ♥ ┃','┃       ┃', '┃   {}  ┃', '┃       ┃', '┃ ♥   ♥ ┃', '┗━━━━━━━┛']
        self.diamonds = ['┏━━━━━━━┓','┃ ♦   ♦ ┃','┃       ┃', '┃   {}  ┃', '┃       ┃', '┃ ♦   ♦ ┃', '┗━━━━━━━┛']
        self.clubs = ['┏━━━━━━━┓','┃ ♣   ♣ ┃','┃       ┃', '┃   {}  ┃', '┃       ┃', '┃ ♣   ♣ ┃', '┗━━━━━━━┛']
        self.print_spades = print(clubs)
        self.print_hearts = print(hearts)
        self.print_diamonds = print(diamonds)
        self.print_clubs = print(clubs)
            
class Chips:
    def __init__ (self):
        chips = ['5', '10', '20', '50', '100'] #30 chips of each type
        chips_total = sorted(chips * 30)
        self.chips = chips_total
            
class Player:
    def __init__ (self, name):
        self.wins = 0
        self.card1 = None
        self.card2 = None
        self.extra_card = None
        self.name = name
        
class Dealer:
    def __init__ (self):
        self.wins = 0
        self.card1 = None
        self.card2 = None
        
class Game:
    def __init__ (self):
        print('Welcome to Python Blackjack!\n')
        name = input('Please insert your player name: ')
        self.deck = Deck()
        self.stash = Chips() 
        self.player = Player(name)
        self.dealer = Dealer()         
    def play_game (self):
        cards = self.deck.cards
        chips = self.stash.chips
        stash_int = [int(i) for i in chips]
        stash_total = 0 
        for chip in range(0, len(stash_int)): 
            stash_total = stash_total + stash_int[chip]
        print('\nWelcome {}! Your starting chips amount is {} €'.format(self.player.name, stash_total))
        pot = []
        turn = None
        while turn != 'q':
            turn = input('\nPress q to quit. Any other key to play. ')
            while len(cards) >= 2 and chips != []:
                if turn == 'q':
                    break
                bet_amount = input('\nPlace your bet (5, 10, 20, 50 or 100 [€]). ')
                pot.append(self.stash.chips.pop(self.stash.chips.index(bet_amount)))
                stash_total -= int(bet_amount)
                pot = [str(int(bet_amount)*2)] #if player wins, pot empties a double chip ---> wins x2 the amount bet
                p_card1 = str(self.deck.remove_card())
                p_card2 = str(self.deck.remove_card())
                dealer_card1 = str(self.deck.remove_card())
                print('\n{} drew a {} and a {}'.format(self.player.name, p_card1, p_card2))
                print('\nThe dealer drew a {}'.format(dealer_card1))
                if 'Jack' in p_card1:     ####RESUMIR####
                    card1_extract = ['10']
                elif 'Queen' in p_card1:
                    card1_extract = ['10']
                elif 'King' in p_card1:
                    card1_extract = ['10']
                else:
                    card1_extract = re.findall(r'\d+',str(p_card1))
                if 'Jack' in p_card2:
                    card2_extract = ['10']
                elif 'Queen' in p_card2:
                    card2_extract = ['10']
                elif 'King' in p_card2:
                    card2_extract = ['10']
                else:
                    card2_extract = re.findall(r'\d+',str(p_card2))   ####RESUMIR####
                if 'Ace' in p_card1:
                    ace_value = input('\nPlease choose the Ace\'s value (1 or 11): ')     ####RESUMIR####
                    card1_extract = ['{}'.format(ace_value)]
                if 'Ace' in p_card2:
                    ace_value = input('\nPlease choose the Ace\'s value (1 or 11): ')
                    card2_extract = ['{}'.format(ace_value)]
                card1_value = int(card1_extract[0])
                card2_value = int(card2_extract[0])
                hand_value = card1_value + card2_value
                print('\nYour current card score is {}'.format(hand_value))
                if hand_value == 21: 
                    print('\n{} got a Blackjack and won the round, as well as {} euros from the pot!'.format(self.player.name, pot[0])) 
                    self.stash.chips.append(pot.pop(0))
                    stash_total += int(bet_amount)*2
                    print('\nStash total: {}'.format(stash_total))
                    self.player.wins += 1
                    turn = input('\nPress q to quit. Any other key to play. ') # melhorar
                    if turn == 'q':
                        break
                else:
                    while hand_value <= 21: 
                        play = input('\nDo you wanna hit or stand ? ')
                        if 'hit' in play:
                            extra_card = str(self.deck.remove_card())
                            print('\n{} drew a {}'.format(self.player.name, extra_card))
                            if 'Jack' in extra_card:     ####RESUMIR####
                                excard_extract = ['10']
                            elif 'Queen' in extra_card:
                                excard_extract = ['10']
                            elif 'King' in extra_card:
                                excard_extract = ['10']
                            else:
                                excard_extract = re.findall(r'\d+',str(extra_card))
                            if 'Ace' in extra_card:
                                ace_value = input('\nPlease choose the Ace\'s value (1 or 11): ')     
                                excard_extract = ['{}'.format(ace_value)]
                            excard_value = int(excard_extract[0])
                            hand_value += excard_value
                            print('\nYour current card score is {}'.format(hand_value))
                        elif 'stand' in play:
                            print('\n{}\'s final score for this round: {}'.format(self.player.name, hand_value))
                            dealer_card2 = str(self.deck.remove_card())
                            print('\nThe dealer drew a {}'.format(dealer_card2))
                            if 'Jack' in dealer_card1:     ####RESUMIR####
                                dc1_extract = ['10']
                            elif 'Queen' in dealer_card1:
                                dc1_extract = ['10']
                            elif 'King' in dealer_card1:
                                dc1_extract = ['10']
                            else:
                                dc1_extract = re.findall(r'\d+',str(dealer_card1))
                            if 'Jack' in dealer_card2:
                                dc2_extract = ['10']
                            elif 'Queen' in dealer_card2:
                                dc2_extract = ['10']
                            elif 'King' in dealer_card2:
                                dc2_extract = ['10']
                            else:
                                dc2_extract = re.findall(r'\d+',str(dealer_card2))   ####RESUMIR####
                            if 'Ace' in dealer_card1:
                                dc1_extract = ['11']
                                if 'Ace' in dealer_card2:
                                    dc2_extract = ['1']
                            elif 'Ace' in dealer_card2:
                                dc2_extract = ['11']
                            dc1_value = int(dc1_extract[0])
                            dc2_value = int(dc2_extract[0])
                            dealer_hand = dc1_value + dc2_value                    
                            while dealer_hand <= 16:
                                exdl_card = str(self.deck.remove_card())
                                print('\nThe dealer drawns another card. It\'s {}'.format(exdl_card))
                                if 'Jack' in exdl_card:     ####RESUMIR####
                                    exdl_extract = ['10']
                                elif 'Queen' in exdl_card:
                                    exdl_extract = ['10']
                                elif 'King' in exdl_card:
                                    exdl_extract = ['10']
                                elif 'Ace' in exdl_card:
                                    if dealer_hand + 11 >= 17 and dealer_hand + 11 <= 21:
                                        exdl_extract = ['11']
                                    else:
                                        exdl_extract = ['1']
                                else:
                                    exdl_extract = re.findall(r'\d+',str(exdl_card))
                                exdl_value = int(exdl_extract[0])
                                dealer_hand += exdl_value
                                break
                            print('\nDealer\'s final score for this round: {}'.format(dealer_hand))
                            if dealer_hand > 21:             
                                print('\nDealer bust! {} wins this round'.format(self.player.name))
                                self.stash.chips.append(pot.pop(0))
                                stash_total += int(bet_amount)*2
                                print('\nStash total: {}'.format(stash_total))
                                self.player.wins += 1
                                turn = input('\nPress q to quit. Any other key to play. ') # melhorar
                                if turn == 'q':
                                    break
                                break
                            if hand_value > dealer_hand: 
                                print('\n{}\'s card total: {}'.format(self.player.name, str(hand_value)))       
                                print('\n{} won the round and {} euros from the pot!'.format(self.player.name, pot[0]))
                                self.stash.chips.append(pot.pop(0))
                                stash_total += int(bet_amount)*2
                                print('\nStash total: {}'.format(stash_total))
                                self.player.wins += 1
                                turn = input('\nPress q to quit. Any other key to play. ') # melhorar
                                if turn == 'q':
                                    break
                                break
                            elif hand_value < dealer_hand:
                                print('\n{}\'s card total: {}'.format(self.player.name, str(hand_value)))
                                print('\nDealer\'s card total: {}'.format(str(dealer_hand)))
                                pot = ['{}'.format(bet_amount)]
                                print('\n{} lost the round and {} euros from the stash'.format(self.player.name, pot[0]))
                                pot.append(self.stash.chips.pop(self.stash.chips.index(bet_amount)))
                                print('\nStash total: {}'.format(stash_total))
                                pot = []
                                self.dealer.wins += 1
                                turn = input('\nPress q to quit. Any other key to play. ') # melhorar
                                if turn == 'q':
                                    break
                                break
                            else:           #hand_value = dealer_hand
                                print('\n{}\'s card total: {}'.format(self.player.name, str(hand_value)))
                                print('\nDealer\'s card total: {}'.format(str(dealer_hand)))
                                print('\nThis round is a tie ! {} loses the round and gets the bet amount back'.format(self.player.name))
                                self.dealer.wins += 1
                                pot = [str(int(bet_amount))]
                                self.stash.chips.append(pot.pop(0))
                                stash_total += int(bet_amount)
                                print('\nStash total: {}'.format(stash_total))  
                                turn = input('\nPress q to quit. Any other key to play. ') # melhorar
                                if turn == 'q':
                                    break
                                break
                    if hand_value > 21:            
                        pot.append(self.stash.chips.pop(self.stash.chips.index(bet_amount)))
                        pot = ['{}'.format(bet_amount)]
                        print('\nBust! {} lost the round and {} euros from the pot'.format(self.player.name, pot[0]))
                        print('\nStash total: {}'.format(stash_total))
                        pot = []
                        self.dealer.wins += 1
                        turn = input('\nPress q to quit. Any other key to play. ') # melhorar
                        if turn == 'q':
                            break
                        break
            print('\nThe game is over! Let\'s check the final score!\n')
            print('{}\'s rounds won: {}\n'.format(self.player.name, self.player.wins))
            print('The dealer\'s rounds won: {}\n'.format(self.dealer.wins))
            print('\nYour stash total is {}\n'.format(stash_total))
            print('{}! Thanks for playing!\n'.format(self.winner(self.player)))
            quit() 
    def winner(self, player):
        if player.wins > self.dealer.wins:
            return '{} won the game'.format(player.name)
        if player.wins < self.dealer.wins:
            return 'The dealer won the game'
        return 'It was a tie'
    
game = Game()
game.play_game()


#EXTRA:
#mostrar dinheiro no stash (transformar os strings de cada ficha e somá-los)
#gráficos das cartas na mesa

#VERIFICAÇÕES FINAIS:
# player hand = 21 -----> blackjack (CORRE)
# stand:
# dealer_hand > 21 -----> dealer bust 
# hand_value > dealer_hand ----> player wins round (CORRE)
# hand_value < dealer_hand ----> dealer wins round (CORRE)
# hand_value = dealer_hand ----> tie, player loses round (CORRE)
# hand_value > 21 ------> player bust (CORRE)
# game ends ------> winner is the player or dealer with most rounds won (CORRE)



                    
        
