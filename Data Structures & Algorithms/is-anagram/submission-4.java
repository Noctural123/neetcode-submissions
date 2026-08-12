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

          return MapS.equals(MapT);

    }
}
