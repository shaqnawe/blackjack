import random
suits = ['\u2666','\u2665','\u2663','\u2660']
values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return (f'{self.value} of {self.suit}')

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(Card(suit,value))
    def __str__(self):
        deck_of_cards = ''
        for card in self.deck:
            deck_of_cards += '\n'+card.__str__()
        return "The deck has:" + deck_of_cards
    # Method to shuffle deck    
    def shuffle(self):
        if len(self.deck) > 1:
            random.shuffle(self.deck)
    # Method to deal a card
    def deal_one(self):
        if len(self.deck) > 1:
            single_card = self.deck.pop()
            return single_card
# deck = Deck()
# deck.shuffle()
# print(deck.deal_one())

class Player:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.dealer = False
    # Add card to cards list
    def add_card(self, card):
        self.cards.append(card)
        # self.value = card.value
    def score(self):
        self.total = 0
        for card in self.cards:
            self.total += int(card.value)
            # print(f'total is: {self.total}')
        return self.total
    def display_cards(self):
        if self.dealer:
            print("First card hidden")
            print(self.cards[1])
        else:
            for card in self.cards:
                print(card)
            print("Your Total is:", self.score())
# player = Player()
# player.add_card(deck.deal_one())
# print(player.score())

class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.dealer = True

# dealer = Dealer()
# dealer.add_card(deck.deal_one())
# dealer.add_card(deck.deal_one())
# print(dealer.score())

class Human(Player):
    def __init__(self):
        super().__init__()

# human = Human()
# human.add_card(deck.deal_one())
# human.add_card(deck.deal_one())
# print(human.score())

class Game:
    def __init__(self):
        pass
    def play(self):
        # Flag to start the game
        playing = True
        while playing:
            # Instantiate Card class
            self.card = Card(suits, values)
            # Instantiate Deck class
            self.deck = Deck()
            # Shuffle deck of cards
            self.deck.shuffle()
            # Instantiate Player parent class
            self.player = Player()
            # Instantiate Human subclass
            self.human = Human()
            # Instantiate Dealer subclass
            self.dealer = Dealer()

            for i in range(2):
                self.dealer.add_card(self.deck.deal_one())
                self.human.add_card(self.deck.deal_one())
            
            # Display cards drawn for Dealer and Player
            self.dealer.display_cards()
            print()
            self.human.display_cards()
            #Set a flag to stop game
            game_over = False
            while not game_over:
                # Check if either dealer or player hits Blackjack
                dealer_hit_blackjack, human_hit_blackjack = self.is_blackjack()
                if dealer_hit_blackjack or human_hit_blackjack:
                    game_over = True
                    self.show_result(dealer_hit_blackjack, human_hit_blackjack)
                    continue
                user_choice = input("Would you like to [Hit / Stand]").lower()
                while user_choice not in ['h', 'hit', 's', 'stand']:
                    user_choice = input(f'Please enter h / s or hit / stand').lower()
                if user_choice == 'h' or 'hit':
                    self.human.add_card(self.deck.deal_one())
                    self.human.display_cards()
                    if self.player_loses():
                        print("You Lose :(")
                        game_over = True
                else:
                    player_card_total = self.human.score()
                    dealer_card_total = self.dealer.score()

                    print("Final Results")
                    print("Your score:", player_card_total)
                    print("Dealer Score:", dealer_card_total)

                    if player_card_total > dealer_card_total and player_card_total <= 21:
                        print("You Win!")
                    elif player_card_total == dealer_card_total:
                        print("It's a Draw!")
                    else:
                        print("You Lose :(")
                    game_over = True
                
            # Ask the user if they want to play again
            second_try = input("Would you like to play again? [Y/N]").lower()
            while second_try not in ['y','n']:
                second_try =  input("Please enter Y or N ").lower
            if second_try == 'n':
                print("Thanks for playing")
                playing = False
            else:
                game_over = False
    def player_loses(self):
        if self.human.score() > 21:
            return True
    # Check if Player or Dealer has Blackjack
    def is_blackjack(self):
        human = False
        dealer = False
        if self.human.score() == 21:
            human = True
        if self.dealer.score() == 21:
            dealer = True
        return human, dealer
    # Show result of game
    def show_result(self, player_hit_blackjack, dealer_hit_blackjack):
        if player_hit_blackjack:
            print(f'Player has blackjack! You Win!')
        elif dealer_hit_blackjack:
            print("Dealer has blackjack! You Lose :(")
        elif player_hit_blackjack and dealer_hit_blackjack:
            print(f'Both players have blackjack! It\'s a Draw!')

def main():
    start_game = Game()
    start_game.play()
main()