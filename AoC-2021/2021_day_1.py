class SonarDepthCalculations():
    """Class consisting of 'sonar scan' depth increase counting functions."""

    def __init__(self):
        """Initialize input attribute."""
        filename = '2021_day_1_input.txt'

        with open(filename, 'r') as file_object:
            self.my_input = [int(line.strip()) for line in file_object]

    def count_depth_increases(self):
        """
        Retrieves input values consisting of ocean depth 'sonar scans' and 
        counts the aggregate number of depth measurement increases from the 
        previous scan value.
        """

        idx = 1
        count = 0
        while idx <= (len(self.my_input))-1:
            if self.my_input[idx] > self.my_input[idx-1]:
                idx +=1
                count +=1
            elif self.my_input[idx] <= self.my_input[idx-1]:
                idx +=1
                
        return count

    def count_sliding_window_increases(self):
        """
        Retrieves input values consisting of ocean depth 'sonar scans' and 
        counts the aggregate number of depth measurement increases in sections 
        of three.
        """
        idx = 0
        count = 0
        while idx <= (len(self.my_input))-1:
            try:
                sum_prev = sum(self.my_input[idx+i] for i in range(3))
                sum_next = sum(self.my_input[idx+i] for i in range(1,4))
                if sum_next > sum_prev:
                    idx +=1
                    count +=1
                elif sum_next <= sum_prev:
                    idx +=1
            except IndexError:
                return count

