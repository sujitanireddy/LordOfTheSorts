#Writing Insertion sort form scratch
#Date: Dec 9th 2025
#Refrence: https://en.wikipedia.org/wiki/Insertion_sort
#Learning Resource - https://www.youtube.com/watch?v=By_5-RRqVeE
#Time Complexity: O(n**2)


"""
Pseudocode:
1. For every ith idx in the list, trigger jth idx which will compre the LHS of the ith idx and swap until the LHS
of the list is sorted.
"""

def insertion_sort(nums):

    #Loop with start from 1st index as we have to compare i-1 index as well.
    for i in range(1, len(nums)):
        j = i
        
        #Inner loop that does the LHS comparison and do the swapping. Using While Loop as we don't know how many times the loop should run.
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    
    return nums

print(insertion_sort(nums=[6,7,8,4,3,2]))

