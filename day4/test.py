# from collections import OrderedDict, defaultdict
# def read_data(filename):
#     data_dict = defaultdict(dict)
#     keys = ['01/14', '02/14', '03/14', '04/14', '05/14', '06/14', '07/14', '08/14', '09/14', '10/14', '11/14', '12/14']
#     subkeys = ['max_temps', 'min_temps', 'avg_temps', 'precips']
#     for key in keys:
#         for subkey in subkeys:
#             data_dict[key][subkey] = []
#     with open(filename) as f:
#         for line in f:
#             line = line.replace('\t', ' ').split()
#             data_dict[line[0][5:7]+'/'+line[0][2:4]]['max_temps'].append(line[1])
#             data_dict[line[0][5:7]+'/'+line[0][2:4]]['min_temps'].append(line[2])
#             data_dict[line[0][5:7]+'/'+line[0][2:4]]['avg_temps'].append(line[3])
#             data_dict[line[0][5:7]+'/'+line[0][2:4]]['precips'].append(line[6])
#     data_dict = OrderedDict(sorted(data_dict.items(), key=lambda t: t[0]))
#     return data_dict
#
# filename = 'data/weather/sf.tsv'
# result = read_data(filename)

from weather import MonthData, MonthlyWeather
sf = MonthlyWeather('sf', 'data/weather/sf.tsv')
sf.__str__()
