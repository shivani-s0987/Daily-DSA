class solution(object):
    def singleNumber(self,nums):
        result=0
        for i in nums:
            result^=1
        return result