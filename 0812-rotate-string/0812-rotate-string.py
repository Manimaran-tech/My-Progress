class Solution(object):
    def rotateString(self, s, goal):
        if len(s)==len(goal):
            c=s+s
            if goal in c:
                return True
        else:
            return False