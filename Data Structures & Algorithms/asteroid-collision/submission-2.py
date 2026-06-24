class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast_stack = []
        for incoming in asteroids: 
            is_alive = True           
            while ast_stack and incoming < 0 and ast_stack[-1] > 0 and is_alive:
                outgoing = abs(ast_stack[-1])
                if abs(incoming) > outgoing:
                    ast_stack.pop()
                elif abs(incoming) < outgoing:
                    is_alive = False
                else:
                    abs(incoming) == outgoing
                    ast_stack.pop()
                    is_alive = False
            if is_alive:
                ast_stack.append(incoming)
        return ast_stack        
            
                
                
                
                
                
                
                
                
                
                
                
                
                
                

