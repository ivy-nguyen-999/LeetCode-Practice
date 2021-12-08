class Solution {
    public boolean isPalindrome(int x) {
        String number = String.valueOf(x);
        char[] digit = number.toCharArray();
        for(int index = 0; index < number.length()/2; index++){
            if(digit[index] != digit[number.length()-1-index]){
                return false;
            }
        }
        return true;
    }
}