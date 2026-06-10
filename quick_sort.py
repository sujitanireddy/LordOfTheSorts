#Writing Quick sort from scratch 
#Date: Dec 11th 2025
#Reference: https://en.wikipedia.org/wiki/Quicksort
#Time Complexity: Average & Best Case: O(n*logn), Worst Case: O(n**2) 


#Nums is the list of numbers, low = 0, high = len(nums) - 1 (last index)
def quick_sort(nums, low, high):

    if low < high:

        #Partition function will return the pivot index after placing the pivot index number in it's correct position
        pivot_index = partition(nums, low, high)
        
        #recursively calling partition on left side of the array 
        quick_sort(nums, low, pivot_index -1 )

        #recursively calling partition on the right side of the array
        quick_sort(nums, pivot_index + 1, high)


def partition(nums, low, high):

    #ith index starts at -1
    i = low - 1
    pivot = nums[high]

    for j in range(low, high):
        if nums[j] < pivot:
            i += 1 

            #Swap
            nums[i], nums[j] = nums[j], nums[i]
    
    #Placing the pivot element in it's sorted position
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i + 1
