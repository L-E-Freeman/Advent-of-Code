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
            coords.append((int(item[0]), int(item[2])))

        # Split coordinates in to groups of 2. (start coords, end coords) for each line.
        self.coords = [coords[i:i + 2] for i in range(0, len(coords), 2)]

    def count_hoz_vert_overlaps(self):
        # Find max x and y coordinates to find size of array needed.
        x_coords = []
        y_coords = []
        vert_hoz_lines = []
        for lst in self.coords:
            # If x1 = x2 or y1 = y2, line is horizontal and needs to be drawn.
            if lst[0][0] == lst[1][0]:
                vert_hoz_lines.append(lst)
            if lst[0][1] == lst[1][1]:
                vert_hoz_lines.append(lst)
            for tup in lst:
                x_coords.append(tup[0])
                y_coords.append(tup[1])

        max_x = max(x_coords)
        max_y = max(y_coords)

        # Create array of zeroes with the correct size. 
        line_arry = np.zeros((max_x, max_y), np.int8)

        print(vert_hoz_lines)

        

a = LineOverlaps()
a.count_hoz_vert_overlaps()