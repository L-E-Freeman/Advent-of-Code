from statistics import mode, multimode

class DecodeBinaryDiagnostics():
    """A class used to decode binary input and translate it to useful decimal 
    diagnostic information. 
    """
    def __init__(self):
        """Initialize input attribute."""
        filename = '2021_day_3_input.txt'

        with open(filename, 'r') as file_object:
            self.my_input = [line.strip() for line in file_object]

    def calculate_power_consumption(self):
        """ 
        Finds bits of the gamma and epsilon rates by determining most and least 
        common bits of all bits at each position of input numbers, and returns
        the product of these rates as power consumption.
        """
        # Split input binary in to a list of the individual digits of the 
        # binary and add these to digit_lists.
        digit_lists = []
        for binary in self.my_input:
            digit_lists.append([binary[idx] for idx in range(len(binary))])

        # Adds lists of digits at their corresponding positions to 
        # position_digits.
        position = 0
        mode_digits = []
        while position <= len(binary)-1:
            mode_digits.append(
                mode([digit_lists[idx][position] for idx in range(
                    len(self.my_input))]))
            position +=1

        # int() function takes base of number to be converted as optional 
        # argument, which is 2 for binary.
        gamma_rate = int(''.join(mode_digits), 2)

        uncom_digits = []
        for i in mode_digits:
            if i == '0':
                uncom_digits.append('1')
            elif i == '1':
                uncom_digits.append('0')
        
        epsilon_rate = int(''.join(uncom_digits), 2)

        return gamma_rate*epsilon_rate
        
    def calculate_life_support_rating(self):
        """
        Find o2 generator rating and co2 scrubber rating by determining the 
        most or least common bits at each position and retaining the number
        which corresponds to these criteria, multiplied together for the life 
        support rating.
        """
        digit_lists = []
        for binary in self.my_input:
            digit_lists.append([binary[idx] for idx in range(len(binary))])

        position = 0
        length_of_input = len(self.my_input)
        length_of_uncom_input = len(self.my_input)
        uncom_digit_lists = digit_lists

        while position <= len(binary):
            # mode of all digits at the current position from each number in 
            # list.
            max_mode = max(multimode(
                digit_lists[inc][position] for inc in range(
                    length_of_input)))
            min_mode = max(multimode(
                uncom_digit_lists[inc][position] for inc in range(
                    length_of_uncom_input)))

            for num in digit_lists:
                if num[position] == max_mode:
                    digit_lists = [
                        num for num in digit_lists if num[position] == max_mode]
            for num in uncom_digit_lists:
                if num[position] != min_mode:
                    uncom_digit_lists = [
                        num for num in uncom_digit_lists if num[position] != min_mode]
            
            length_of_input = len(digit_lists)
            length_of_uncom_input = len(uncom_digit_lists)
            
            if len(digit_lists) == 1 and len(uncom_digit_lists) == 1:
                break

            position +=1
            
        o2_generator_rating = int(''.join(digit_lists[0]), 2)
        co2_scubber_rating = int(''.join(uncom_digit_lists[0]), 2)
        
        return o2_generator_rating*co2_scubber_rating
    
            

        
        
