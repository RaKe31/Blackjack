import random
playerIn = True
dealerIn = True
deck = [2,3,5,6,7,8,9,10,2,3,5,6,7,8,9,10,2,3,5,6,7,8,9,10,2,3,5,6,7,8,9,10,'A','K','Q','J','A','K','Q','J','A','K','Q','J','A','K','Q','J']
playerHand = []
dealerHand = []
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

def total(turn):
    total = 0
    face =['J','Q','K']
    for card in turn:
        if card in range(1,11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    if len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)
print(dealerHand)
print(playerHand)
while playerIn or dealerIn:
    print(f"dealer had {revealDealerHand()} and X")
    print(f"you  had {playerHand} for a total of {total(playerHand)} and  X")
    if playerIn:
        stayOrHit = input('1:stay\n 2:hit\n')
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '1':
        playerIn == False
    else:
        dealCard(playerHand)
    if total(playerHand) > 21:
        break
    elif total(dealerHand) > 21:
        break
if total(playerHand) == 21:
    print(f"\n you have {playerHand} for a total of 21 and the dealer has {dealerHand} for the total of {total(dealerHand)}")
    print("Blackjack You win")
elif total(dealerHand) == 21:
    print(f"\n you have {playerHand} for a total of 21 and the dealer has {dealerHand} for the total of {total(dealerHand)}")
    print("Blackjack Dealer win")
elif total(playerHand) > 21:
    print(f"\n you have {playerHand} for a total of 21 and the dealer has {dealerHand} for the total of {total(dealerHand)}")
    print("You busts Dealer win")
elif total(dealerHand) > 21:
    print(f"\n you have {playerHand} for a total of 21 and the dealer has {dealerHand} for the total of {total(dealerHand)}")
    print("Dealer busts you win")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\n you have {playerHand} for a total of 21 and the dealer has {dealerHand} for the total of {total(dealerHand)}")
    print("Dealer win")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\n you have {playerHand} for a total of 21 and the dealer has {dealerHand} for the total of {total(dealerHand)}")
    print("You win")

