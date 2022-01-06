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

        # Split coordinates in to groups of 2. (start coords, end coords) for each line.
        self.coords = [coords[i:i + 2] for i in range(0, len(coords), 2)]

    def count_hoz_vert_overlaps(self):
        # Find max x and y coordinates to find size of array needed.
        x_coords = []
        y_coords = []
        hoz_lines = []
        vert_lines = []
        for lst in self.coords:
            print(lst)
            # If x1 = x2 or y1 = y2, line is horizontal and needs to be drawn.
            if lst[0][0] == lst[1][0]:
                vert_lines.append(lst)
            if lst[0][1] == lst[1][1]:
                hoz_lines.append(lst)
            for tup in lst:
                x_coords.append(tup[0])
                y_coords.append(tup[1])

        max_x = max(x_coords)
        max_y = max(y_coords)

        # Create array of zeroes with the correct size. 
        line_arry = np.zeros((max_x+1, max_y+1), np.int8)


        # Find range of coordinates in between line points and add them to list.
        all_coords = []
        for line in hoz_lines:
            if line[0][0] < line [1][0]:
                for i in range(line[0][0], line[1][0]+1):
                    all_coords.append((i, line[0][1]))
            else:
                for i in range(line[1][0], line[0][0]+1):
                    all_coords.append((i, line[0][1]))

        for line in vert_lines:
            if line[0][1] < line[1][1]:
                for i in range(line[0][1], line[1][1]+1):
                    all_coords.append((line[0][0], i))
            else:
                for i in range(line[1][1], line[0][1]+1):
                    all_coords.append((line[0][0], i))

        for coord in all_coords:
            line_arry[coord] +=1

        n = line_arry >= 2

        return len(line_arry[n])
        

        

a = LineOverlaps()
a.count_hoz_vert_overlaps()