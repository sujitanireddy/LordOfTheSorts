#Writing Selction sort from scratch
#Date: Dec 12th 2025
#Time Complexity: O(n**2)

def selection_sort(nums):

    #Range from 1st index to the last in the list
    for i in range(len(nums)):

        smallest_idx = i

        #For every number at index i, compare every other number in the inner loop to find the min number
        for j in range(i+1, len(nums)):

            if nums[j] < nums[smallest_idx]:
                
                smallest_idx = j
        
        #At the end of this inner loop, we will have the smallest number, lets swap

        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]

    return nums