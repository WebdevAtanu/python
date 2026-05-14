nums = {1, 2, 3, 3, 2}  # sets do not allow duplicate values
print(nums)             # output: {1, 2, 3}
nums.pop()              # remove the last element
nums.add(4)             # add 4 to the set
nums.remove(3)          # remove 3 from the set
nums.clear()            # clear the set

copySet = nums.copy()   # copy the set
print(copySet) 

newSet = set()          # create an empty set
newSet.add(1)           # add 1 to the set
newSet.add(2)           # add 2 to the set
newSet.add(3)           # add 3 to the set
print(newSet)

nums1 = {1, 2, 3}
nums2 = {3, 4, 5}
print(nums1.union(nums2))           # union of nums1 and nums2
print(nums1.intersection(nums2))    # intersection of nums1 and nums2