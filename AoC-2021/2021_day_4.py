import numpy as np

class BingoSolver():
    """Calculates winning and losing scores for a set of bingo boards given 
    the numbers being drawn."""
    
    def __init__(self):
        """Initialize input variables."""
        with open("2021_day_4_input.txt") as file_object:
            input = file_object.readlines()

        # Get drawn numbers and neatly formatted list of boards.
        boards = []
        for i, line in enumerate(input):
            if i == 0:
                numbers = line
            elif line.strip() == '':
                pass
            else:
                boards.append(line.strip().replace('  ', ' '))

        # Convert strings of ints in to lists of ints.
        int_list = []
        for line in boards:
            line_list = line.split()
            map_obj = map(int, line_list)
        
            for l in list(map_obj):
                int_list.append(l)

        # Create suitable 3D array.
        a1D = np.array(int_list)

        # -1 allows numpy to infer shape based on number of lines.
        self.my_input = np.reshape(a1D, (-1,5,5))
        self.drawn_numbers = [int(num) for num in numbers.strip().split(',')]

    def find_board_scores(self):
        """Adds winning boards to a list, picks first score added as the
        winning board and last score as losing board."""
        
        # If a row or column is == -1, add score to list and place -2 in
        # the array to make sure it isn't looped over again.
        winning_scores = []
        for num in self.drawn_numbers:
            self.my_input[self.my_input == num] = -1
            for arry in self.my_input:
                if -2 not in arry:
                    for row in arry:
                        if np.all(row==-1):
                            winning_scores.append(
                                num*(arry[arry != -1].sum()))
                            arry[0,0] = -2
                    arry = np.transpose(arry)
                    for row in arry:
                        if np.all(row== -1):
                            winning_scores.append(
                                num*(arry[arry != -1].sum()))
                            arry[0,0] = -2

        return winning_scores[0], winning_scores[-1]

