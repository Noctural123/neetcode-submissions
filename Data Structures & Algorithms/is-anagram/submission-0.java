class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> MapS = new HashMap<>();
        HashMap<Character, Integer> MapT = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char sChar = s.charAt(i);
            MapS.put(sChar, MapS.getOrDefault(sChar, 0) + 1);

            char tChar = t.charAt(i);
            MapT.put(tChar, MapT.getOrDefault(tChar, 0) + 1);
        }

        for(char c : MapS.keySet()){
            if(!MapT.containsKey(c) || !MapS.get(c).equals(MapT.get(c))){
                return false;
            }
        }

        return true;
    }
}
