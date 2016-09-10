# def test():
#     return 'hello'

# this is the game plan
# we are going to make
# a function that will read the data in
# built into this, we are going to make functions that
# 1. creates a list of the differences <- we will use from collections
# Counter in order to get the amounts
# 2. We are going to create a function MAX that gets the max differences
# and saves the date
# 3. Clearly, we need a function that will read the data
# 4. and a function that will hold all of the other functions and
# print everything properly

# def exchange_rate_csv_reader(filename):
#     '''
#     INPUT: csv file of exchange rate data
#     OUTPUT: list of changes between exchange rates day to day
#     this file skips bank holidays
#     '''
#     with open(filename) as f:
#         result = []
#         line_info = []
#         todaysrate = 0
#         for i, line in enumerate(f):
#             if 'Bank holiday' not in line:
#                 line_info = line.replace(',', ' ').split()
#                 if i == 4:
#                     todaysrate = round(float(line_info[2]), 2)
#                 elif i > 4 and len(line_info)==4:
#                     result.append(round(todaysrate - round(float(line_info[2]), 2), 2))
#                     todaysrate = round(float(line_info[2]), 2)
#     return result

def exchange_rate_csv_reader(filename):
    '''
    INPUT: csv file of exchange rate data
    OUTPUT: list of changes between exchange rates day to day
    this file skips bank holidays
    '''
    with open(filename) as f:
        differences = []
        dates = []
        line_info = []
        result = []
        todaysrate = 0
        for i, line in enumerate(f):
            if 'Bank holiday' not in line:
                line_info = line.replace(',', ' ').split()
                if i == 4:
                    todaysrate = round(float(line_info[2]), 2)
                elif i > 4 and len(line_info)==4:
                    differences.append(round(todaysrate - round(float(line_info[2]), 2), 2))
                    dates.append(line_info[0])
                    todaysrate = round(float(line_info[2]), 2)
    result.append(differences)
    result.append(dates)
    return result

def summarize_csv_info(list):
    '''
    INPUT: list of exchange rate differences
    OUTPUT: summarized count information as a string
    '''
    from collections import Counter
    info_dict = dict(Counter(list[0]))
    sortedkeys = sorted(info_dict.keys())
    result = ''
    print_line = '{}: {}\n'
    for key in sortedkeys:
        result += print_line.format(key, info_dict[key])
    return result

def get_max_change(list):
    '''
    INPUT: list of lists where list[0]=inter-day changes and list[1]=date
    OUTPUT: string indicating max change and date of max change
    '''
    max_change = max(list[0])
    indices = [i for i, x in enumerate(list[0]) if x == max_change]

    for index in indices:
