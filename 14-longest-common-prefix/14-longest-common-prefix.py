class Solution:
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # handle the case the array is 1
        if(len(strs) == 1):
            return strs[0]
        # if the array has more than 1 element
        result = ""
        index = 0
        
        # loop thru each string until stop
        stop = True
        while(stop):
            # handle empty string
            if (len(strs[0]) <= index):
                return result
            
            # use the first string to compare with the rest
            tempLetter = strs[0][index]
            for str in strs:
                # handle empty string
                if (len(str) <= index):
                    return result
                
                # if there is uncommon prefix, break the loop
                if str[index] != tempLetter:
                    stop = False
                    break
            if(stop):
                result += tempLetter
            # increment index
            index += 1
                
        return result
            