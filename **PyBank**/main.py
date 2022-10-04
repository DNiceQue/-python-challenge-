# Importing dependecies
import os
import csv

# Specify the file to open and create to
budget_data = os.path.join("PyBank/Resources/budget_data.csv")

# Specify the file to export text file to
text_path = os.path.join("PyBank, analysis, budget_analysis.txt")

# Tracking various financial parameters
total_months = 0
total_revenue = 0
month_of_change = []
previous_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999]

# Read the csv file and convert into list of dictionaries
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the header row
    csv_header = next(csvreader)

    # Loop through the data to find total months
    for row in csvreader:

        # Count the total of months
        total_months += 1

        # Calculate the total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"])- previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]

        # The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row['Date']

        # The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row['Date']

    # Calculate the  average revenue change 
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

    # Write changes to csv 
    with open(text_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("---------------------\n")
        file.write("Total Months: %d\n" % total_months)
        file.write("Total Revenue: $%d\n" % total_revenue)
        file.write("Average Revenue Change $%d\n" % revenue_average)
        file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
        file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
 
 


