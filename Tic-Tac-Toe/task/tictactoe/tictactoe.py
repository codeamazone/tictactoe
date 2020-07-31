m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
field = None
coordinates = [0, 0]
m_index = [0, 0]
player = 'X'
winner = None


def create_field():
    global m
    global field
    field = f'''---------
| {m[0][0]} {m[0][1]} {m[0][2]} |
| {m[1][0]} {m[1][1]} {m[1][2]} |
| {m[2][0]} {m[2][1]} {m[2][2]} |
---------'''
    print(field)


def check_input():
    global coordinates
    range_ = {1, 2, 3}
    move = input('Enter the coordinates:').split()
    string_check = [x for x in move if not x.isdigit()]
    digit_check = [x for x in move if x.isdigit()]
    if len(string_check) > 0 or len(digit_check) < 2 or len(digit_check) > 3:
        print('You should enter numbers!')
        check_input()
    elif len(digit_check) == 2:
        x = digit_check[0]
        y = digit_check[1]
        if int(x) not in range_ or int(y) not in range_:
            print('Coordinates should be from 1 to 3!')
            check_input()
        else:
            coordinates[0] = int(x)
            coordinates[1] = int(y)
            return coordinates


def convert_coordinates():
    global m
    global coordinates
    global m_index
    m_indices = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    field_indices = [[1, 3], [2, 3], [3, 3], [1, 2], [2, 2], [3, 2], [1, 1], [2, 1], [3, 1]]
    field_index = field_indices.index(coordinates)
    m_index = m_indices[field_index]
    return m_index


def check_win():
    global winner
    row_1 = m[0]
    row_2 = m[1]
    row_3 = m[2]
    column_1 = [x[0] for x in m]
    column_2 = [x[1] for x in m]
    column_3 = [x[2] for x in m]
    diagonal_left = [m[0][0], m[1][1], m[2][2]]
    diagonal_right = [m[0][2], m[1][1], m[2][0]]
    row_1_win = row_1[1:] == row_1[:-1] and ' ' not in row_1  # three in row_1
    row_2_win = row_2[1:] == row_2[:-1] and ' ' not in row_2  # three in row_2
    row_3_win = row_3[1:] == row_3[:-1] and ' ' not in row_3  # three in row_3
    column_1_win = column_1[1:] == column_1[:-1] and ' ' not in column_1  # three in column_1
    column_2_win = column_2[1:] == column_2[:-1] and ' ' not in column_2  # three in column_2
    column_3_win = column_3[1:] == column_3[:-1] and ' ' not in column_3  # three in column_3
    diagonal_left_win = diagonal_left[1:] == diagonal_left[:-1] and ' ' not in diagonal_left  # three in diagonal_left
    diagonal_right_win = diagonal_right[1:] == diagonal_right[:-1] and ' ' not in diagonal_right  # three in diagonal_right
    if row_1_win:
        print(f'{row_1[0]} wins')
        winner = 'yes'
    elif row_2_win:
        print(f'{row_2[0]} wins')
        winner = 'yes'
    elif row_3_win:
        print(f'{row_3[0]} wins')
        winner = 'yes'
    elif column_1_win:
        print(f'{column_1[0]} wins')
        winner = 'yes'
    elif column_2_win:
        print(f'{column_2[0]} wins')
        winner = 'yes'
    elif column_3_win:
        print(f'{column_3[0]} wins')
        winner = 'yes'
    elif diagonal_left_win:
        print(f'{diagonal_left[0]} wins')
        winner = 'yes'
    elif diagonal_right_win:
        print(f'{diagonal_right[0]} wins')
        winner = 'yes'
    else:
        winner = 'no'


create_field()
while True:
    check_input()
    convert_coordinates()
    if m[m_index[0]][m_index[1]] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        if player == 'X':
            m[m_index[0]][m_index[1]] = 'X'
            player = 'O'
        else:
            m[m_index[0]][m_index[1]] = 'O'
            player = 'X'
        create_field()
        check_win()
        if winner == 'yes':
            break
        elif ' ' not in [i for j in m for i in j]:
            print('Draw')
            break
