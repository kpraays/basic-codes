# bar code size needs to be 12 digits
# check_digit of the bar code is the last digit

# computation of first eleven digits
#     part_1 = (take the sum of digits in odd positions) * 3
#     part_2 = (take the sum of the digits in the even positions)
#
#     dig_sum = part_1 + part_2
#     if last digit of dig_sum is 0
#         then check_digit_calculated = 0
#     else
#         check_digit_calculated = 10 - last digit of dig_sum

# if check_digit == check_digit_calculated then the bar code is validated

# have functions to do this computation
###########################################################

def get_input():
    """
    this function will
        - get the input
        - check for length 12 digit limitation
        - return the check digit based on input

    Return - tuple - (number, check digit, invalid_input)
    """
    #number = input("enter the 12 digit bar code")
    #number = "079400804501452425"
    #number = "079400804501"
    number = "079400804abc"
    #number = "010as"
    invalid_input = False

    if len(number) != 12:
        print("Error in barcode - number of digits is not 12")
        invalid_input = True
        check_digit = ""
    elif not number.isnumeric():
        print("The input string has invalid characters")
        invalid_input = True
        check_digit = ""
    else:
        check_digit = number[11]
    return number, check_digit, invalid_input

def get_output(calculated_check_digit, actual_check_digit):
    """
    This function will give the output
    It will compare the calculated_check_digit with actual check_digit.

    Input -
        calculated_check_digit -- Integer
        actual_check_digit -- Integer
    """
    if calculated_check_digit == actual_check_digit:
        print("Validated")
    else:
        print("Validation was not successful")

def compute_check_digit(eleven_dig_num):
    """
    This function will do the calculation of check digit as explained in comments above

    Input - eleven_dig_num - string

    Return - check_digit_calculated - integer
    """
    part_1 = 0
    part_2 = 0
    for digit in range(len(eleven_dig_num)):
        # 7896 - 7 is at position 1, 8 is at position 2, 9 is at position 3, 6 is at position 4 (based on the question)
        if (digit+1)%2!=0:
            # get sum of odd position
            part_1 += int(eleven_dig_num[digit])
        if (digit+1)%2==0:
            # get sum of even position
            part_2 += int(eleven_dig_num[digit])

    dig_sum = part_1*3 + part_2
    print(f"dig_sum is {dig_sum}")

    if str(dig_sum)[-1] == "0":
        # if last digit is 0
        check_digit_calculated = 0
        print(f"last digit of dig_sum is 0")
    else:
        check_digit_calculated = 10 - int(str(dig_sum)[-1])
        print(f"last digit of dig_sum is {str(dig_sum)[-1]}")
    print(f"check digit calculated is {check_digit_calculated}")

    return check_digit_calculated

number, actual_check_digit, invalid_input = get_input()
if not invalid_input:
    check_digit_calculated = compute_check_digit(str(number)[0:11]) # take 11 digits from the input
    get_output(check_digit_calculated, int(actual_check_digit))