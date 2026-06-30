class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroid_stack = []

        for i, ast in enumerate(asteroids):
            is_alive = True
            while asteroid_stack and is_alive and asteroid_stack[-1] > 0 and ast < 0:
                if abs(ast) > abs(asteroid_stack[-1]):
                    asteroid_stack.pop()
                elif abs(ast) == abs(asteroid_stack[-1]):
                    asteroid_stack.pop()
                    is_alive = False
                else:
                    is_alive = False
            if is_alive:
                asteroid_stack.append(ast)
        return asteroid_stack
        