# Import Modules
import os
import csv

#set path for file 
csvpath = os.path.join('/Users/patricbeaven/Desktop/Bootcamp/03-Python/Starter_Code/PyPoll/Resources/election_data.csv')

#Lists to store data
ballot_id = []
county = []
candidate= []

#Open the file for reading, specify delimiter and variable holding contents, read hear row 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #add data into lists
    for x in csvreader:
        ballot_id.append(x[0])
        county.append(x[1])
        candidate.append(x[2])

    #The total number of votes cast
    total_votes = len(ballot_id)
    
    #A complete list of candidates who received votes. Find unique values in candidate list and append to separate list
    candidate_list = []
    for x in candidate:
        if x not in candidate_list:
            candidate_list.append(x)
    
    #The total number of votes each candidate won. make a new dictionary, loop through candidates add unique candidate to dictionary and add additional counts in dictionary
    #Convert dictionary to list 
    candidate_votes_d = {}
    for x in candidate:
        if x in candidate_votes_d:
            candidate_votes_d[x] +=1
        else:
            candidate_votes_d[x] =1   
    
    candidate_votes_l = list(candidate_votes_d.values())
    
    #The percentage of votes each candidate won, go through candidate votes list and append to new list . values / total values *100
    candidate_per = []
    for x in range(len(candidate_votes_l)):
        per_vot = round((candidate_votes_l[x]/total_votes*100), 3)
        candidate_per.append(per_vot)
   
    #The winner of the election based on popular vote
    winner_num = max(candidate_per)
    index_winner = candidate_per.index(max(candidate_per))
    winner_name = candidate_list[index_winner]

    #zip key results lists together 
    elect_results = list(zip(candidate_list, candidate_per, candidate_votes_l))

    #Format Analysis 
print(f'------------------------------------')
print(f'Election Results')
print(f'------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'------------------------------------')
for x in elect_results: 
    print(f'{x[0]}: {x[1]}% ({x[2]}) ')
print(f'------------------------------------')
print(f'Winner: {winner_name}')
print(f'------------------------------------')

# Set variable for output file
file = os.path.join("/Users/patricbeaven/Desktop/Bootcamp/03-Python/Starter_Code/PyPoll/Resources/Output.txt")

#  Open the output file
with open(file, "w") as output_file:
    
    # Write summary
    output_file.write(f'------------------------------------\n')
    output_file.write(f'Election Results\n')
    output_file.write(f'------------------------------------\n')
    output_file.write(f'Total Votes: {total_votes}\n')
    output_file.write(f'------------------------------------\n')
    for x in elect_results: 
        output_file.write(f'{x[0]}: {x[1]}% ({x[2]}) \n')
    output_file.write(f'------------------------------------\n')
    output_file.write(f'Winner: {winner_name}\n')
    output_file.write(f'------------------------------------\n')
