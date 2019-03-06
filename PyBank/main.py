#Dependencies
import os
import csv

#Read csv to dataframe
csvpath = os.path.join('budget_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    #Determine average of changes over the entire period, as well as greatest increase, greatest decrease, and date

    months = 0
    net_total = 0
    profit_losses = []
    date = []
    for row in csvreader:
        print(row[1])
        months += 1
        net_total += int(row[1])
        profit_losses.append(int(row[1]))
        date.append(row[0])
    average = 0
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""
    for i in range(len(profit_losses)-1):
        change = profit_losses[i+1]-profit_losses[i]
        average += change
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = date[i+1]
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = date[i+1]
    average /= (months -1)

#print results
output = f'''Financial Analysis
  ----------------------------
    Total Months: {months}
    Total: ${net_total}
    Average Change: ${average}
    Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
    Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
'''
print(output)

#export results to txt file
file = open('pybank_results.txt', 'w') 
file.write(output)
file.close()



