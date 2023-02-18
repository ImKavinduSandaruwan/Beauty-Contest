def forth_time(h,i):
    print("                             Alice In Boaderland -> Beauty Contest")
    print()
    marks_list = [0, 0]
    Round = 1
    while True:
        # Taking players inputs
        try:
            player1 = int(input(str(h) + " Enter a number between 0 - 100: "))  # player1 = h
            if player1 < 0 or player1 > 100:
                print("Enter a number between 0 and 100")
                continue
            player2 = int(input(str(i) + " Enter a number between 0 - 100: "))  # player2 = i
            if player2 < 0 or player2 > 100:
                print("Enter a number between 0 and 100")
                continue
        except ValueError as e:
            print("Please Enter a number between 0 - 100")
            break

        print()
        print("------------------------------Round:- " + str(Round) + "------------------------------------")
        print(str(h)+ "         " +str(i))
        print("---------------------------------------------------------------------------")
        print("  " + str(player1) + "              " + str(player2))
        Round = int(Round)

        # taking average
        avg = (player1 + player2) / 2
        death_num = avg * 0.8

        # Gap between player 1 and death number
        player1_gap = player1 - death_num
        player1_gap = abs(player1_gap)

        # Gap between player 2 and death number
        player2_gap = player2 - death_num
        player2_gap = abs(player2_gap)

        min_player_gap = min(player1_gap, player2_gap)

        if player1_gap == min_player_gap:  # player1 = h [0,0,]
            # Marking system
            for i in range(len(marks_list)):
                if i == 0:
                    continue
                else:
                    marks_list[i] -= 1
            print("Score:-")
            print(" " + str(marks_list[0]) + "               " + str(marks_list[1]))
            print()
            print("                         Death number is: " + str(round(death_num, 2)))
            print("                     Congratulations Player " + str(h) + " won")
            print("---------------------------------------------------------------------------")

        elif player2_gap == min_player_gap:
            # Marking system
            for i in range(len(marks_list)):
                if i == 1:
                    continue
                else:
                    marks_list[i] -= 1
            print("Score:-")
            print(" " + str(marks_list[0]) + "               " + str(marks_list[1]))
            print()
            print("                         Death number is: " + str(round(death_num, 2)))
            print("                     Congratulations " + str(i) + " won")
            print("---------------------------------------------------------------------------")
        else:
            print("No one win")
        Round = Round + 1

        if marks_list[0] == -10:
            print(str(h) + " Eliminated")  # e = player1 in second round
            print(str(i)+" won the game")
            break
        elif marks_list[1] == -10:
            print(str(i) + " Eliminated")
            print(str(h)
                  +" won the game")
            break

