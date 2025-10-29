class Solution(object):
    def longestCommonPrefix(self, strs):
        init= strs[0]
        for i in strs[1:]:
            while not i.startswith(init):
                init = init[:-1]
                if init=="":
                    return ""
        return init
            


