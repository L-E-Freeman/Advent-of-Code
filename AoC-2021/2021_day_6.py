class LanternfishGrowth():
    """Calculates growth of lanternship population by modelling the fish as 
    a number representing days until reproduction."""

    def __init__(self):
        """Initializing input variable."""

        with open("2021_day_6_input.txt") as f:
            lst = f.read()
        
        lst = lst.split(",")
        self.my_input = [int(i) for i in lst]

    def calculate_number_lanternfish(self, days_after_initial=80):
        """Returns length of list containing all lanternship, which is the 
        lanternship population after given number of days."""

        counter = 0
        # Run for given number of cycles. Range stops 1 short, so include 
        # last value.
        for i in range(days_after_initial+1):
            # Add necessary number of 8's.
            added_fish = [8] * counter
            self.my_input.extend(added_fish)
            if i == days_after_initial:
                return len(self.my_input)
            counter = 0
            # Increment fish down and find how many 8's (new fish) need to
            # be added.
            for x in range(len(self.my_input)):
                self.my_input[x] -= 1

                if self.my_input[x] == -1:
                    self.my_input[x] = 6
                    counter +=1
                
        
a = LanternfishGrowth()
print(a.calculate_number_lanternfish())