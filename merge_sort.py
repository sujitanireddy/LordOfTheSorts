#Writing Merge Sort from Scratch
#Date: Dec 8th 2025
#Refrence: https://en.wikipedia.org/wiki/Merge_sort
#Time Complexity: O(n*logn)

"""
Pseudocode:
1. Split the array into two halves recursively until only one number is in the left and right splits of the array.
2. Compare the left and right side of the array.
    - If the left side is smaller than right side. Add the left side number to the final sorted array.
    - else: add the right side to the final sorted array.
    - If any elements are left over in either left side or right side, add them to the final sorted array.
3. Return the final merged sorted array
"""

def merge_sort(nums):

    #Basecase
    if len(nums) < 2:
        return nums
    
    #Floor division as we only want int type
    median = len(nums)//2

    #Splitting into left and right sides using list slicing and recursively calling merge_sort until the base case is satisfied, i.e returning only one number in the list.
    left_side = merge_sort(nums[:median])
    right_side = merge_sort(nums[median:])

    #Final sorted list
    sorted_list = []

    #Indx for left_side and right_side
    i = j = 0

    #Loop for comparing left_side number to right_side number and appending accordingly for sorting.
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            sorted_list.append(left_side[i])
            i+=1
        else:
            sorted_list.append(right_side[j])
            j+=1
    
    #Loops for adding left over numbers in either left_side or right_side lists
    while i < len(left_side):
        sorted_list.append(left_side[i])
        i+=1
    
    while j < len(right_side):
        sorted_list.append(right_side[j])
        j+=1
    
    return sorted_list