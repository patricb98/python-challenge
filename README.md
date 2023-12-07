# python-challenge
challenge 3 

Pybank
-  Your task is to create a Python script that analyses the records to calculate each of the following values:
-  The total number of months included in the dataset
-  The net total amount of "Profit/Losses" over the entire period
-  The changes in "Profit/Losses" over the entire period, and then the average of those changes
-  The greatest increase in profits (date and amount) over the entire period
-  The greatest decrease in profits (date and amount) over the entire period

Start by importing os and csv modules into script. Then link csv file and output.txt path to script. Open the csv and head headers.
Append column data into lists. calculate total length of date list to find total months included in the dataset. 
Sum p/l list to find net profit/loss over period
Find av change in profit between periods by looping through length of p_l list -1. Diff between periods = previous period - current period, add values to new list. Find av change by sum of new list / length of new list 
find greatest inc in profit of change pl list using max function. find the index of max change. Corrilate max change index with date list to find month and value 
find greatest dec in profit ^ same as above but use min function 
Print results in terminal 
Print results in output txt file 

PyPoll 
- Your task is to create a Python script that analyzes the votes and calculates each of the following values:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on popular vote

Start by importing os and csv modules into script. Then link csv file and output.txt path to script. Open the csv and head headers.
Append column data into lists.
find total number of votes by finding length of new list
find list of candidates by looping through candidate list and appending unique values into a new list
find total # of votes for each candidate by using a count occurrences of element in list loop and adding values to a dictionary, then convert dictionary of values into a new list. 
find percentage of votes by looping through counted vote lists and dividing by total votes to find percentage and append to new candidate percent list 
find winner by using max function on percentage list. find index of max percentage. corrilate max percentage index with candidate list to find name   
Zip candidate list, candidate percentage list and candidate votes list together so we can print results out
Print results in terminal 
Print results in output txt file 
