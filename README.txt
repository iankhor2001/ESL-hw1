Instruction
    Remove the data whose value of the TEMP (temperature) column is '-99.000' or '-999.000'.
    Find out the maximum of the TEMP value from C0A880, C0F9A0, C0G640, C0R190, C0X260.
    Output the ID of the station and the maximum of it in the lexicographical order.
    If you cannot find the maximum, please output 'None'.

Sample answer
    [['C0A880', 27.0], ['C0F9A0', 22.0], ['C0G640', 28.0], ['C0R190', 'None'], ['C0X260', 27.0]]

My results
    [['C0A880', 23.1], ['C0F9A0', 25.2], ['C0G640', 25.4], ['C0R190', 27.1], ['C0X260', 25.5]]

How to set up and run my program:
    To read any .csv file, just change the file name over at line 11. (Now it's set to 108000165.csv.)
    Then just let it run.

To TA, if your question here intended to mean "explain how my code function", here's the answer:
    
    1)  I first used filter() and lambda functions to filter out the inputs with TEMP equal to -999.000 or -99.000.  (Line 31)
    2)  Then I used filter() and lambda functions again to select the data of these stations: ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']  (Line 32)
    3)  I then used a for loop to loop through the list of 5 stations.  (Line 36)
    4)  In the for loop, I first select the individual station for the data list using filter().  (Line 37)
    5)  If the list of data for the station is empty ( [] ), it will just append ['STATION_ID', 'None'] to the final result list.  (Line 38-39)
    6)  If not, I used a temporary list to keep just the id and TEMP data of that station and change them into a tuple.  (Line 41)
    7)  Then I used max() to pick the tuple with the max TEMP value.  (Line 43)
    8)  It is then converted into a list and appended into the final result list.
    9)  Since I already selected the station in the lexicographical order, there is no reason to sort the final result again. 
        However if you really wants to sort them again, just uncomment line 49. The line will sort it for you. It uses a sort() method on the list we have.
    10) Finally, the code print out the result using print(). (Line 57)