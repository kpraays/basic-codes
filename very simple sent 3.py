def get_input():
    n = int(input("enter the total number of items"))
    items = []
    for i in range(n):
        item = int(input("enter the item"))
        items.append(item)
    print(f"data to be sent {items}")
    return items

def get_individual_sum_from_input(items):
    checksum = 0
    # while calculating checksum, to consider negative inputs - we take absolute value for checksum
    for item in items:
        checksum += abs(item)
    print(f"checksum is {checksum}")

    individual_sum = 0
    for digit in str(checksum):
        individual_sum += int(digit)
    print(f"individual sum is {individual_sum}")
    return checksum, individual_sum

def get_encrypted_data(individual_sum, items):
    encrypted_data = []
    for item in items:
        encrypted_data.append(item+individual_sum)
    print(f"encrypted data is {encrypted_data}")
    return encrypted_data

items = get_input()
checksum, individual_sum = get_individual_sum_from_input(items)
encrypted_data = get_encrypted_data(individual_sum, items)

# to get the output
# we append the checksum to the encrypted data list
encrypted_data.append(checksum)
print(f"the final output is: {encrypted_data}")
