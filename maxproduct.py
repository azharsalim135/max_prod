my_list = [
    -1,
    -2,
    -6,
    -7,
    -3,
    -10,
    0
]      # Define the list where we need to find max product of three numbers.
print(my_list)

def maxProd(list):
    list.sort()         # Sorting the list
    if max(list) >= 0:  
        # If the largest value in the list is equal to or greater than zero, then we have two possibilities.
# 1) We can multiply the last three values in the list.
# and
# 2) We can multiply the first two negative values and the last non-negative value.
# In both cases, the result is positive or zero.

        if list[-1] * list[-2] * list[-3] > list[0] * list[1] * list[-1]: # Here we check which of the two possibilities has the larger number, and print those values
            print("Three numbers are %d , %d, %d " % (list[-1], list[-2], list[-3]))  
        else:
            print("Three numbers are %d, %d, %d " % (list[0], list[1], list[-1]))
        return max(list[-1] * list[-2] * list[-3], list[0] * list[1] * list[-1])

    else:
#         If the largest value in the list is not a zero or a positive integer, then all the values in the list are negative.
# When all the values in a sorted list are negative, to find the maximum of the product of three numbers, we multiply the first three elements.
        print("Three numbers are %d, %d, %d " % (list[-1], list[-2], list[-3]))
        return list[-1] * list[-2] * list[-3]


print(maxProd(my_list))
