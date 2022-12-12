# ord() 사용 방법
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str_to_int(num_str):
            num = 0
            for i, c in enumerate(num_str[::-1]):
                num += pow(10, i) * (ord(c) - ord('0'))
            return num

        return str(str_to_int(num1) * str_to_int(num2))

# hash사용 방법
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                       '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        def str_to_int(num_str):
            num = 0
            for i, c in enumerate(num_str[::-1]):
                num += pow(10, i) * num_mapping[c]
            return num

        return str(str_to_int(num1) * str_to_int(num2))        