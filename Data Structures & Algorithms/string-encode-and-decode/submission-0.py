class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            len_of_word = len(word)
            encoded_string += f"{len_of_word:03d}" + word
        print(encoded_string)
        return encoded_string

    def decode(self, strs: str) -> List[str]:
        result = []
        start_index = 0
        end_index = 3
        while start_index < len(strs):     
            len_of_word = int(strs[start_index:end_index].strip())
            item = strs[end_index:end_index + len_of_word]
            start_index = end_index + len_of_word
            end_index = start_index + 3
            result.append(item)     
        return result
