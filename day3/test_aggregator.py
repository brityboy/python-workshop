def aggregator(self, attr, statistic):
    months = sorted(list(object.months))
    list_of_cities = self.data.keys()
    whole_list = []
    for month in months:
        value_list = []
        city_list = []
        for city in list_of_cities:
            value_list.append(getattr(self.data[city].data[month], attr))
            city_list.append(city)
        whole_list.append([month, value_list, city_list])
    result = ''
    for line in whole_list:
        month = line[0]
        if statistic == 'max':
            value  = max(line[1])
        elif statistic == 'min':
            value = min(line[1])
        citynumber = line[1].index(value)
        city = line[2][citynumber]
        printstring = '{}\t{}\t{}\n'
        result += printstring.format(month, city, value)
    return result
