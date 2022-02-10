# odd_even_swap(S1, S2)
# gives output such that
# i)  in odd positions of output - letters from even positions of S2 will be there
# ii) in even positions of output - letters from odd positions of S2 will be there
#
# constraint 1 - if no even position letters are available in S2 - output will retain the odd position letters from S1
# constraint 2 - if no odd position letter are available in S2 - output will retain the even position letters from S1
#
# note: case to consider
# if S1 and S2 - same length
# if length(S1) > length(S2)
# if length(S1) < length(S2)

# for this question
# consider string abcd
# a - odd pos - 1 -- 0 index
# b - even pos - 2 -- 1 index
# c - odd pos - 3 -- 2 index
# d - even pos - 4 -- 3 index


# Algorithm
#
# take empty output string
# collect letters from even positions of S2 -- even_pos_S2
# collect letters from odd positions of S2  -- odd_pos_S2
# collect letters from even positions of S1 -- even_pos_S1
# collect letters from odd positions of S1  -- odd_pos_S1
#
# for each position of the output string  -- length of output string will be equal to length of S1
#     if it is odd position
#         if even_pos_S2 list is not empty
#             put first item of even_pos_S2 list in output string
#             delete first item of even_pos_S2 list
#         elif even_pos_S2 list is empty
#             put first item of odd_pos_S1 list in output string
#             delete first item of odd_pos_S1 list
#
#     if it is even position
#         if odd_pos_S2 list is not empty
#             put first item of odd_pos_S2 list in output string
#             delete first item of odd_pos_S2 list
#         elif odd_pos_S2 list is empty
#             put first item of even_pos_S1 list in output string
#             delete first item of even_pos_S1 list

def get_odd_even_lists(S1, S2):
    even_pos_S2 = []
    odd_pos_S2 = []
    even_pos_S1 = []
    odd_pos_S1 = []

    for i in range(len(S1)):
        if (i+1)%2 == 0:
            # even position
            even_pos_S1.append(S1[i])
        elif (i+1)%2 != 0:
            # odd position
            odd_pos_S1.append(S1[i])

    for i in range(len(S2)):
        if (i+1)%2 == 0:
            # even position
            even_pos_S2.append(S2[i])
        elif (i+1)%2 != 0:
            # odd position
            odd_pos_S2.append(S2[i])
    return even_pos_S1, odd_pos_S1, even_pos_S2, odd_pos_S2

def odd_even_swap(S1, S2):
    even_pos_S1, odd_pos_S1, even_pos_S2, odd_pos_S2 = get_odd_even_lists(S1, S2)
    output_string = ""

    for i in range(len(S1)):
        if (i+1)%2 != 0:
            # odd position
            if even_pos_S2:
                output_string += even_pos_S2[0]
                del even_pos_S2[0]
            elif not even_pos_S2: # even_pos_S2 is empty
                output_string += S1[i]

        elif (i + 1) % 2 == 0:
            # even position
                if odd_pos_S2:
                    output_string += odd_pos_S2[0]
                    del odd_pos_S2[0]
                elif not odd_pos_S2: #odd_pos_S2 is empty
                    output_string += S1[i]

    return output_string

# string_1 = input("enter string one")
# string_2 = input("enter string two")

string_1 = "abcd"
string_2 = "efgh"
# the output string will be: fehg

# string_1 = "ab"
# string_2 = "efgh"
# the output string will be: fe

# string_1 = "abcd"
# string_2 = "fg"
# the output string will be: gfcd

output = odd_even_swap(string_1, string_2)
print(f"the output string will be: {output}")
