import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

try:
    with open(budget_data_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        csv_header = next(csvreader)

        csv_data = list(csvreader)

        Total_Months = len(csv_data)
        Net_Total_Profit_Loss = 0
        Prior_Profit_Loss = 0
        Change_in_Profit_Loss = 0
        Greatest_Increase_in_Profits = {"Date": "", "Profit/Losses": 0}
        Greatest_Decrease_in_Profits = {"Date": "", "Profit/Losses": 0}

        for i in range(Total_Months):
            row = csv_data[i]

            Net_Total_Profit_Loss += int(row[1])

            if i > 0:
                change = int(row[1]) - Prior_Profit_Loss
                Change_in_Profit_Loss += change

                if change > Greatest_Increase_in_Profits["Profit/Losses"]:
                    Greatest_Increase_in_Profits["Profit/Losses"] = change
                    Greatest_Increase_in_Profits["Date"] = row[0]
                elif change < Greatest_Decrease_in_Profits["Profit/Losses"]:
                    Greatest_Decrease_in_Profits["Profit/Losses"] = change
                    Greatest_Decrease_in_Profits["Date"] = row[0]
                
            Prior_Profit_Loss = int(row[1])

        Average_Change = Change_in_Profit_Loss / (Total_Months - 1) if Total_Months > 1 else 0

        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {Total_Months}")
        print(f"Total: ${Net_Total_Profit_Loss}")
        print(f"Average Change: ${Average_Change:.2f}")
        print(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits['Date']} (${Greatest_Increase_in_Profits['Profit/Losses']})")
        print(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits['Date']} (${Greatest_Decrease_in_Profits['Profit/Losses']})")

        output_file = os.path.join("PyBank Analysis.txt")

        with open(output_file, "w", newline='') as datafile:

            datafile.write("Financial Analysis\n")
            datafile.write("----------------------------\n")
            datafile.write(f"Total Months: {Total_Months}\n")
            datafile.write(f"Total: ${Net_Total_Profit_Loss}\n")
            datafile.write(f"Average Change: ${Average_Change:.2f}\n")
            datafile.write(f"Greatest Increase in Profits: {Greatest_Increase_in_Profits['Date']} (${Greatest_Increase_in_Profits['Profit/Losses']})\n")
            datafile.write(f"Greatest Decrease in Profits: {Greatest_Decrease_in_Profits['Date']} (${Greatest_Decrease_in_Profits['Profit/Losses']})\n")

        print(f"Results exported to: {output_file}")

except FileNotFoundError:
    print(f"Error: File '{budget_data_csv}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")


