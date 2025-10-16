"""
File: battleship.py
Author: Elif Meral
Date: 04/17/2024
Section: 24
E-mail: elifm1@umbc.edu
Description:
        Two users input where they want to place their ships and plays battleships until one looses.
"""
# makes an empty board


def setup_board(rows, columns):
    the_grid = []
    top_row = []
# top row numbers
    for j in range(columns):
        if j == 0:
            top_row.append(' ')
        else:
            top_row.append(j - 1)
    the_grid.append(top_row)
# left side numbers
    for i in range(1, rows):
        new_row = []
        for j in range(columns):
            if j == 0 and i >= 1:
                new_row.append(i - 1)
            else:
                new_row.append(' ')
        the_grid.append(new_row)
# putting the lines
    for i in range(rows):
        for j in range(columns):
            if j != columns - 1:
                print(the_grid[i][j], end=' | ')
            else:
                print(the_grid[i][j])
    return the_grid


# makes players' boards


def player_boards(board):
    player1_board = [row[:] for row in board]
    player2_board = [row[:] for row in board]
    player1_plays = [row[:] for row in board]
    player2_plays = [row[:] for row in board]

    return player1_board, player2_board, player1_plays, player2_plays

# place each individual ship


def place_ship(board, ship, x, y, direction, length):
    ships = {'Carrier': 'Ca', 'Battleship': 'Ba', 'Cruiser': 'Cr', 'Submarine': 'Su', 'Destroyer': 'De'}
    if direction == 'r':
        for num in range(length):
            board[x][y + num] = ships[ship]
    elif direction == 'd':
        for num in range(length):
            board[x + num][y] = ships[ship]

# makes sure the player places each ship on the board properly.


def place_ships(player_board):
    ship_locations = []
    ship_lengths = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    ships_placed = 0
    while ships_placed < len(ships):
        for ship in ships:
            check_position = False
            while not check_position:
                position = input(f'Enter y x coordinates to place the {ship}: ')
                x_pos, y_pos = position.split()
                x_pos = int(x_pos) + 1
                y_pos = int(y_pos) + 1
                direction = input('Enter Right or Down (r or d): ')
                if direction == 'r':
                    if 1 <= x_pos < 11 and 1 <= y_pos < 11 - ship_lengths[ship]:
                        overlapping = False
                        for length in range(ship_lengths[ship]):
                            if player_board[x_pos][y_pos + length] != ' ':
                                overlapping = True
                        if overlapping:
                            print('Overlapping ships. Try Again.')
                        else:
                            place_ship(player_board, ship, x_pos, y_pos, direction, ship_lengths[ship])
                            ship_locations.append(position)
                            ships_placed += 1
                            check_position = True
                            for i in range(len(player_board)):
                                for j in range(len(player_board[i])):
                                    if j != len(player_board[i]) - 1:
                                        if (player_board[i][j] == 'Ca' or player_board[i][j] == 'Ba'
                                                or player_board[i][j] == 'Cr' or player_board[i][j] == 'Su'
                                                or player_board[i][j] == 'De'):
                                            print(player_board[i][j], end='| ')
                                        else:
                                            print(player_board[i][j], end=' | ')
                                    else:
                                        print(player_board[i][j])
                    else:
                        print('That was out of range. Try Again.')
                elif direction == 'd':
                    if 1 <= x_pos < 11 - ship_lengths[ship] and 1 <= y_pos < 11:
                        overlapping = False
                        for length in range(ship_lengths[ship]):
                            if player_board[x_pos + length][y_pos] != ' ':
                                overlapping = True
                        if overlapping:
                            print('Overlapping ships. Try Again.')
                        else:
                            place_ship(player_board, ship, x_pos, y_pos, direction, ship_lengths[ship])
                            ship_locations.append(position)
                            ships_placed += 1
                            check_position = True
                            for i in range(len(player_board)):
                                for j in range(len(player_board[i])):
                                    if j != len(player_board[i]) - 1:
                                        if (player_board[i][j] == 'Ca' or player_board[i][j] == 'Ba'
                                                or player_board[i][j] == 'Cr' or player_board[i][j] == 'Su'
                                                or player_board[i][j] == 'De'):
                                            print(player_board[i][j], end='| ')
                                        else:
                                            print(player_board[i][j], end=' | ')
                                    else:
                                        print(player_board[i][j])
                    else:
                        print('That was out of range. Try Again.')
                else:
                    print('Invalid input. Try Again.')
    return player_board

