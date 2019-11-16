# The signatures of this class and its public methods are required for the automated
# grading to work. You must not change the names or the list of parameters. You may
# introduce private/protected utility methods though.

# Gibt 2.8 Punkte

class MagicDrawingBoard:
    def __init__(self, x, y):
        if x <= 0 or y <= 0:
            raise Warning("Board dimensions are corrupted")
        self.__x_coordinate = x
        self.__y_coordinate = y
        self.__board = [[0 for i in range(self.__x_coordinate)] for j in range(self.__y_coordinate)]

    def reset(self):
        self.__board = [[0 for i in range(self.__x_coordinate)] for j in range(self.__y_coordinate)]

    def pixel(self, xy):
        x_coord = xy[0]
        y_coord = xy[1]
        if x_coord < 0 or y_coord < 0:
            raise Warning("invalid coordinates")

        self.__board[y_coord][x_coord] = 1

    def rect(self, start_xy, end_xy):
        start_tuple = (start_xy[0], start_xy[1])
        end_tuple = (end_xy[0], end_xy[1])

        if end_tuple[0] <= start_tuple[0] or end_tuple[1] <= start_tuple[1]:
            raise Warning("end coordinates are smaller than start coordinates")

        if start_tuple[0] < 0 or start_tuple[1] < 0:
            raise Warning("invalid start tuple")

        if start_tuple[0] > self.__x_coordinate or start_tuple[1] > self.__y_coordinate:
            raise Warning("start tuple out of bounds")

        if end_tuple[0] > self.__x_coordinate or end_tuple[1] > self.__y_coordinate:
            raise Warning("end tuple out of bounds")

        x_idx = [i for i in range(start_tuple[0], end_tuple[0])]
        y_idx = [i for i in range(start_tuple[1], end_tuple[1])]

        for idx_y, val_y in enumerate(self.__board):
            if idx_y in y_idx:
                for idx_x, val_x in enumerate(val_y):
                    if idx_x in x_idx:
                        self.__board[idx_y][idx_x] = 1


    def img(self):
        new_board = []
        for value in self.__board:
            new_board.append("".join(str(e) for e in value))
        res_board = "\n".join(str(e) for e in new_board)
        return res_board



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(6, 4)
    db.pixel((1, 1))
    db.rect((6,6), (1,1))
    print("After drawing:")
    print(db.img())
    db.reset()
    print("After resetting:")
    print(db.img())
