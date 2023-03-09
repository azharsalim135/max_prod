# max_prod
## Problem: Find the largest product of 3 integers in an array/list 

Here we have list of intgers, and we have to find the largest product of 3 integers in the list.
In this secenerio we have 3 possible type of list

1. List with all +ve integers
2. List with all negative integers
3. Mix of positive, negative and zero

## Solution

<b> First: </b> sort the list 

<b> Second: </b>  Check weather if the sorted list contains negative values only. 
         If this condintion is false, Then we have two possibilties. 
         ie. if( max(list) <= 0 ), then
         
         possibility  one: Largest product of 3 integers are multiplication of 3 positive integers.
                           If this is true, then max_product = LARGEST * SECOND_LARGEST * THIRD_LARGEST
         
         possibiltity two: Largest product of 3 integers are multiplication two negative integers and a positive integer.
                           If this is true, then product = SMALLEST * SECOND_SMALLEST * LARGEST. (where SMALLEST and SECOND_SMALLEST are negative values. -ve*-ve is +ve)
         
         
Here we check both of these possilities and compare which value is largest and return largest amogst the two.

         ie. return max(LARGEST * SECOND_LARGEST * THIRD_LARGEST, SMALLEST * SECOND_SMALLEST * LARGEST)     
         
<b> Third: </b>  If the sorted list only contains negative numbers, then the largest of product of 3 integers will be

          LARGEST * SECOND_LARGEST * THIRD_LARGEST

In a ordred list of negetive numbers, numbers close to zero will be the largest one.

## Results

                           [-1, -2, -6, -7, -3, -10]
                           Three numbers are -1, -2, -3
                           -6
                           
                           [-1, -2, -6, -7, -3, -10, 10]
                           Three numbers are -10, -7, 10
                           Result:  700
                           
                           [-1, -2, -6, 0, 1, 2, 6]
                           Three numbers are -6, -2, 6
                           Result:  72

