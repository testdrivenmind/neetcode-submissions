class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            len_of_word = len(word)
            encoded_string += f"{len_of_word:03d}" + word
        print(encoded_string)
        return encoded_string

    def decode(self, encoded_str: str) -> List[str]:
        result = []
        start_index = 0
        end_index = 3
        while start_index < len(encoded_str):     
            len_of_word = int(encoded_str[start_index:end_index])
            item = encoded_str[end_index:end_index + len_of_word]
            start_index = end_index + len_of_word
            end_index = start_index + 3
            result.append(item)     
        return result
