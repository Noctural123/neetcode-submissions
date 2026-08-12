class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put(']', '[');
        closeToOpen.put(')', '(');
        closeToOpen.put('}', '{');

        for(int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if(!stack.isEmpty() && closeToOpen.containsKey(c)){
                if(closeToOpen.get(c) == stack.peek()){
                    stack.pop();
                }
                else{
                    return false;
                }
            }
            else{
                stack.push(c);
            }
        }
        // if return true then '[' will fail since it never hits the return false
        return stack.isEmpty();
    }
}
