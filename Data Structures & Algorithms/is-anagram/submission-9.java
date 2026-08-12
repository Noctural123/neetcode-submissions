class Solution {
    public boolean isAnagram(String s, String t) {

        HashMap<Character, Integer> mapS = new HashMap<>();
        HashMap<Character, Integer> mapT = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            mapS.put(ch, mapS.getOrDefault(ch, 0)+1);
        }

        for(int i = 0; i < t.length(); i++){
            char ch = t.charAt(i);
            mapT.put(ch, mapT.getOrDefault(ch, 0)+1);
        }

        return mapT.equals(mapS);
    }
}
