# coding: utf-8
# Import pathlib and csv libraries for reading and writing to csv files
import csv
from pathlib import Path


# Use this loan list for calculations
loan_costs = [500, 600, 200, 1000, 450]


# Print the number of loans from the loan list
total_loans = len(loan_costs)
print(f"The total number of loans is {total_loans}")


# Calculate and print the sum of the loans from the loan list
total_value = sum(loan_costs)
print(f"The total value of all loans is ${total_value}")


#Calculate and print the average loan size
average_loan_amount = total_value / total_loans
print (f"The average loan amount is ${average_loan_amount}")


# Use this list to calculate the loans present value
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# Get and print the future value and remaining months of repayment on the loan
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print (f"The future value of the loan is ${future_value}")
print (f"There are {remaining_months} months remaining")
discount_rate = 0.20


# Print the loans fair value (present value) assuming a 20% discount rate
present_value = (future_value)/(1+ (discount_rate/12)) ** remaining_months
print (f"Fair value is ${present_value:.2f}")


# Use conditional logic to evaluate borrowing given the present value of the loan.
# Print 'The loan is worth at least the cost to buy it' if the present value is greater than the loan price. 
# Print 'The loan is too expensive and not worth the price' if the present value is less than the loan price.
loan_price = loan.get("loan_price")

if present_value >= loan_price:
    print("The loan is worth at least the cost to buy it")
else:
    print("The loan is too expensive and not worth the price")


# Given the following loan data, calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}


# Create and use a function to calculate present value including parameters for: future value, remaining months and annual discount rate
# Use a 20% discount rate
# Return the present value

def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = (future_value) / (1 + annual_discount_rate/12) ** remaining_months
    print("pv",present_value)
    return present_value

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

annual_discount_rate = 0.20
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)


# Print the present value of the loan
print(f"The present value of the loan is: ${present_value: .2f}")


# Using the below list, create a new list of inexpensive loans
# Iterate through the loans to find the ones equal or less than 500. Use a conditional statement to identify the inexpensive loans
# Append the inexpensive loans to a new list named inexpensive loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an inexpensive loans list
inexpensive_loans = []

# Append the loans less than or equal to 500 to the new inexpensive loan list
for loan_size in loans:
    if loan_size["loan_price"] <= 500:
       inexpensive_loans.append(loan_size)
       

# Print the list of inexpensive loans
for loan_size in loans:
    if loan_size["loan_price"] <= 500:
       print(loan_size)
       

# Output the list of inexpensive loans to a new csv file to be named 'inexpensive loans list'
# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path using either the absolute or relative path
csvpath = Path("/Users/patrickbeeson/Desktop/fintech_workspace/inexpensive_loans.csv")
# csvpath = Path("inexpensive_loans.csv")

# write the header row and each row of loan values from the `inexpensive loans` list.
with open(csvpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")

    csvwriter.writerow(header)

    for item in inexpensive_loans:
        csvwriter.writerow(item.values())
