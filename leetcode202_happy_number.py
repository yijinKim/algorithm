# yijinKim
class Solution:
	def isHappy(self, n: int) -> bool:

		# 이미 나왔던 수를 저장해놓는 set()
		existed = set()

		# n이 1이 아닐때 계속 무한루프를 돈다.
		while n != 1:
			# n이 no출현했기 때문에 set에 넣어준다.
			existed.add(n)
			# n을 문자열로 반복문을 돌며 하나씩 제곱해서 더한다.
			n = sum([int(i) ** 2 for i in str(n)])
			# n이 이미 나왔던 수라면 false를 리턴한다.
			if n in existed:
				return False
		# n이 1이 될 경우 무한루프를 벗어나면서 true를 리턴한다.
		return True

# Others
# runtime, memory가 더 효율적인 풀이
class Solution:
	def isHappy(self, n: int) -> bool:
		visited = set()

		while True:
			result = 0
			for x in str(n):
				visited.add(int(x))
				result += int(x) * int(x)
			if result == 1:
				return True
			if result in visited:
				return False
			n = result		