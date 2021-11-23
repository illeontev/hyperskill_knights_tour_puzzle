def create_matrix(row_count, col_count, knight_x, knight_y):
    matrix = []
    for i in range(row_count):
        row = []
        for j in range(col_count):
            if i == knight_y and j == knight_x:
                row.append("X")
            else:
                row.append("")
        matrix.append(row)
    return matrix


def check_borders(matrix, x, y):
    row_count = len(matrix)
    col_count = len(matrix[0])
    if x < 0 or x > col_count - 1:
        return False
    if y < 0 or y > row_count - 1:
        return False
    return True


def set_value(matrix, x, y, value):
    matrix[y][x] = value


def is_possible_move(matrix, x, y):
    return check_borders(matrix, x, y) and matrix[y][x] not in ("X", "*")

def is_possible_move_for_new_step(matrix, new_x, new_y):
    return matrix[new_y][new_x] not in ("X", "", "*")

def count_possible_moves(matrix, x, y):
    return is_possible_move(matrix, x - 2, y - 1)\
           + is_possible_move(matrix, x - 2, y + 1) \
           + is_possible_move(matrix, x - 1, y - 2) \
           + is_possible_move(matrix, x - 1, y + 2) \
           + is_possible_move(matrix, x + 1, y - 2) \
           + is_possible_move(matrix, x + 1, y + 2) \
           + is_possible_move(matrix, x + 2, y - 1) \
           + is_possible_move(matrix, x + 2, y + 1)


def fill_possible_move(matrix, x, y):
    if is_possible_move(matrix, x, y):
        set_value(matrix, x, y, str(count_possible_moves(matrix, x, y)))


def fill_possible_moves(matrix, knight_x, knight_y):
    fill_possible_move(matrix, knight_x - 2, knight_y - 1)
    fill_possible_move(matrix, knight_x - 2, knight_y + 1)
    fill_possible_move(matrix, knight_x - 1, knight_y - 2)
    fill_possible_move(matrix, knight_x - 1, knight_y + 2)
    fill_possible_move(matrix, knight_x + 1, knight_y - 2)
    fill_possible_move(matrix, knight_x + 1, knight_y + 2)
    fill_possible_move(matrix, knight_x + 2, knight_y - 1)
    fill_possible_move(matrix, knight_x + 2, knight_y + 1)


