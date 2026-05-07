nums = {1, 2, 3, 3, 2}
print(nums)
nums.pop() # remove the last element
nums.add(4) # add 4 to the set
nums.remove(3) # remove 3 from the set
nums.clear() # clear the set

copySet = nums.copy() # copy the set
print(copySet) 

newSet = set() # create an empty set
newSet.add(1)
newSet.add(2)
newSet.add(3)
print(newSet)

nums1 = {1, 2, 3}
nums2 = {3, 4, 5}
print(nums1.union(nums2)) # union of nums1 and nums2
print(nums1.intersection(nums2)) # intersection of nums1 and nums2