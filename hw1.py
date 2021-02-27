# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108000165.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

def sort_by_TEMP(station_data):
    return station_data[1]


target_data = list(filter(lambda item: item['TEMP'] != '-99.000' or item['TEMP'] != '-999.000', data))
target_data = list(filter(lambda item: True if item['station_id'] in ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260'] else False, target_data))

result = []

for stations in ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']:
    station_data = list(filter(lambda station: station['station_id'] == stations, target_data))
    temp_list = [(station['station_id'], float( "{:.1f}".format( float(station['TEMP']) ) ) ) for station in station_data]
    # float("{:.1f}".format(float(station['TEMP']))) converts data from string format to float format with 1 decimal space
    max_temp = list(max(temp_list))
    if max_temp[1] == -99.0 or max_temp[1] == -999.0:
        max_temp[1] = 'None'
    result.append(max_temp)
# filtering for the requested stations

# result.sort(key=sort_by_TEMP)
# The above line can be used to sort the result by tempurature from lowest to highest

# Since when doing the for loop, 
# the program already ordered the list of stations by lexicographical order, 
# we don't have to sort them again here, 
# saving disk space and processing time

print(result)

