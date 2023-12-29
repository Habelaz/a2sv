class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            num = str(num)
            num = [int(n) for n in num]
            num.sort()
            ans = ''
            count = 0

            for i in num:
                if i == 0:
                    count += 1
                    continue
                ans += str(i)
                
            ans = ans[0] + '0' * count + ans[1:]
            return int(ans)
        else:
            num = abs(num)
            num = str(num)
            nums = [int(n) for n in num]
            nums.sort()
            print(nums)
            ans = ''
            for i in range(len(nums)-1,-1,-1):
                ans += str(nums[i])
            return -1 * int(ans)
