#Dependencies
import os
import csv

#Read csv to dataframe
election_data = 'election_data.csv'
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    candidate_dict = {}
    num_votes = len(csvreader)
    for row in csvreader:
        candidate = row[2]
        if candidate in candidate_dict:
            candidate_dict[candidate] += 1
        else:
            candidate_dict[candidate] = 1
    candidates = candidate_dict.keys()

    output = f'''
  Election Results
  -------------------------
  Total Votes: {num_votes}
  -------------------------
  '''
    max_votes = 0
    winner = ""
    
    for candidate in candidate_dict:
        percent_vote = str((candidate_dict[candidate]/num_votes) * 100)
        votes = str(candidate_dict[candidate])
        candidate_results = candidate + ": "  + percent_vote + "% (" + votes + ")"
        output = output + candidate_results
        if votes > max_votes:
            winner = candidate
            max_votes = votes

    output = output + f'''
  -------------------------
  Winner: {winner}
  -------------------------
  '''
print(output)

#export results to txt file
file = open('pypoll_results.txt', 'w') 
file.write(output)
file.close()


