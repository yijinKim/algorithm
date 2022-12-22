class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        ans = 0
        dic = {}
        for i in tasks:
            dic[i] = dic.get(i,0) + 1
        
        count = [dic[task] for task in dic]
        max_count = max(count)
        max_count_tasks = count.count(max_count)
        ans =  max_count + (max_count-1)*n +(max_count_tasks) - 1
        return max(len(tasks), ans)