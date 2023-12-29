'''You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j 
where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. 
The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.'''


from functools import cache


class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        
        @cache
        def dp(job_index, current_day, current_day_dificulty, current_day_jobs):
            if current_day > d:
                return float('inf') #infinite difficulty
            if job_index == len(jobDifficulty):
                if current_day == d:
                    return current_day_dificulty
                else:
                    return float('inf')
            # do the job in the current day
            difficulty_do_job_today = dp(job_index+1, current_day, max(current_day_dificulty, jobDifficulty[job_index]), current_day_jobs + 1)

            # do the job the next day
            difficulty_do_job_tomorrow = float('inf')
            if current_day_jobs > 0: # we cannot do nothign in the whole day
                difficulty_do_job_tomorrow = current_day_dificulty + dp(job_index, current_day+1, 0, 0)
 
            return min(difficulty_do_job_today, difficulty_do_job_tomorrow)
        res = dp(0, 1, 0, 0)
        if res == float('inf'):
            return -1
        else:
            return res
        

jobDifficulty = [6,5,4,3,2,1]
d = 2
'''Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7 '''
obj = Solution()
print(obj.minDifficulty(jobDifficulty, d))