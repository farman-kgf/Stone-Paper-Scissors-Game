import random as r
n=0
loop ="y"
user_score = 0
computer_score = 0
computer_gusse = r.randint(1,3)
while loop=="y":
    while n<3:
        if computer_gusse == 1:
            computer_choice = "rock"
        elif computer_gusse == 2:
            computer_choice = "paper"
        elif computer_gusse == 3:
            computer_choice = "scissors"
        print("write\n1 for rock\n2 for paper\n3 for scissors")
        user_input = int(input("what do you chose :"))
        if user_input == 1:
            user_choice = "rock"
        elif user_input == 2:
            user_choice = "paper"
        elif user_input == 3:
            user_choice = "scissors"
        else:
            print("invalid input")
        print("Computer chose: ", computer_choice)
        print("you chose: ", user_choice)
        if computer_gusse==1 and user_input==1:
            print("draw")
        elif computer_gusse==1 and user_input==2:
            print("you won round")
            user_score+=1
        elif computer_gusse==1 and user_input==3:
            print("computer won round")
            computer_score+=1
        elif computer_gusse==2 and user_input==1:
            print("computer won round")
            computer_score+=1
        elif computer_gusse==2 and user_input==2:
            print("draw")
        elif computer_gusse==2 and user_input==3:
            print("you won round")
            user_score+=1
        elif computer_gusse==3 and user_input==1:
            print("you won round")
            user_score+=1
            computer_score+=1
        elif computer_gusse==3 and user_input==2:
            print("computer won round")
        elif computer_gusse==3 and user_input==3:
            print("draw")
        n+=1
    print("game over")
    if user_score>computer_score:
        print("your score:",user_score,"computer score:",computer_score)
        print("you won the game")
    elif user_score<computer_score:
        print("your score:",user_score,"computer score:",computer_score)
        print("you lose the game")
    else:
        print("Ohh! game draw")

    loop = input("do you want to play again(y/n) : ")
else:
    print("invalid input")