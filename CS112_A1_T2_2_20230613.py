# File name : CS112_A1_T2_2_20230613.py


# purpose : Number scrabble is played with the list of numbers between 1 and 9. Each player takes 
# turns picking a number from the list. Once a number has been picked, it cannot be picked 
# again. If a player has picked three numbers that add up to 15, that player wins the game. 
# However, if all the numbers are used and no player gets exactly 15, the game is a draw.


# Author : Mohamed Ashraf Mahmoud Ahmed


# Id : 20230613


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = 0
player2 = 0
# if the summation of one them is 15 , the game ends
player1_attempts=[]
player2_attempts=[]
# those 2 arrays will collect the attempts of the 2 players
def explain_the_game():
    print()
    print("Welcome to Scrabble game")
    print("Scrabble game is played with a list of numbers from 1 to 9")
    print("Each player picks a number from the list and this number can not be picked again")
    print("The player who picks three numbers summed up to 15 is the winner")
    print("if no one gets three numbers summed up to 15, the game is draw ")
def player1_input():
    global player1
    # global so that the variable can be defined in this scope
    player1_number = int(input("Player 1 number: "))


    while not (1 <= player1_number <= 9 and player1_number in my_list):
        print("Please enter a valid number.")
        print()
        player1_number = int(input("Player 1 number: "))
    player1_attempts.append(player1_number)
    # adding the valid number of the player to the array list
    my_list.remove(player1_number)
    # once a number is picked , it is removed from the list
    player1 += player1_number
    return player1
def player2_input():
    global player2
    player2_number = int(input("Player 2 number: "))

    while not (1 <= player2_number <= 9 and player2_number in my_list):
        print("Please enter a valid number.")
        print()
        player2_number = int(input("Player 2 number: "))
    player2_attempts.append(player2_number)
    my_list.remove(player2_number)
    player2 += player2_number
    return player2

def play_the_game():
    explain_the_game()
    counter = 0
    # we will make a counter of 3 iterations to force the player to pick at least 3 numbers
    for x in range(3):
        print()
        print("The available numbers are", my_list)
        print()
        player1_input()
        counter+=1
        if player1==15 and counter==3:
            print()
            print("Player one is the winner")
            break

        # the game will not end unless the player picks 3 numbers

        player2_input()
        if player2==15 and counter==3:
            print()
            print("Player two is the winner")
            break
        if counter==3:    
            # if the two players picked 3 numbers and there is still no winner
            # we will allow another try for both players

            for i in range(1):
                print()
                print("The available numbers are",my_list)
                print()
                player1_input()
                print()
                print( "Player one attempts are",player1_attempts )
                # showing player one his attemps
                print()
                if player1_attempts[0]+player1_attempts[1]+player1_attempts[3]==15 or player1_attempts[1]+player1_attempts[2]+player1_attempts[3]==15 or player1_attempts[0]+player1_attempts[2]+player1_attempts[3]==15:
                    print()
                    # this is because we need only 3 numbers summed up to 15
                    print("Player one is the winner")
                    break
                player2_input()
                print()
                print("Player two attempts are",player2_attempts)
                # showing player two his attempts
                print()
                if player2_attempts[0]+player2_attempts[1]+player2_attempts[3]==15 or player2_attempts[1]+player2_attempts[2]+player2_attempts[3]==15 or player2_attempts[0]+player2_attempts[2]+player2_attempts[3]==15:
                    print()
                    print("Player 2 is the winner")
                    break
                else:
                    # if there is still no winner after the fourth attempt for the both players
                    # player one still has to pick the last number in the list
                    print("Player one still has one more attempt")
                    print()
                    player1_input()
                    print()
                    print("Player one final attempts are",player1_attempts)
                    # showing player one his final attempts
                    print()
                    if player1_attempts[0]+player1_attempts[1]+player1_attempts[4]==15 or player1_attempts[1]+player1_attempts[2]+player1_attempts[4]==15 or player1_attempts[2]+player1_attempts[3]+player1_attempts[4]==15 or player1_attempts[0]+player1_attempts[2]+player1_attempts[4]==15 or player1_attempts[0]+player1_attempts[3]+player1_attempts[4]==15 or player1_attempts[1]+player1_attempts[3]+player1_attempts[4]==15:
                        print("Player one is the winner")
                    else:
                        print()
                        print("No winner , the game is draw")



play_the_game()
while 1 :
    # to allow the players to play again
    print()
    play_again=input("Do you want to play again? ")
    print()
    if play_again=='yes' or play_again=='Yes' or play_again=='YES' or play_again=='YeS' or play_again=='yEs':
        my_list=[1,2,3,4,5,6,7,8,9]
        player1=0
        player2=0
        player1_attempts=[]
        player2_attempts=[]
        play_the_game()
    else:
        print()
        print("Game Over")
        print()
        print("Thank you")
        break


