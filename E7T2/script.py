# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.


def is_valid(state):
    player_count = 0

    if not state:
        return False, "no characters"

    for i in range(len(state)):
        for j in range(len(state)):
            if len(state[i]) != len(state[j]):
                return False, "The game world lengths are corrupted"


    valid_chars = [" ", "#", "o"]
    state_str = "".join(state)

    for c in state_str:
        if c not in valid_chars:
            return False, "%s is not a valid character" % c

        if c == "o":
            player_count += 1

    if player_count == 0:
        return False, "no player"

    if player_count > 1:
        return False, "multiple players detected"

    return True, "state correct"


def what_moves_are_possible(validstate):

    if len(validstate) == 1:
        if len(validstate[0]) == 1:
            return [], None, None

    possible_moves = ["down", "left", "right", "up"]
    player_index = 0

    row_count = 0

    for row in validstate:
        row_count += 1
        if "o" in row:
            player_index = row.index("o")
            break

    if row_count == 1:
        possible_moves.remove("up")

    else:
        if validstate[row_count - 2][player_index] == "#":
            possible_moves.remove("up")

    if row_count == len(validstate):
        possible_moves.remove("down")

    else:
        if validstate[row_count][player_index] == "#":
            possible_moves.remove("down")

    if player_index == 0:
        possible_moves.remove("left")

    else:
        if player_index != 0:
            if validstate[row_count - 1][player_index - 1] == "#":
                possible_moves.remove("left")

        else:
            possible_moves.remove("left")

    if player_index == len(validstate[0]):
        possible_moves.remove("right")

    else:
        if player_index != len(validstate[0])-1:
            if validstate[row_count - 1][player_index + 1] == "#":
                possible_moves.remove("right")
        else:
            possible_moves.remove("right")

    return (tuple(possible_moves), player_index, row_count-1)




def get_new_state(validstate, validdirection, player_idx, player_row):

    new_state = list(validstate)

    if validdirection == "right":
        new_state_row = list(validstate[player_row])
        new_state_row[player_idx] = " "
        new_state_row[player_idx+1] = "o"
        new_state_row = "".join(new_state_row)
        new_state[player_row] = new_state_row

    if validdirection == "left":
        new_state_row = list(validstate[player_row])
        new_state_row[player_idx] = " "
        new_state_row[player_idx-1] = "o"
        new_state_row = "".join(new_state_row)
        new_state[player_row] = new_state_row

    if validdirection == "up":
        old_state_row = list(validstate[player_row])
        old_state_row[player_idx] = " "
        old_state_row = "".join(old_state_row)
        new_state_row = list(validstate[player_row-1])
        new_state_row[player_idx] = "o"
        new_state_row = "".join(new_state_row)
        new_state[player_row] = old_state_row
        new_state[player_row-1] = new_state_row

    if validdirection == "down":
        old_state_row = list(validstate[player_row])
        old_state_row[player_idx] = " "
        old_state_row = "".join(old_state_row)
        new_state_row = list(validstate[player_row+1])
        new_state_row[player_idx] = "o"
        new_state_row = "".join(new_state_row)
        new_state[player_row] = old_state_row
        new_state[player_row+1] = new_state_row

    return tuple(new_state)


def move(state, direction):
    if not is_valid(state)[0]:
        raise Warning(is_valid(state)[1])

    if direction in what_moves_are_possible(state)[0]:
        new_state = get_new_state(state, direction, what_moves_are_possible(state)[1], what_moves_are_possible(state)[2])

        new_possible_moves = what_moves_are_possible(new_state)[0]

        return (new_state, new_possible_moves)

    if direction not in what_moves_are_possible(state):
        raise Warning("%s is not a valid move" % direction)


if __name__ == "__main__":
    s1 = (
            "o#      ",
            "###    #",
            "#     ##",
            "   #####"
        )
    s2 = move(s1, "left")

    print("= New State =")
    print("\n".join(s2[0]))
    print("\nPossible Moves: {}".format(s2[1]))
