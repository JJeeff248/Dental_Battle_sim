# error_module.py
# A module that can be used for error checking

# By Brianna and Chris

def error_check(values, input_query, error_message, num):
    """
    Takes in a list of valid inputs, an input statement, and an error message,
    and only accepts input from the user if it is an expected value
    """
    # Set valid variable and loop until true
    valid = False
    if num == False:
        while valid == False:
            output = input(input_query).lower()
            # Set valid to true if input is in list of accepted inputs
            if output in values:
                valid = True
            # Else send an error message
            else:
                print(error_message)
    else:
        while valid == False:
            while valid == False:
                try:
                    output = int(input(input_query))
                    valid = True
                except:
                    print(error_message)
                
            # Set valid to true if input is in list of accepted inputs
            if output >= values[0] and output <= values[1]:
                valid = True
            # Else send an error message
            else:
                print(error_message)
                valid = False
    # Return the input
    return output
