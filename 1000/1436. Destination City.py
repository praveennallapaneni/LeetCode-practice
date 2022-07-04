class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        d = dict(paths)
        
        for city in d.values():
            if city not in d.keys():
                return city
