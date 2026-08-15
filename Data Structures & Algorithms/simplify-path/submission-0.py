class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for cur in parts:
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "." and cur != "":
                stack.append(cur)
        print(stack)
        return "/" + "/".join(stack)
        
        