# displays the board for the corresponding player


def boards_displayed(player_board, player_plays):
    # prints the players board
    for i in range(len(player_board)):
        for j in range(len(player_board[i])):
            if j != len(player_board[i]) - 1:
                if (player_board[i][j] == 'Ca' or player_board[i][j] == 'Ba'
                        or player_board[i][j] == 'Cr' or player_board[i][j] == 'Su'
                        or player_board[i][j] == 'De' or player_board[i][j] == 'HH' or player_board[i][j] == 'XX'):
                    print(player_board[i][j], end='| ')
                else:
                    print(player_board[i][j], end=' | ')
            else:
                print(player_board[i][j])

    # prints the players plays
    for i in range(len(player_plays)):
        for j in range(len(player_plays[i])):
            if j != len(player_plays[i]) - 1:
                if (player_plays[i][j] == 'Ca' or player_plays[i][j] == 'Ba'
                        or player_plays[i][j] == 'Cr' or player_plays[i][j] == 'Su'
                        or player_plays[i][j] == 'De' or player_plays[i][j] == 'HH' or player_plays[i][j] == 'XX'):
                    print(player_plays[i][j], end='| ')
                else:
                    print(player_plays[i][j], end=' | ')
            else:
                print(player_plays[i][j])
# checks hitting position


def check_hit(board, plays, x, y, ship_lengths):
    ship_names = {'Ca': 'Carrier', 'Ba': 'Battleship', 'Cr': 'Cruiser', 'Su': 'Submarine', 'De': 'Destroyer'}
    if board[x][y] != ' ':
        ship_attacked = ship_names[board[x][y]]
        board[x][y] = 'HH'
        length_left = ship_lengths[ship_attacked]
        length_left -= 1
        ship_lengths[ship_attacked] = length_left
        plays[x][y] = 'HH'
        return True, ship_lengths
    else:
        board[x][y] = 'XX'
        plays[x][y] = 'XX'
        return False, ship_lengths

# checks if the player has won


def check_winner(ship_lengths):
    ship_names = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
    for ship in ship_names:
        if ship_lengths[ship] == 0:
            return True
    return False

# runs the whole game


def run_game():
    # the players place their ships
    the_board = setup_board(11, 11)
    player1_board, player2_board, player1_plays, player2_plays = player_boards(the_board)
    print('Player 1, place your ships')
    place_ships(player1_board)
    setup_board(11, 11)
    print('Player 2, place your ships')
    place_ships(player2_board)
    # the game starts and players take turns until one player sinks all the ships.
    ship_lengths = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    player = 1
    win_status = False
    while not win_status:
        check_position = False
        while not check_position:
            if player == 1:
                print('Player 1, it is your turn.')
                boards_displayed(player1_board, player1_plays)
                x, y = input('Enter y x coordinates to fire: ').split()
                x = int(x) + 1
                y = int(y) + 1
                check_position = False
                while not check_position:
                    if 1 <= x < 11 and 1 <= y < 11:
                        check_position = True
                        hit, ship_lengths = check_hit(player2_board, player1_plays, x, y, ship_lengths)
                        if hit:
                            print('Player 1 hit!')
                            if check_winner(ship_lengths):
                                win_status = True
                                print('Player 1 has won!')
                        else:
                            print('Player 1 missed!')
                        player = 2
                    else:
                        print('Invalid coordinates')
                        x, y = input('Enter y x coordinates to fire: ').split()
                        x = int(x) + 1
                        y = int(y) + 1
            else:
                print('Player 2, it is your turn.')
                boards_displayed(player2_board, player2_plays)
                x, y = input('Enter y x coordinates to fire: ').split()
                x = int(x) + 1
                y = int(y) + 1
                check_position = False
                while not check_position:
                    if 1 <= x < 11 and 1 <= y < 11:
                        check_position = True
                        hit, ship_lengths = check_hit(player1_board, player2_plays, x, y, ship_lengths)
                        if hit:
                            print('Player 2 hit!')
                            if check_winner(ship_lengths):
                                win_status = True
                                print('Player 2 has won!')
                        else:
                            print('Player 2 missed!')
                        player = 1
                    else:
                        print('Invalid coordinates')
                        x, y = input('Enter y x coordinates to fire: ').split()
                        x = int(x) + 1
                        y = int(y) + 1


if __name__ == '__main__':
    run_game()
