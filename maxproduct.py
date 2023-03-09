my_list = [
    -1,
    -2,
    -6,
    0,
    1,
    2,
    6,
    
]  # Define the list where we need to find max product of three numbers.
print(my_list)


def maxProd(list):
    list.sort()  # Sorting the list

    SMALLEST = list[0]
    SECOND_SMALLEST = list[1]
    LARGEST = list[-1]
    SECOND_LARGEST = list[-2]
    THIRD_LARGEST = list[-3]

    if max(list) >= 0:
        # If the largest value in the list is equal to or greater than zero, then we have two possibilities.
        # 1) We can multiply the last three values in the list.
        # and
        # 2) We can multiply the first two negative values and the last non-negative value.
        # In both cases, the result is positive or zero.

        # if (
        #     LARGEST * SECOND_LARGEST * THIRD_LARGEST
        #     > SMALLEST * SECOND_SMALLEST * LARGEST
        # ):
        #     print(
        #         "Three numbers are %d , %d, %d "
        #         % (LARGEST, SECOND_LARGEST, THIRD_LARGEST)
        #     )
        # else:
        #     print(
        #         "Three numbers are %d, %d, %d " % (SMALLEST, SECOND_SMALLEST, LARGEST)
        #     )

        # PS. above if conditions ( lines 30 to 41) are only used to print the elements whose products are the largest, only follwing statement is reqruired

        return max(
            LARGEST * SECOND_LARGEST * THIRD_LARGEST,
            SMALLEST * SECOND_SMALLEST * LARGEST,
        )

    else:
        #         If the largest value in the list is not a zero or a positive integer, then all the values in the list are negative.
        # When all the values in a sorted list are negative, to find the maximum of the product of three numbers, we multiply the last three elements.
        print(
            "Three numbers are %d, %d, %d " % (LARGEST, SECOND_LARGEST, THIRD_LARGEST)
        )
        return LARGEST * SECOND_LARGEST * THIRD_LARGEST


print("Result: ",maxProd(my_list))
