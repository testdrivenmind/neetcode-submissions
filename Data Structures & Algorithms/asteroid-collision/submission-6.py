class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ast_stack = []

        for ast in asteroids:
            is_alive = True
            while ast_stack and is_alive and ast < 0 and ast_stack[-1] > 0:
                if abs(ast) > abs(ast_stack[-1]):
                    ast_stack.pop()
                elif abs(ast) < abs(ast_stack[-1]):
                    is_alive = False
                else:
                    is_alive = False
                    ast_stack.pop()
            if is_alive:
                ast_stack.append(ast)  
        return ast_stack