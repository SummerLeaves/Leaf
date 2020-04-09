import csv
import re

pattern = re.compile('^(WVJCE-)[\d\d\d]')

class DCB:
    DCB_id = 0
    num_assembled = 0
    num_not_assembled = 0
    num_unknown = 0
    num_total = 0

    def __init__(self):
        self.bad_DCB = {}
        self.good_DCB = {}
        self.unknown_DCB = {}

    def print_out(self):
        print("The total number of boards (assembled, not assembled, unknown): " + str(DCB.num_total))
        print("The number of assembled boards: " + str(DCB.num_assembled))
        print("The number of boards not assembled: " + str(DCB.num_not_assembled))
        print("The number of boards with unknown condition: " + str(DCB.num_unknown))
    
    def increment_total(self):
        DCB.num_total += 1

    def increment_num_assembled(self):
        DCB.num_assembled += 1

    def increment_not_assembled(self):
        DCB.num_not_assembled += 1
    
    def increment_num_unknown(self):
        DCB.num_unknown += 1

    def assembled_dict_update(self, line):
        self.good_DCB[line[1]] = line[2:12]
    
    def not_assembled_dict_update(self, line):
        self.bad_DCB[line[1]] = line[2:12]

    def unknown_dict_update(self, line):
        self.unknown_DCB[line[1]] = line[2:12]

def process_line(line):
    if (line[3] == "Yes" or line[3] == 'yes'):
        return 1
    elif(not line[3]):
        return 2
    else:
        return 3

with open('PEPI_LVR.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    new_DCB = DCB()

    for line in csv_reader:
        if re.match(pattern, line[0]):
            assembled = process_line(line)
            if (assembled == 1):
                new_DCB.assembled_dict_update(line)
                new_DCB.increment_num_assembled()
            elif (assembled == 2):
                new_DCB.not_assembled_dict_update(line)
                new_DCB.increment_not_assembled()
            else:
                new_DCB.unknown_dict_update(line)
                new_DCB.increment_num_unknown()
            
            new_DCB.increment_total()

    new_DCB.print_out()
