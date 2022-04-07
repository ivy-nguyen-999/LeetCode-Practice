class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:        
        # sorted the array
        arr.sort()
        # store the result
        occur = 0
        
        for i in range(len(arr) - 2):
            j, k = i + 1, len(arr) - 1
            
            while j < k:
                threeSum = arr[i] + arr[j] + arr[k]
                if threeSum < target:
                    j += 1
                elif threeSum > target:
                    k -= 1
                elif arr[j] != arr[k]: # threeSum == target
                    numJ, numK = 1, 1
                    j += 1
                    k -= 1
                    while j <= k and arr[j] == arr[j - 1]:
                        numJ += 1
                        j += 1
                    while j <= k and arr[k] == arr[k + 1]:
                        numK += 1
                        k -= 1
                    occur += (numJ * numK)
                else: #arr[j] == arr[k]
                    M = k - j + 1
                    pairs = int(M * (M-1) / 2)
                    occur += pairs
                    break
                    
        return occur % (10**9 + 7)
