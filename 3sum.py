class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1

                else:
                    r -= 1
        return result


# class Solution:
#     def twoSum(self,target, nums):
#         if not nums or len(nums) == 1:
#             return []
#         if len(nums) == 2:
#             return [nums] if sum(nums) == target else []
#         # return_list
#         rl = []
#         # hashmap to check if the element has been used
#         d = {}
#         for i in range(len(nums)):
#             remain = target - nums[i]
#             if remain in d.keys() :
#                 if d[remain] == False:
#                     # only add to the return_list when the element is unused
#                     rl.append([nums[i], remain])
#                     d[remain] = True
#                     d[nums[i]] = True
#             else:
#                 d[nums[i]] = False
#         return rl

#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if not nums or len(nums) < 3:
#             return []
#         if len(nums) == 3:
#             return [nums] if sum(nums) == 0 else []
#         else:
#             nums.sort()
#             rl = []
#             d = {}
#             i = 0
#             while i < len(nums) and nums[i] <= 0:
#                 if nums[i] not in d.keys():
#                     tl = self.twoSum(-nums[i], nums[i + 1 :])
#                     print(tl)
#                     if tl:
#                         rl += list(map(lambda x : x + [nums[i]], tl))
#                 d[nums[i]] = True
#                 i +=1
#             return rl
