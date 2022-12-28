class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        res = sum(piles)
        piles = [-pile for pile in piles]
        i = 0
        heapq.heapify(piles)
        while i < k:
            pile = heapq.heappop(piles)
            pospile = -pile
            res -= pospile // 2
            heapq.heappush(piles, pile + pospile // 2)
            i += 1
        return res