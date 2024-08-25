import random 

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll


while True:

    
    players = input("Choose numbers of players (2 - 4): ")   
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4 : 
            break
        else:
             print("Most between 2 - 4")
    else:
        print("Invalid, try again.")    



max_value = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_value:

    for players_idx in range(players):
        print("\n Player ", players_idx + 1 , "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Do you like to roll? (y): ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled 1, turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("Your rolled ", value)

            print("You score is: ", current_score) 
            
        players_scores[players_idx] += current_score
        print("You score is: ", players_scores[players_idx] )

                

