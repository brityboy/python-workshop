from datetime import datetime
from collections import OrderedDict, defaultdict
import sys
import os
import re


class MonthData(object):
    '''
    A class to store the weather stats for a month.
    '''
    def __init__(self, month, max_temps, min_temps, avg_temps, precips):
        '''
        INPUT:
            - month: name of the month (e.g. 01/14)
            - max_temps: list of the maximum temperatures per day
            - min_temps: list of the minimum temperatures per day
            - avg_temps: list of the average temperatures per day
            - precips: list of the precipation amounts per day

        Fill in the data for the month.

        Create these instance variables:
            - month: name of the month
            - avg_temp: average of all the average temperatures
            - min_temp: minimum of all the minimum temperatures
            - max_temp: maximum of all the maximum temperatures
            - total_precip: total of all the precipitation
            - days_precip: number of days where there was precipitation
        '''
        self.month = month
        self.avg_temp = round(1.0*sum(avg_temps)/len(avg_temps), 2)
        self.min_temp = min(min_temps)
        self.max_temp = max(max_temps)
        self.total_precip = sum(precips)
        self.days_precip = len([item for item in precips if item > 0])


class MonthlyWeather(object):
    '''
    A class to store the month by month weather stats for a city.
    '''
    def __init__(self, name, filename):
        '''
        INPUT:
            name: str (the city name)
            filename: str (name of tsv file of the data)

        Fill in the data for a city from a tsv file.
        '''
        self.name = name
        self.data = self._read_data(filename)


    def _read_data(self, filename):
        '''
        INPUT:
            filename: str
        OUTPUT: dict (str => MonthData)

        Read in the data from the filename and store it in an OrderedDict.
        The keys are the month names (e.g. 01/14) and the values are the
        associated MonthData objects.
        '''
        data_dict = defaultdict(dict)
        keys = ['01/14', '02/14', '03/14', '04/14', '05/14', '06/14', '07/14', '08/14', '09/14', '10/14', '11/14', '12/14']
        subkeys = ['max_temps', 'min_temps', 'avg_temps', 'precips']
        for key in keys:
            for subkey in subkeys:
                data_dict[key][subkey] = []
        with open(filename) as f:
            for line in f:
                line = line.split('\t')
                data_dict[line[0][5:7]+'/'+line[0][2:4]]['max_temps'].append(int(line[1]))
                data_dict[line[0][5:7]+'/'+line[0][2:4]]['min_temps'].append(int(line[2]))
                data_dict[line[0][5:7]+'/'+line[0][2:4]]['avg_temps'].append(float(line[3]))
                if line[7] != 'T':
                    data_dict[line[0][5:7]+'/'+line[0][2:4]]['precips'].append(float(line[7]))
                else:
                    data_dict[line[0][5:7]+'/'+line[0][2:4]]['precips'].append(float(0.00))
        total_info = OrderedDict(sorted(data_dict.items(), key=lambda t: t[0]))
        result = {}
        for key in keys:
            result[key] = MonthData(key, total_info[key]['max_temps'], total_info[key]['min_temps'], total_info[key]['avg_temps'], total_info[key]['precips'])
        return OrderedDict(sorted(result.items(), key=lambda t: t[0]))


    def __str__(self):
        '''
        INPUT: None
        OUTPUT: str

        Return a string demonstrating these values for each month:
            - average temperature
            - number of days with precipitation
            - total amount of precipitation
        '''
        keys = self.data.keys()
        result = ''
        for key in keys:
            print_avg_temp = self.data[key].avg_temp
            print_days_precip = self.data[key].days_precip
            print_total_precip = self.data[key].total_precip
            # printstring = key+'\t{0:.2f}\t{0:.0f}\t{0:.2f}\n'
            printstring = '{}\t{}\t{}\t{}\n'
            result += printstring.format(key, round(print_avg_temp, 2), print_days_precip, round(print_total_precip, 2))
        return '\t\tprecipitation\nmonth\ttemp\tdays\ttotal\n'+result


class WeatherByCity(object):
    '''
    A class for representing weather data for a city
    '''
    def __init__(self, directory):
        '''
        INPUT: directory: str (location of tsv data files)

        Fill in the data for all the city tsv files in the directory.

        Create these instance variables:
            - data: dict (str => MonthlyWeather)
            - months: set (strs)

        The data dictionary should have the city names as keys and their
        associated MonthlyWeather objects as values.

        The months are all the months that are in any of the datasets.

        Raise an IOError if the directory given doesn't exist.
        '''

        self.data = self._read_directory(directory)
        self.months = self._month_checker()

    def _month_checker(self):
        final_list = []
        for city in self.data.keys():
            for month in self.data[city].data.keys():
                final_list.append(month)
        return set(final_list)


    def _read_directory(self, directory):
        files_and_names = []
        for filename in os.listdir(directory):
            files_and_names.append([filename[0:-4], directory+'/'+filename])

        result = {}
        for file_and_name in files_and_names:
            result[file_and_name[0]] = MonthlyWeather(file_and_name[0], file_and_name[1])
        return result


    def warmest_city_per_month(self):
        return self._aggregator('avg_temp', 'max')
    def coldest_city_per_month(self):
        return self._aggregator('avg_temp', 'min')
    def rainiest_city_per_month(self):
        return self._aggregator('total_precip', 'max')
    def days_rain_city_per_month(self):
        return self._aggregator('days_precip', 'max')


    def _aggregator(self, attr, statistic):
        '''
        INPUT: object - this is a dictionary where key = city name and value = MonthlyValues(city)
                attr - this is the MonthData attribute that we wish to search through
                statistic - this is either max or min, since we might look for max or min objects
        OUTPUT: dictionary where key = month and value is a tuple (city, value)
        '''
        months = sorted(list(self.months))
        list_of_cities = self.data.keys()
        whole_list = []
        for month in months:
            value_list = []
            city_list = []
            for city in list_of_cities:
                value_list.append(getattr(self.data[city].data[month], attr))
                city_list.append(city)
            whole_list.append([month, value_list, city_list])
        # result = ''
        # for line in whole_list:
        #     month = line[0]
        #     if statistic == 'max':
        #         value  = max(line[1])
        #     elif statistic == 'min':
        #         value = min(line[1])
        #     citynumber = line[1].index(value)
        #     city = line[2][citynumber]
        #     printstring = '{}\t{}\t{}\n'
        #     result += printstring.format(month, city, value)
        # return result
        result = {}
        for line in whole_list:
            month = line[0]
            if statistic == 'max':
                value  = max(line[1])
            elif statistic == 'min':
                value = min(line[1])
            citynumber = line[1].index(value)
            city = line[2][citynumber]
            result[month] = (city, value)
        return result

if __name__ == '__main__':
#     # sf = MonthlyWeather('sf', 'data/weather/sf.tsv')
#     # print sf.data
#     #print sf
    w = WeatherByCity('data/weather')
#     print cities.data['sf']
#     print cities.data['denver']
#     print cities.data['seattle']
#     print cities.months
    print w.warmest_city_per_month()
    print w.coldest_city_per_month()
    print w.rainiest_city_per_month()
    print w.days_rain_city_per_month()
