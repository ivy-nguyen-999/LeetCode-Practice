class Solution {
    public int romanToInt(String s) {
        // Adding Symbol and Value to a map 
        Map<Character, Integer> romanNum = new HashMap<Character, Integer>();
        romanNum.put('I', 1);
        romanNum.put('V', 5);
        romanNum.put('X', 10);
        romanNum.put('L', 50);
        romanNum.put('C', 100);
        romanNum.put('D', 500);
        romanNum.put('M', 1000);
        
        int ans = 0;
        
        // Reading the string s
        for(int index = 0; index < s.length(); index++) {
            // the first char
            char s1 = s.charAt(index);
            
            if(index + 1 < s.length()) {
                // the second char
                char s2 = s.charAt(index + 1);
                // value of the current symbol is greater than or equal the next symbol
                if(romanNum.get(s1) >= romanNum.get(s2)) {
                    ans += romanNum.get(s1);
                }
                else {
                    // value of the current symbol is less than the next symbol
                    ans += romanNum.get(s2) - romanNum.get(s1);
                    // increase the index
                    index++;
                }
            }
            else {
                ans += romanNum.get(s1);
            } 
        }
        return ans;
    }
}