import numpy as np


class LineOverlaps():

    def __init__(self):
        """Initialize input variable."""

        with open("2021_day_5_input.txt") as file_object:
            raw = file_object.readlines()

        # Split input in to list, remove arrow. 
        lines = []
        for line in raw:
            line = line.strip().split()

            for value in line:
                if value != "->":
                    lines.append(value)

        # Convert coordinates to integers, place in to tuples.
        coords = []
        for item in lines:
            item = item.split(",")
            coords.append((int(item[0]), int(item[1])))

        # Split coordinates in to groups of 2. (start coords, end coords) 
        # for each line.
        self.coords = [coords[i:i + 2] for i in range(0, len(coords), 2)]

    def sort_coordinates(self):
        """Sorts coordinates of lines in to horizontal, vertical, and diagonal, 
        and finds maximum value of x and y coordinates."""
        # Find max x and y coordinates to find size of array needed.
        x_coords = []
        y_coords = []
        self.hoz_lines = []
        self.vert_lines = []
        self.diag_lines = []
        for lst in self.coords:
            # If x1 = x2 or y1 = y2, line is horizontal/vertical and needs 
            # to be drawn. Else is diagonal.
            if lst[0][0] == lst[1][0]:
                self.vert_lines.append(lst)
            elif lst[0][1] == lst[1][1]:
                self.hoz_lines.append(lst)
            else:
                self.diag_lines.append(lst)
            for tup in lst:
                x_coords.append(tup[0])
                y_coords.append(tup[1])

        self.max_x = max(x_coords)
        self.max_y = max(y_coords)

    def parse_intermediate_coordinates(self):
        """Uses sorted coordinates to find all integer points along lines 
        drawn between given coordinates, and returns list of these points
        for either just horizontal and vertical lines or all lines."""
        
        self.sort_coordinates()

        # Find range of coordinates in between line points and add them to 
        # list.
        hoz_vert_coords = []
        for line in self.hoz_lines:
            if line[0][0] < line [1][0]:
                # +1 as must be inclusive of second coordinate.
                for i in range(line[0][0], line[1][0]+1):
                    hoz_vert_coords.append((i, line[0][1]))
            else:
                for i in range(line[1][0], line[0][0]+1):
                    hoz_vert_coords.append((i, line[0][1]))

        for line in self.vert_lines:
            if line[0][1] < line[1][1]:
                for i in range(line[0][1], line[1][1]+1):
                    hoz_vert_coords.append((line[0][0], i))
            else:
                for i in range(line[1][1], line[0][1]+1):
                    hoz_vert_coords.append((line[0][0], i))

        diag_coords = []
        for line in self.diag_lines:
            # y = mx + c
            m = (line[0][1] - line[1][1]) / (line[0][0] - line[1][0])
            # Finding c
            y = line[0][1]
            x = line[0][0]
            c = y - (x*m)

            # Find range of x values.
            x_values = []
            if line[0][0] < line[1][0]:
                for i in range(line[0][0], line[1][0]+1):
                    x_values.append(i)
            else:
                for i in range(line[1][0], line[0][0]+1):
                    x_values.append(i)

            # Solve y for every value of x
            for i in x_values:
                y_value = (m*i) + c
                diag_coords.append((i, int(y_value)))

        all_coords = hoz_vert_coords + diag_coords

        return hoz_vert_coords, all_coords
        
    def draw_lines(self, only_horizontal=False):
        """Takes parameter of whether all coordinates or just the hoz and
        vert subset should be used. Adds 1 to every coordinate point in 
        array and returns the number of 2's in the array, indicating 
        overlapping lines"""
        
        if only_horizontal:
            coords = self.parse_intermediate_coordinates()[0]
        else:
            coords = self.parse_intermediate_coordinates()[1]

        line_arry = np.zeros((self.max_x+1, self.max_y+1), np.int8)
        
        for coord in coords:
            line_arry[coord] +=1

        n = line_arry >= 2
        
        return len(line_arry[n])