def clear_possible_moves(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    for i in range(row_count):
        for j in range(col_count):
            if matrix[i][j] not in ["X", "*"]:
                matrix[i][j] = ""


def print_border(col_count, size_of_cell):
    border = " "
    for i in range(col_count * (size_of_cell + 1) + 3):
        border += "-"
    print(border)


def print_chessboard(matrix):
    col_count = len(matrix[0])
    row_count = len(matrix)
    size_of_cell = len(str(col_count * row_count))

    print_border(col_count, size_of_cell)

    for i in range(row_count)[::-1]:
        print(f"{i + 1}| ", end="")
        for j in range(col_count):
            if matrix[i][j] != "":
                print(" " * (size_of_cell - 1 - len(str(matrix[i][j])) + 1) + str(matrix[i][j]), end=" ")
            else:
                print("_" * size_of_cell, end=" ")
        print("|")

    print_border(col_count, size_of_cell)

    number_row = "  "
    for i in range(col_count):
        number_row += " " * (size_of_cell) + str(i + 1)
    print(number_row)


def get_knight_coordinates(input_message, row_count, col_count):
    positions = input(input_message).split()

    if len(positions) != 2:
        raise ValueError
    x = int(positions[0])
    y = int(positions[1])
    if x < 1 or x > col_count:
        raise ValueError
    if y < 1 or y > row_count:
        raise ValueError

    return x - 1, y - 1


def get_borders():
    if len(dimensions) != 2:
        raise ValueError
    col_count = int(dimensions[0])
    row_count = int(dimensions[1])

    if col_count <= 0:
        raise ValueError
    if row_count <= 0:
        raise ValueError

    return row_count, col_count


def count_visited_cells(matrix):
    col_count = len(matrix[0])
    row_count = len(matrix)
    count = 0
    for i in range(row_count):
        for j in range(col_count):
            if matrix[i][j] in ["*", "X"]:
                count += 1
    return count

# don't know yet how to check it
def solution_exists():
    return True

def play_game(row_count, col_count, knight_x, knight_y):
    matrix = create_matrix(row_count, col_count, knight_x, knight_y)
    fill_possible_moves(matrix, knight_x, knight_y)
    print_chessboard(matrix)

    while count_possible_moves(matrix, knight_x, knight_y):
        knight_x_new, knight_y_new = get_knight_coordinates("Enter your next move: ", row_count, col_count)
        if is_possible_move_for_new_step(matrix, knight_x_new, knight_y_new):
            set_value(matrix, knight_x, knight_y, "*")
            clear_possible_moves(matrix)

            knight_y, knight_x = knight_y_new, knight_x_new
            set_value(matrix, knight_x, knight_y, "X")
            fill_possible_moves(matrix, knight_x, knight_y)
            print_chessboard(matrix)
        else:
            print("Invalid move!", end=" ")

    visited_cells_num = count_visited_cells(matrix)
    if visited_cells_num == col_count * row_count:
        print("\nWhat a great tour! Congratulations!")
    else:
        print("\nNo more possible moves!")
        print(f"Your knight visited {visited_cells_num} squares!")


def get_solution(row_count, col_count, knight_x, knight_y):
    matrix = create_matrix(row_count, col_count, knight_x, knight_y)
    fill_possible_moves(matrix, knight_x, knight_y)

    answers = create_matrix(row_count, col_count, knight_x, knight_y)
    set_value(answers, knight_x, knight_y, 1)

    find_solution(matrix, answers, knight_x, knight_y, 1)

    return answers

def find_minimum_moves_count_coordinates(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    minimum = row_count * col_count
    x_min = -1
    y_min = -1
    for i in range(row_count):
        for j in range(col_count):
            if matrix[i][j] not in ("", "X", "*"):
                if int(matrix[i][j]) < minimum:
                    minimum = int(matrix[i][j])
                    x_min = j
                    y_min = i
    return x_min, y_min


def find_solution(matrix, answers, knight_x, knight_y, move_num):
    x_min, y_min = find_minimum_moves_count_coordinates(matrix)
    if x_min == -1:
        set_value(answers, knight_x, knight_y, move_num)
        return

    set_value(matrix, knight_x, knight_y, "*")
    set_value(matrix, x_min, y_min, "X")
    clear_possible_moves(matrix)
    fill_possible_moves(matrix, x_min, y_min)
    set_value(answers, knight_x, knight_y, move_num)
    find_solution(matrix, answers, x_min, y_min, move_num + 1)

def is_wrong_solution(solution, row_count, col_count):
    for i in range(row_count):
        for j in range(col_count):
            if solution[i][j] == "":
                return True
    return False


# This program starts here
while True:
    dimensions = input("Enter your board dimensions: ").split()
    try:
        row_count, col_count = get_borders()
        break
    except ValueError:
        print("Invalid dimensions!")

while True:
    try:
        knight_x, knight_y = get_knight_coordinates("Enter the knight's starting position: ", row_count, col_count)
        break
    except ValueError:
        print("Invalid position!")

while True:
    answer = input("Do you want to try the puzzle? (y/n): ")
    solution = get_solution(row_count, col_count, knight_x, knight_y)
    if is_wrong_solution(solution, row_count, col_count):
        print("No solution exists!")
        break
    else:
        if answer == "y":
            play_game(row_count, col_count, knight_x, knight_y)
            break
        elif answer == "n":

            print("\nHere's the solution!")
            print_chessboard(solution)
            break
        else:
            print("Invalid input!")








