# Import Modules
import os
import csv


current_directory = os.path.dirname(__file__)
csv_path = os.path.join(current_directory, 'Resources', 'budget_data.csv')
file = os.path.join(current_directory, "Analysis", "Output.txt")
#set path for file 
#csvpath = os.path.join("Resources/budget_data.csv")

#Lists to store data
date = []
p_l = []

#Open the file for reading, specify delimiter and variable holding contents, read hear row 
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #add data into lists
    for x in csvreader:
        date.append(x[0])
        p_l.append(int(x[1]))

    #Total number of months in dataset 
    total_months = len(date)
    
    #Net profit/loss over period
    profit_loss = sum(p_l)
    
    #Average change in profit between periods. calc av change in p_l then add to new list. calc av of new list
    change_p_l = []
    for x in range(len(p_l)-1):
            change_p_l.append(p_l[x+1]-p_l[x])
    average_change = round(sum(change_p_l)/len(change_p_l),2) 
    
    #Greatest increase in profits. find max in change list then find correlating index in date list     
    inc_profits = max(change_p_l)
    index_inc = change_p_l.index(max(change_p_l))
    inc_month = date[index_inc+1]

    #Greatest decrease in profits find min in change list then find crrelating index in date list      
    dec_profits = min(change_p_l)
    index_dec = change_p_l.index(min(change_p_l))
    dec_month = date[index_dec+1]

#Format anaylsis
print('Financial Analysis')
print('---------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total P/L: ${profit_loss}') 
print(f'Average Monthly Change: ${average_change}')
print(f'Greatest Increase in Profits: {inc_month}  (${inc_profits})')  
print(f'Greatest Decrease in Profits: {dec_month}  (${dec_profits})')

# Set variable for output file



#  Open the output file
with open(file, "w") as output_file:
    
    # Write summary
    output_file.write('Financial Analysis\n')
    output_file.write('---------------------------------------------\n')
    output_file.write(f'Total Months: {total_months}\n')
    output_file.write(f'Total P/L: ${profit_loss}\n')
    output_file.write(f'Average Monthly Change: ${average_change}\n')
    output_file.write(f'Greatest Increase in Profits: {inc_month}  ${inc_profits}\n')
    output_file.write(f'Greatest Decrease in Profits: {dec_month}  ${dec_profits}\n')
    