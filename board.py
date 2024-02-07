from contants import X, O, EMPTY, LENGTH

class Board:
    def __init__(self):
        #self.state = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
        self.state = []
        for i in range(LENGTH):
            row = []
            for j in range(LENGTH):
                row.append(EMPTY)
            self.state.append(row)

        self.turn = X
        self.opp_turn = O
        self.turn_no = 0

    # Validates move, returns 1 on fail and 0 on success
    def validate_move(self, move, auto):
        # Correct input format check
        if len(move) != 3 or move[1] != " " or move[0].isdigit() == False or move[2].isdigit() == False:
            if not auto:
                print("Invalid input format, try again")
            return 1
        
        # Out of bounds check
        x = int(move[0])
        y = int(move[2])
        if x > LENGTH - 1 or x < 0 or y > LENGTH - 1 or y < 0:
            if not auto:
                print("Coordinates out of bounds, try again")
            return 1
        
        # Space occupied check
        if self.state[x][y] != EMPTY:
            if not auto:
                print("Space occupied, try again")
            return 1

        return 0

    # Makes move, returns 1 if move is invalid else it makes move and returns 0
    def make_move(self, move, auto):
        if self.validate_move(move, auto) == 1:
            return 1
        x = int(move[0])
        y = int(move[2])
        self.state[x][y] = self.turn

        opp = self.turn
        self.turn = self.opp_turn
        self.opp_turn = opp

        self.turn_no+=1
        
    # Check if game has reached terminal state, return 1 if it has and 0 if not
    def check_end(self):
        # Check each horizontal/vertical line
        for i in range(LENGTH):
            for j in range(1, LENGTH):
                prev_symbol = self.state[i][j-1]
                cur_symbol = self.state[i][j]
                if cur_symbol == EMPTY or prev_symbol != cur_symbol:
                    break
                if j == LENGTH - 1:
                    return 1
            for j in range(1, LENGTH):
                prev_symbol = self.state[j-1][i]
                cur_symbol = self.state[j][i]
                if cur_symbol == EMPTY or prev_symbol != cur_symbol:
                    break
                if j == LENGTH - 1:
                    return 1
        # Check downwards diagonal
        for i in range(1, LENGTH):
            cur_down = self.state[i][i]
            prev_down = self.state[i-1][i-1]

            if cur_down == EMPTY or cur_down != prev_down:
                break
            if i == LENGTH - 1:
                return 1
        # Check upwards diagonal
        for i in range(1, LENGTH):
            cur_up = self.state[LENGTH-i-1][i]
            prev_up = self.state[LENGTH-i][i-1]
            if cur_up == EMPTY or cur_up != prev_up:
                break
            if i == LENGTH - 1:
                return 1

        # check for a draw
        if self.turn_no == LENGTH * LENGTH:
            return -1
        return 0
    
    # Print game board
    def print_board(self):
        print(" " + LENGTH *"-")
        for i in range(LENGTH):
            print("|", end = "")
            for j in range(LENGTH):
                print(self.state[i][j], end = "")
            print("|")
        print(" " + LENGTH *"-")
