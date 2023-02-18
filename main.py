from second import second_time
from third import third_time
print("                             Alice In Boaderland -> Beauty Contest")
print()
marks_list = [0,0,0,0,0]
Round = 1
while True:
    #Taking players inputs
    try:
        player1 = int(input("Player 1) Enter a number between 0 - 100: "))
        if player1 < 0 or player1 > 100:
            print("Enter a number between 0 and 100")
            continue
        player2 = int(input("Player 2) Enter a number between 0 - 100: "))
        if player2 < 0 or player2 > 100:
            print("Enter a number between 0 and 100")
            continue
        player3 = int(input("Player 3) Enter a number between 0 - 100: "))
        if player3 < 0 or player3 > 100:
            print("Enter a number between 0 and 100")
            continue
        player4 = int(input("Player 4) Enter a number between 0 - 100: "))
        if player4 < 0 or player4 > 100:
            print("Enter a number between 0 and 100")
            continue
        player5 = int(input("Player 5) Enter a number between 0 - 100: "))
        if player5 < 0 or player5 > 100:
            print("Enter a number between 0 and 100")
            continue
    except ValueError as e:
        print("Please Enter a number between 0 - 100")
        break
    print()
    print("------------------------------Round:- "+str(Round)+"------------------------------------")
    print("Player 1       Player 2       Player 3       Player 4       Player 5")
    print("---------------------------------------------------------------------------")
    print("  "+str(player1)+"              "+str(player2)+"             "+str(player3)+"            "+str(player4)+"             "+str(player5))
    Round = int(Round)

    #taking average
    avg = (player1 + player2 + player3 + player4 + player5) / 5
    death_num = avg * 0.8
    #print("Death number is: {:.2f}".format(death_num))
    #print("                         Death number is: "+str(round(death_num,2)))

    #Gap between player 1 and death number
    player1_gap = player1 - death_num
    player1_gap = abs(player1_gap)

    #Gap between player 2 and death number
    player2_gap = player2 - death_num
    player2_gap = abs(player2_gap)

    #Gap between player 3 and death number
    player3_gap = player3 - death_num
    player3_gap = abs(player3_gap)

    #Gap between player 4 and death number
    player4_gap = player4 - death_num
    player4_gap = abs(player4_gap)

    #Gap between player 5 and death number
    player5_gap = player5 - death_num
    player5_gap = abs(player5_gap)

    min_player_gap = min(player1_gap, player2_gap, player3_gap, player4_gap, player5_gap)
    #min_player_gap = round(min_player_gap,2)
    #print("Minimun gap is: "+str(min_player_gap))
    #print("Minimum gap is: {:.2f}".format(min_player_gap))

    #marks_list = [0,0,0,0,0]
    #             1 2 3 4 5

    #Check who belong to min_player_gap
    if player1_gap == min_player_gap:
        #Marking system
        for i in range(len(marks_list)):
            if i == 0:
                continue
            else:
                marks_list[i] -= 1
        print("Score:-")
        print(" "+str(marks_list[0])+"               "+str(marks_list[1])+"             "+str(marks_list[2])+"            "+str(marks_list[3])+"             "+str(marks_list[4]))
        print()
        print("                         Death number is: " + str(round(death_num, 2)))
        print("                     Congratulations Player 1 won")
        print("---------------------------------------------------------------------------")
    elif player2_gap == min_player_gap:
        for i in range(len(marks_list)):
            if i == 1:
                continue
            else:
                marks_list[i] -= 1
        print("Score:-")
        print(" "+str(marks_list[0])+"               "+str(marks_list[1])+"             "+str(marks_list[2])+"            "+str(marks_list[3])+"             "+str(marks_list[4]))
        print()
        print("                         Death number is: " + str(round(death_num, 2)))
        print("                     Congratulations Player 2 won")
        print("---------------------------------------------------------------------------")
    elif player3_gap == min_player_gap:
        for i in range(len(marks_list)):
            if i == 2:
                continue
            else:
                marks_list[i] -= 1
        print("Score:-")
        print(" "+str(marks_list[0])+"               "+str(marks_list[1])+"             "+str(marks_list[2])+"            "+str(marks_list[3])+"             "+str(marks_list[4]))
        print()
        print("                         Death number is: " + str(round(death_num, 2)))
        print("                     Congratulations Player 3 won")
        print("---------------------------------------------------------------------------")
    elif player4_gap == min_player_gap:
        for i in range(len(marks_list)):
            if i == 3:
                continue
            else:
                marks_list[i] -= 1
        print("Score:-")
        print(" "+str(marks_list[0])+"               "+str(marks_list[1])+"             "+str(marks_list[2])+"            "+str(marks_list[3])+"             "+str(marks_list[4]))
        print()
        print("                         Death number is: " + str(round(death_num, 2)))
        print("                     Congratulations Player 4 won")
        print("---------------------------------------------------------------------------")
    elif player5_gap == min_player_gap:
        for i in range(len(marks_list)):
            if i == 4:
                continue
            else:
                marks_list[i] -= 1
        print("Score:-")
        print(" "+str(marks_list[0])+"               "+str(marks_list[1])+"             "+str(marks_list[2])+"            "+str(marks_list[3])+"             "+str(marks_list[4]))
        print()
        print("                         Death number is: " + str(round(death_num, 2)))
        print("                     Congratulations Player 5 won")
        print("---------------------------------------------------------------------------")
    else:
        print("No one win")
    Round = Round + 1

    marks = None

    if marks_list[0] == -10:
        print("Player 1 Eliminated")
        player2, player3, player4, player5 = "player2", "player3", "player4", "player5"
        a, b, c, d = player2, player3, player4, player5
        break
    elif marks_list[1] == -10:
        print("Player 2 Eliminated")
        player1, player3, player4, player5 = "player1", "player3", "player4", "player5"
        a, b, c, d = player1, player3, player4, player5
        break
    elif marks_list[2] == -10:
        print("Player 3 Eliminated")
        player1, player2, player4, player5 = "player1", "player2", "player4", "player5"
        a, b, c, d = player1, player2, player4, player5
        break
    elif marks_list[3] == -10:
        print("Player 4 Eliminated")
        player1, player2, player3, player5 = "player1", "player2", "player3", "player5"
        a, b, c, d = player1, player2, player3, player5
        break
    elif marks_list[4] == -10:
        print("Player 5 Eliminated")
        player1, player2, player3, player4 = "player1", "player2", "player3", "player4"
        a, b, c, d = player1, player2, player3, player4
        break
print("___________________________________________________________________________________________")
#continue game with other 4 members
second_time(a, b, c, d)

#continue game with other 3 members

