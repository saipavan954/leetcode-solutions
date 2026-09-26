class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        n = len(nums)
        ans = 0

        def isPrime(x):
            if x < 2:
                return False

            i = 2
            while i * i <= x:
                if x % i == 0:
                    return False
                i += 1

            return True

        for i in range(n):
            # Main diagonal
            if isPrime(nums[i][i]):
                ans = max(ans, nums[i][i])

            # Other diagonal
            if isPrime(nums[i][n - 1 - i]):
                ans = max(ans, nums[i][n - 1 - i])

        return ans