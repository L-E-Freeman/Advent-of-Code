class LanternfishGrowth():

    def __init__(self):
        with open("2021_day_6_input.txt") as f:
            lst = f.read()
        
        lst = lst.split(",")
        self.my_input = [int(i) for i in lst]



    def calculate_number_lanternfish(self, days_after_initial=3):

        # Run for given number of cycles.
        counter = 0
        for i in range(0, days_after_initial):
            # Add necessary number of 8's.
            added_fish = [8] * counter
            print(f"day {i}", added_fish, counter)
            self.my_input.extend(added_fish)
            print(f"list {self.my_input}")
            counter = 0
            # Increment fish down and find how many 8's need to be added.
            for x in range(len(self.my_input)):
                self.my_input[x] -= 1

                if self.my_input[x] == -1:
                    self.my_input[x] = 6
                    counter +=1




        return self.my_input
            


a = LanternfishGrowth()
print(a.calculate_number_lanternfish())