class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def string_to_num(num_str):
            num = 0
            for i, c in enumerate(num_str[::-1]):
                num += (10**i) * (ord(c) - ord('0'))
            return num
        return str(string_to_num(num1) * string_to_num(num2))