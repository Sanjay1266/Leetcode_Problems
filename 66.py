class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in digits:
            num = num *10 + int(i)
        num = num + 1
        arr = []
        string = str(num)
        for k in string:
            arr.append(int(k))
        return arr

        # string = str(cur)
        # arr = []
        # for i in string:
        #     arr.append(int(i))
        # return arr

        