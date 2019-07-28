def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def new_game():
    global board
    board = ["_" for i in range(10)]
    display_board(board)
    player1_sign = input("Hello Player1 which Sign do you want to play X or O?")
    player1_sign = player1_sign.upper()
    if player1_sign == 'X':
        player2_sign = 'O'
    else:
        player2_sign = 'X'

    return player1_sign, player2_sign, board


def make_a_turn(player1_sign, player2_sign, curr_turn):
    curr_place = int(input(f"hello {curr_turn} where do you want to place your sign?"))
    if board[curr_place] == "_":
        if curr_turn == "player1":
            board[curr_place] = player1_sign
            curr_turn = "player2"
        else:
            board[curr_place] = player2_sign
            curr_turn = "player1"

        display_board(board)

    else:
        print("this location is already occupied ")
    return curr_turn


def check_for_win(player_sign):
    WON = False
    if all(place == player_sign for place in (board[1], board[2], board[3])):
        WON = True
    if all(place == player_sign for place in (board[1], board[4], board[7])):
        WON = True
    if all(place == player_sign for place in (board[1], board[5], board[8])):
        WON = True
    if all(place == player_sign for place in (board[4], board[5], board[6])):
        WON = True
    if all(place == player_sign for place in (board[8], board[5], board[2])):
        WON = True
    if all(place == player_sign for place in (board[3], board[6], board[9])):
        WON = True
    if all(place == player_sign for place in (board[7], board[8], board[9])):
        WON = True
    if all(place == player_sign for place in (board[7], board[5], board[3])):
        WON = True
    if all(place == player_sign for place in (board[8], board[5], board[2])):
        WON = True

    if WON:
        print(f"congrats you won the game! {player_sign}")
        answer = input("do you wanna play again Y/N?")
        if answer == 'Y':
            new_game()
        else:
            exit(code=None)


def main():
    global board
    curr_turn = "player1"
    playing = True
    player1_sign, player2_sign, board = new_game()
    print(f'Ok so player1 your sign is {player1_sign}  player 2 your sign is {player2_sign}')
    while playing:
        curr_turn = make_a_turn(player1_sign, player2_sign, curr_turn)
        check_for_win(player1_sign)
        check_for_win(player2_sign)


if __name__ == '__main__':
    main()
