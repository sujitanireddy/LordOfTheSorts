#Writing Bubble Sort from Scratch 
#Refrence - https://en.wikipedia.org/wiki/Bubble_sort
#Time Complexity: O(n**2)

"""
Pseudocode
1. Loop through the list and compare adjacent numbers, if the number to the right is less than the number to the left -> Swap them.
    Example: [6,3,2,1] -> Here for the first comparison the number to the right is 3 and number to the left is 6 and 3 < 6, so we swap -> [3,6,2,1].
2. Step 1 is repeated until all elements are sorted.
"""

def bubble_sort(nums):

    #Flag to check if swapping is required
    swapping = True
    end = len(nums)

    while swapping:

        swapping = False

        for i in range(1, end):

            #Checking if right number < left number
            if nums[i] < nums[i-1]:

                #swapping the numbers
                nums[i], nums[i-1] = nums[i-1], nums[i]

                swapping = True

        end -= 1
    
    return nums