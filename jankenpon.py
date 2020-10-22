import random

def validate(hand):
    if hand < 0 or hand > 2:
        return False
    else:
        return True

def handshape(hand, name):
    hands = ['Rock', 'Paper', 'Scissors']
    print(name + ' picked: ' + hands[hand])

def battle(player, computer):
    if player == computer:
        return 'Draw'
    elif player == 0 and computer == 1:
        return 'You Lose...'
    elif player == 1 and computer == 2:
        return 'You Lose...'
    elif player == 2 and computer == 0:
        return 'You Lose...'
    else:
        return 'You Win!!'

def main():
    print(
    """
    \n \U0000270A \U0001F590 \U0000270C ====== WELCOME TO JANKENPON GAME ====== \U0000270C \U0001F590 \U0000270A
    """)
    player_name = input('Please enter your name: ')

    print('\nPick a hand: (0: Rock, 1: Paper, 2: Scissors)')

    player_handshape = None
    while True:
        try:
            player_handshape = int(input('Please enter a number (0-2): '))
        except ValueError:
            print('Please input valid number')
            continue
        else:
            break

    if validate(player_handshape):
        computer_handshape = random.randint(0, 2)
        print('\n')
        handshape(player_handshape, player_name)
        handshape(computer_handshape, 'Computer')
        result = battle(player_handshape, computer_handshape)
        print('\nResult: ' + result)

    else:
        while True:
            print("Please input valid number")
            while True:
                try:
                    player_handshape = int(input('Please enter a number (0-2): '))
                except ValueError:
                    print('Please input valid number')
                    continue
                else:
                    break
            if validate(player_handshape):
                computer_handshape = random.randint(0, 2)
                print('\n')
                handshape(player_handshape, player_name)
                handshape(computer_handshape, 'Computer')
                result = battle(player_handshape, computer_handshape)
                print('\nResult: ' + result)
                break

if __name__ == '__main__':
    main()

while True:
    while True:
        again = str(input('Play again? (y/n): '))
        if again in ('y', 'n'):
            break
        print('Invalid input')
    if again == 'y':
        main()
    else:
        print('\nThank you for playing JANKENPON game!')
        print('See you later!')
        break
