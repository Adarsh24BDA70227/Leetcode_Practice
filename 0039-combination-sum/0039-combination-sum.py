class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        def backtrack(start, rem, path):
            if rem == 0:
                res.append(list(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > rem:
                    break
                path.append(candidates[i])
                backtrack(i, rem - candidates[i], path)
                path.pop()
        backtrack(0, target, [])
        return res                
        


        



       
        