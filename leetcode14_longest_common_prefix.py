# yijinKim
class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		# 원소 길이 기준 오름차순 정렬
		strs.sort(key = lambda x: len(x))

		# 빈 배열 "" 리턴
		if len(strs) == 0:
			return ""
		# 가장 짧은 원소 인덱스 0부터 차례대로 루프
		for i in range(len(strs[0])):
			# 다음 짧은 원소부터 돌면서 common prefix 만들어지는지 확인
			for j in range(1, len(strs)):
				if strs[0][i] ~= strs[j][i]:
					return strs[0][:i]
		return strs[0]