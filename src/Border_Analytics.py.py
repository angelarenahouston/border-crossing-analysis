#Data Scientist:  Angela Rena Houston
#Insight Data Scientist Boston Fellows
#Coding Challenge
#Due:  11/13/2019
#Submitted:  11/15/2019

#Instructions:  https://github.com/InsightDataScience/border-crossing-analysis
#We have to calculate the total number of times that
#vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian
#and U.S.-Mexican borders each month. We also want to know the running
#monthly average of total number of crossings for that type of crossing
#and border.

#Implementation Steps
#Install Anocanda 3.7
#Write the Python Program.
#Load the Border_Crossing_Entry_Data.csv Input File.
#Calculate the total number of crossings (Value). 
#Calculate the running monthly average of total crossings,
#rounded to the nearest whole number, for that combination
#of Border and Measure, or means of crossing.
#Write the output data to report.csv.
#Expected output format:  Border,Date,Measure,Value,Average (3,4,5,6,7)
#Sort in descending order:  Date, Value, Measure, Border.

import sys
import csv
import math

is_avg = True
counter = 0
value = 0
sum = 0
avg = 0

with open('report1.csv', 'w') as outputfile:
    writer = csv.writer(outputfile)
    with open('Border_Crossing_Entry_Data.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:  
            if is_avg:
                row.insert(7, 'Average')
                is_avg = False
            else:
                counter = counter + 1
                value = int(float(row[6]))
                sum = sum + round(value,)
                avg = sum / counter
                
                row.insert(7, avg)
            writer.writerow((row[3], row[4], row[5], row[6], row[7]))

with open('report1.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = sorted(reader, key=lambda row: (row['Border'], row['Date'], row['Measure'], row['Value']))

with open('report.csv', 'w', newline='') as output:    
    writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(data)

#References
#https://www.anaconda.com/distribution/
#https://docs.python.org/3/tutorial/index.html
#https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
#https://www.csvexplorer.com/blog/open-big-csv/
#https://docs.python.org/3/library/csv.html
#https://docs.python.org/3/tutorial/introduction.html
#https://docs.python.org/3/library/csv.html?highlight=csv#module-csv
#https://www.guru99.com/python-csv.html
#https://stackoverflow.com/questions/42740869/use-python-to-calculate-data-in-csv
#https://s3.amazonaws.com/MLMastery/machine_learning_mastery_with_python_mini_course.pdf?__s=i518tha6ewpzxpfgbu1p
#https://thepythonguru.com/python-how-to-read-and-write-csv-files/
#https://www.tutorialspoint.com/python/number_round.htm
#https://www.tutorialspoint.com/python/python_files_io.htm
#https://stackoverflow.com/questions/16695740/use-python-to-write-on-specific-columns-in-csv-file
#https://stackoverflow.com/questions/7588934/how-to-delete-columns-in-a-csv-file
#https://stackoverflow.com/questions/47825184/adding-new-column-to-csv-in-python
#https://www.tutorialspoint.com/find-average-of-a-list-in-python
#https://stackoverflow.com/questions/47886931/sort-csv-by-column-name
#https://stackoverflow.com/questions/38118526/python-3-calculate-average-write-to-csv

