


numbers= [10,20,10,40,50,60,70]
target=120 

class py_solution:
  def twoSum(self, nums, target):
       lookup = {}
       for i, num in enumerate(nums):
           if target - num in lookup:
               return (lookup[target - num], i+1 )
           lookup[num] = i+1
print(py_solution().twoSum((numbers),target))
