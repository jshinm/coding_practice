# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5

class Solution:
    def canJump_I(self, nums: List[int]) -> bool:
        #each number at index i indicates the MAX jump, 
        #thus [3,2,1] can go, for instance, 3(1)-2(1)-1; 3(2)->1; 3, thus True

        #backtracing method
        # [3,2,1,0]
        # 3-0
        # 2-1-0
        # 1-2-0
        # 1-1-1-0
        
        if len(nums) == 1: #single item is always true
            return True
        
        #go backwards and see if there's a path
        #TC: O(N)
        idx = len(nums)-1
        
        for i,n in enumerate(nums[-2::-1]): #starting from the second to the last in reverse
            
            temp_i = len(nums)-(i+2) #current index in forward direction
            if temp_i + nums[temp_i] >= idx: 
                idx = temp_i #update pointer 
        return idx == 0 #the pointer must reach the first index

    def canJump_extra(self, nums: List[int]) -> bool:
        #if the question were to indicate the consecutive jumps
        #while loop {run until reach the end OR reach zero that is not the last index}
        #[1,1,1,2] => True
        #[1,10,1] => True
        
        if len(nums) == 1: #single item is always true
            return True
        
        idx = 0
        
        try:
            while True:
                idx += nums[idx] #move to next index
                
                if idx >= len(nums)-1: #if the next passes the last idx, then it's true
                    return True

                if idx + nums[idx] >= len(nums)-1: 
                    #if the number pointed by the next index is greater than 
                    #or equal to the size of the array, it's true
                    return True                     

                if nums[idx] == 0 and idx != len(nums)-1: 
                    #the only false case is if there's zero prior to reaching the last index
                    return False
                
        except Exception as e:
            print(e)