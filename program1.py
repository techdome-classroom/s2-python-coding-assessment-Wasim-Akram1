class Solution(object):
    def isValid(self, s:str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        while True:
            if '()' in s:
                s=s.replace('()','')
            elif '{}' in s:
                s=s.replace('{}','')
            elif '[]'in s:
                s=s.replace('[]','')
            else:
                return not s
            
        pass







    



  

