class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        res =set()
        codes = {"a": ".-", 
                 "b": "-...", 
                 "c": "-.-.", 
                 "d": "-..", 
                 "e": ".", 
                 "f": "..-.", 
                 "g": "--.", 
                 "h": "....", 
                 "i":"..", 
                 "j": ".---", 
                 "k": "-.-", 
                 "l": ".-..", 
                 "m": "--", 
                 "n": "-.", 
                 "o": "---", 
                 "p": ".--.", 
                 "q": "--.-",
                 "r": ".-.", 
                 "s": "...", 
                 "t": "-", 
                 "u": "..-", 
                 "v": "...-", 
                 "w": ".--", 
                 "x": "-..-", 
                 "y": "-.--", 
                 "z": "--.."}
        
        for i in words:
            morse =[]
            for j in i:
                morse.append(codes[j])
            
            res.add("".join(morse)) # conerting list to string
        
        return len(res)
