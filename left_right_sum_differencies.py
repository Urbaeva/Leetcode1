def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftArr = [0] * n
        rightArr = [0] * n
        i = 1
        while i < n:
            leftArr[i] = leftArr[i - 1] + nums[i - 1]
            i += 1

        j = n - 2
        while j >= 0:
            rightArr[j] = rightArr[j + 1] + nums[j + 1]
            j -= 1

        resultArr = []
        for k in range(n):
            resultArr.append(abs(leftArr[k]-rightArr[k]))
        return resultArr
        
