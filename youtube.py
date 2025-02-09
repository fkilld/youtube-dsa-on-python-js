# 0 Reverse the array
# Input: arr[] = {1, 4, 3, 2, 6, 5}  
# Output: {5, 6, 2, 3, 4, 1}
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# def reverse_array(arr):
#     left = 0;
#     right= len(arr)-1
#     while left < right:
#         arr[left],arr[right]=arr[right],arr[left]
        
#         left+=1
#         right-=1
#     return arr

# print(reverse_array([1, 4, 3, 2, 6, 5]))
# Input: arr[] = {4, 5, 1, 2} 
# Output: {2, 1, 5, 4}
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.


# 	1	
# Find the maximum and minimum element in an array

# Input: arr[] = [3, 2, 1, 56, 10000, 167]
# Output: 1 10000
# Explanation: minimum and maximum elements of array are 1 and 10000.




# def find_max_min(arr):
#     maxe = arr[0]
#     mine = arr[0]
#     i = 0
#     l = len(arr)
#     while i < l :
#         if arr[i]>maxe:
#             maxe =arr[i]
#         if arr[i] < mine:
#             mine = arr[i]
#         i+=1
#     return   mine,maxe

# arr = [3, 2, 1, 56, 10000, 167]
# min_val, max_val = find_max_min(arr)
# print(min_val, max_val)


# 	2	
# Find the "Kth" max and min element of an array

def kth_smallest(arr, k):
    i =0
    while i <k :
        mini = i
        j= i+1
        while j<len(arr):
            if arr[j]<arr[mini]:
                mini = j
            j+=1
        arr[i],arr[mini]=arr[mini],arr[i]
        i+=1
    return arr[k-1]

def kth_largest(arr, k):
    i =0
    while i <k :
        maxi = i
        j= i+1
        while j<len(arr):
            if arr[j]>arr[maxi]:
                maxi = j
            j+=1
        arr[i],arr[maxi]=arr[maxi],arr[i]
        i+=1
    return arr[k-1]
arr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth smallest element:", kth_smallest(arr.copy(), k))
print("Kth largest element:", kth_largest(arr.copy(), k))

















# 	3	
# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

# 	4	
# Move all the negative elements to one side of the array

# 	5	
# Find the Union and Intersection of the two sorted arrays.

# 	6	
# Write a program to cyclically rotate an array by one.

# 	7	
# find Largest sum contiguous Subarray [V. IMP]

# 	8	
# Minimise the maximum difference between heights [V.IMP]

# 	9	
# Minimum no. of Jumps to reach end of an array

# 	10	
# find duplicate in an array of N+1 Integers

# 	11	
# Merge 2 sorted arrays without using Extra space.
# icon
# 	12	
# Kadane's Algo [V.V.V.V.V IMP]
# icon
# 	13	
# Merge Intervals

# 	14	
# Next Permutation

# 	15	
# Count Inversion

# 	16	
# Best time to buy and Sell stock

# 	17	
# find all pairs on integer array whose sum is equal to given number

# 	18	
# find common elements In 3 sorted arrays

# 	19	
# Rearrange the array in alternating positive and negative items with O(1) extra space

# 	20	
# Find if there is any subarray with sum equal to 0

# 	21	
# Find factorial of a large number

# 	22	
# find maximum product subarray

# 	23	
# Find longest consecutive subsequence

# 	24	
# Given an array of size n and a number k, find all elements that appear more than " n/k " times.

# 	25	
# Maximum profit by buying and selling a share atmost twice

# 	26	
# Find whether an array is a subset of another array

# 	27	
# Find the triplet that sum to a given value

# 	28	
# Trapping Rain water problem

# 	29	
# Chocolate Distribution problem

# 	30	
# Smallest Subarray with sum greater than a given value

# 	31	
# Three way partitioning of an array around a given value

# 	32	
# Minimum swaps required bring elements less equal K together

# 	33	
# Minimum no. of operations required to make an array palindrome

# 	34	
# Median of 2 sorted arrays of equal size

# 	35	
# Median of 2 sorted arrays of different size