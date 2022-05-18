from ast import And
from itertools import count
from typing import final


print("Please follow the instructions \nto figure out how much you need \nto save to become a millionaire!\n")
input("PLEASE PRESS ENTER TO CONTINUE...\n")

income = input("Please enter your annual NET income: \n")
monthly_expenses = input("Please enter your total monthly expenses: \n")
monthly_play_money = input("Enter any additional expenses for leisure activities: \n")
current_savings = input("Please enter the dollar figure \nof your current savings: \n")

monthly_excess = int(income) / 12 - int(monthly_expenses) - int(monthly_play_money)
total_current_savings = int(current_savings) + monthly_excess
counter = 1

final_savings = total_current_savings
print(final_savings)
while counter < 10000:
    counter = counter + 1
    final_savings = final_savings + monthly_excess
    if final_savings >= 1000000:
        years = counter / 12
        print("It will take " + str(counter) + " months, or " + str(years) + " years to become a millionaire")
        break
print(final_savings)

