import os
import csv

#variables
votes = 0
names = []
candidates = []
candidate_votes = 0


#file path
csvpath = os.path.join("..","..","..","..", 'LearnPython','NUCHI201908DATA2', 'Homework', '03-Python', 'Instructions','PyPoll','Resources','election_data.csv')


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
     
    
    for row in csvreader:
        votes += 1
        names = row[2]
        candidates.append(names)
        if names == candidates[0]:
            candidate_votes += 1
        elif names == candidates[1]:
            candidate_votes += 1
        elif names == candidates[2]:
            candidate_votes += 1
        elif names == candidates[3]:
            candidate_votes += 1

candidates = set(candidates)
percentage_votes = round((candidate_votes / votes),2)
candidate_details = {
    'Correy': [percentage_votes, candidate_votes],
    "O'Tooley": [percentage_votes, candidate_votes],
    'Khan': [percentage_votes, candidate_votes],
    'Li': [percentage_votes, candidate_votes]
}
 
print(f"""Election Results
--------------------------------------
Total Votes: {votes}
--------------------------------------
{candidate_details}""")    

import pathlib
pathlib.Path("pypollresults.txt").write_text(f"""Election Results
--------------------------------------
Total Votes: {votes}
--------------------------------------
{candidates}""") 
