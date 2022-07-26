class Solution:
    def interpret(self, command: str) -> str:
        res = []
          
        for i in range(len(command)):
            if command[i]== '(' and command[i+1] == ')':
                res.append('o')
            
            elif command[i]== '(' and command[i+1] != ')':
                pass
            elif command[i]== ')' and command[i-1] != ')':
                pass
            
            else:
                res.append(command[i])
        
        return ''.join(res)
