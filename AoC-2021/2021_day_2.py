class PositionAndDepthIncreases():
    """Class consisting of submarine command interpreting functions"""

    def __init__(self):
        """Initialize input attribute."""
        filename = '2021_day_2_input.txt'

        with open(filename, 'r') as file_object:
            self.my_input = [line.strip() for line in file_object]

    def calculate_position_and_depth(self):
        """
        Retrieves input values consisting of a direction command and 
        a unit amount and moves the submarine based on these. 
        """
        horizontal_pos = 0
        depth = 0
        for command in self.my_input:
            command = command.split()
            unit_increase = int(command[1])

            if command[0] == 'forward':
                horizontal_pos += unit_increase
            elif command[0] ==  'down':
                depth += unit_increase
            elif command[0] == 'up':
                depth -= unit_increase

        return horizontal_pos*depth

    def calculate_position_and_depth_with_aim(self):
        """
        Retrieves input values consisting of a direction command and 
        a unit amount and moves the submarine based on these, including an aim 
        value which increases or decreases based on 'down' and 'up' commands. 
        """
        aim = 0
        horizontal_pos = 0
        depth = 0
        for command in self.my_input:
            command = command.split()
            unit_increase = int(command[1])

            if command[0] == 'forward':
                horizontal_pos += unit_increase
                depth += aim*unit_increase
            if command[0] == 'down':
                aim += unit_increase
            if command[0] =='up':
                aim -= unit_increase

        return horizontal_pos*depth

