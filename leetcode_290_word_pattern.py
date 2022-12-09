# yijinKim
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # 띄어쓰기 기준으로 리스트를 만든다
        words = s.split(" ")
        # dic[pat] = word 형태로 딕셔너리 사용할것임.
        dic = {}
        # 패턴과 words의 길이가 동일해야하고
        if len(pattern) != len(words):
            return False
        # 패턴의 unique한 문자 개수와 words의 unique한 문자 개수가 동일해야한다
        if len(set(words)) != len(set(pattern)):
            return False
        # zip으로 하나씩 쌍을 이뤄 살펴볼때
        for pat, word in zip(pattern, words):
            # 딕셔너리안에 pattern의 원소가 key로 존재하지 않으면 딕셔너리에 넣어준다
            if pat not in dic:
                dic[pat] = l
            # key로 존재하면 해당 value값이 쌍인 word값과 동일한지 살펴준다.
            else:
                if dic[pat] != l:
                    return False
        return True

# Others
class Solution(object):
    def wordPattern(self, pattern, str):        
        # split str into single words.
        slist = str.split()
   
        # here we need to consider the len difference
        # eg: pattern:"aaa" str:"aa aa aa aa"
        if len(pattern) != len(slist):
            return False
        
        # just like we do in isomorphic problem.
        return (len(set(pattern)) == len(set(slist)) == len(set(zip(pattern, slist))))