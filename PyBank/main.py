import os
import csv

csvpath = os.path.join("..","..","..","..", 'LearnPython','NUCHI201908DATA2', 'Homework', '03-Python', 'Instructions','PyBank','Resources', 'budget_data.csv')
PL = 0
PLTotal = 0
months = 0
maxnum = 0
minnum = 0 
minmaxassigned = False

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:  
        months = sum(1 for row in csvreader)
        PL = int(row[1])
        PLTotal += PL
        if minmaxassigned == False:
            minnum = PL
            maxnum = PL
            minmaxassigned == True

        if PL > maxnum:
            maxnum = PL
        if PL < minnum:
            minnum = PL
        

averagechange = round((PLTotal/months),2)
        
print(f"""Financial Analysis
--------------------------------------
Total Months: {months}
Total Profit/Losses: ${PLTotal}
Average Change: ${averagechange}
Greatest Increase in Profits: {maxnum}
Greatest Decrease in Profits: {minnum}""")    

import pathlib
pathlib.Path("pybankresults.txt").write_text(f"""Financial Analysis
--------------------------------------
Total Months: {months}
Total Profit/Losses: ${PL}
Average Change: ${averagechange}
Greatest Increase in Profits: {maxnum}
Greatest Decrease in Profits: {minnum}""") 

    