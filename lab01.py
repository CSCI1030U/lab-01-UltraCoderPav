def main():
    cost_per_item = 19.99
    quantity = 5 

    # YOUR CODE FOR PART 1 GOES HERE  
# Part 1
# The variables cost_per_item and quantity contain numeric values.
# Use these two variables to calculate the total cost (before tax) of the items, 
# which calculates the cost of purchasing quantity of an item which will cost cost_per_item each,
# putting the value in a new variable called subtotal_cost. 
# Next, calculate the tax on this subtotal_cost and put this value into another variable, 
# called tax, which will be 13% of the cost (HST). 
# Finally, assign the sum of these two variables to a new variable, called total_cost

    subtotal_cost = cost_per_item * quantity # total price before tax
    tax = subtotal_cost * 0.13 # will take total price and get tax value on it
    total_cost = subtotal_cost + tax # total price with tax included


    # YOUR CODE FOR PART 2 GOES HERE

# Print the values of all 5 variables, each on their own line, 
# in the form: <variable_name> = <variable_value>. 
# The exact output of your program will look like this:

# cost_per_item = $19.99
# quantity = 5
# subtotal_cost = $99.95
# tax = $12.99
# total_cost = $112.94
# To print a number using exactly two decimal places, 
# use f'variable = {variable:0.2f}' within your print() function call. 
# One example of this has been included in the lab01.py file already,
# and is also included, below:

# print(f'cost_per_item = ${cost_per_item:0.2f}')
# Note: The output has to match exactly, 
# so be sure to put exactly one space on each side of the = sign, 
# and there will be a newline after each variable output (as is the default for print()).
    print(f'cost_per_item = ${cost_per_item:0.2f}') # a sample for you to use for the other prices
    print(f'quantity = {quantity}') 
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')


    # THIS IS THE CODE FOR PART 3

    #     Part 3
# In the final section within lab01.py, 
# there is a simple program that contains an error. 
# So that it doesn't interfere with your previous code, it has been commented out. 
# Uncomment this code (e.g. by selecting it and hitting CTRL-/ on Windows/Linux, or Command-/ on MacOS). 
# Identify the type of error, and the line number where the error has occurred. 
# Search for this error message on the web, and learn about what causes it (e.g. from a Stack Overflow post). 
# Ask ChatGPT or another free AI to explain the error for you.

# Once you have collected enough information about the error, 
# find a way to fix the error so that it produces the expected output, but doesn't use any f-strings.

# Note: It is expected that the result of the calculation has more than 2 decimal places.
# That is fine (and expected) for the purposes of this lab assignment.

    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    print('After 5 years, your investment will be worth ' + str(investment) + ' dollars.')
    #expected output: After 5 years, your investment will be worth 1187.6863056468749 dollars.
    #error python gives me is thar can only concatenate str (not "float") to str 
    # its a Typeerror, to fix it i need to change the Datatype to a string. 
    #you do this by using str()


if __name__ == "__main__":
    main()