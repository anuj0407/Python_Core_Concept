import random
stake = int(input("Enter your stake(in $): "))
goal = int(input("Enter your goal(in $): "))
no_of_times = int(input("Enter no. of times you want to gamble: "))

no_of_win = 0
no_of_loss = 0
amount = stake
no_of_bet = 0
while no_of_times>0:
    bet = 1 # $1
    no_of_bet += 1
    if stake>0 and stake<goal:
        if random.random()<0.5:
            stake -= bet # Lost the bet
            no_of_loss += 1
        else:
            stake += bet # Won the bet
            no_of_win += 1
    elif stake == goal: 
        print("Reached the goal !")
        break
    elif stake < 0:
        print("No money left to gamble")
        break
    
    no_of_times -= 1


win_percentage = (no_of_win/no_of_bet)*100
loss_percentage = (no_of_loss/no_of_bet)*100
print(f"You won {no_of_win} times, and your win percentage is: {win_percentage}")
print(f"You lost {no_of_loss} times, and your loss percentage is: {loss_percentage}")
