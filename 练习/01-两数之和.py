from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                          # 数字 -> 它的下标
        for i, num in enumerate(nums):     # i 是下标，num 是值
            # 1. 算出我要找的另一个数
            
            # 2. 如果它在 seen 里，return 两个下标（注意哪个在前）
            # 3. 把当前的 num 和 i 记进 seen
        
        return []