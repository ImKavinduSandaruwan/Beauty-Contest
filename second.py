from third import third_time
def second_time(a,b,c,d):
    print("                             Alice In Boaderland -> Beauty Contest")
    print()
    marks_list = [0, 0, 0, 0]
    Round = 1
    while True:
        # Taking players inputs
        try:
            player1 = int(input(str(a)+" Enter a number between 0 - 100: "))
            if player1 < 0 or player1 > 100:
                print("Enter a number between 0 and 100")
                continue
            player2 = int(input(str(b)+" Enter a number between 0 - 100: "))
            if player2 < 0 or player2 > 100:
                print("Enter a number between 0 and 100")
                continue
            player3 = int(input(str(c)+" Enter a number between 0 - 100: "))
            if player3 < 0 or player3 > 100:
                print("Enter a number between 0 and 100")
                continue
            player4 = int(input(str(d)+" Enter a number between 0 - 100: "))
            if player4 < 0 or player4 > 100:
                print("Enter a number between 0 and 100")
                continue
        except ValueError as e:
            print("Please Enter a number between 0 - 100")
            break

        print()
        print("------------------------------Round:- " + str(Round) + "------------------------------------")
        print(str(a)+"         "+str(b)+"        "+str(c)+"        "+str(d))
        print("---------------------------------------------------------------------------")
        print("  " + str(player1) + "              " + str(player2) + "             " + str(player3) + "            " + str(player4))
        Round = int(Round)

        # taking average
        avg = (player1 + player2 + player3 + player4) / 4
        death_num = avg * 0.8

        # Gap between player 1 and death number
        player1_gap = player1 - death_num
        player1_gap = abs(player1_gap)

        # Gap between player 2 and death number
        player2_gap = player2 - death_num
        player2_gap = abs(player2_gap)

        # Gap between player 3 and death number
        player3_gap = player3 - death_num
        player3_gap = abs(player3_gap)

        # Gap between player 4 and death number
        player4_gap = player4 - death_num
        player4_gap = abs(player4_gap)

        min_player_gap = min(player1_gap, player2_gap, player3_gap, player4_gap)

        if player1_gap == min_player_gap: #player1 = a [0,0,0,0]
            # Marking system
            for i in range(len(marks_list)):
                if i == 0:
                    continue
                else:
                    marks_list[i] -= 1
            print("Score:-")
            print(" " + str(marks_list[0]) + "               " + str(marks_list[1]) + "             " + str(marks_list[2]) + "            " + str(marks_list[3]))
            print()
            print("                         Death number is: " + str(round(death_num, 2)))
            print("                     Congratulations "+str(a)+" won")
            print("---------------------------------------------------------------------------")

        elif player2_gap == min_player_gap:
            # Marking system
            for i in range(len(marks_list)):
                if i == 1:
                    continue
                else:
                    marks_list[i] -= 1
            print("Score:-")
            print(" " + str(marks_list[0]) + "               " + str(marks_list[1]) + "             " + str(marks_list[2]) + "            " + str(marks_list[3]))
            print()
            print("                         Death number is: " + str(round(death_num, 2)))
            print("                     Congratulations "+str(b)+" won")
            print("---------------------------------------------------------------------------")

        elif player3_gap == min_player_gap:
            # Marking system
            for i in range(len(marks_list)):
                if i == 2:
                    continue
                else:
                    marks_list[i] -= 1
            print("Score:-")
            print(" " + str(marks_list[0]) + "               " + str(marks_list[1]) + "             " + str(marks_list[2]) + "            " + str(marks_list[3]))
            print()
            print("                         Death number is: " + str(round(death_num, 2)))
            print("                     Congratulations "+str(c)+" won")
            print("---------------------------------------------------------------------------")

        elif player4_gap == min_player_gap:
            # Marking system
            for i in range(len(marks_list)):
                if i == 3:
                    continue
                else:
                    marks_list[i] -= 1
            print("Score:-")
            print(" " + str(marks_list[0]) + "               " + str(marks_list[1]) + "             " + str(marks_list[2]) + "            " + str(marks_list[3]))
            print()
            print("                         Death number is: " + str(round(death_num, 2)))
            print("                     Congratulations "+str(d)+" won")
            print("---------------------------------------------------------------------------")

        else:
            print("No one win")
        Round = Round + 1

        if marks_list[0] == -10:
            print(str(a)+" Eliminated")   #a = player1 in second round
            e, f, g = b, c, d
            break
        elif marks_list[1] == -10:
            print(str(b)+" Eliminated")
            e, f, g = a, c, d
            break
        elif marks_list[2] == -10:
            print(str(c)+" Eliminated")
            e, f, g = a, b, d
            break
        elif marks_list[3] == -10:
            print(str(d)+" Eliminated")
            e, f, g = a, b, c
            break

    third_time(e,f,g)