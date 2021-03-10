class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash_table = {}
        
        
        for string in strs:
            
            ss = ''.join(sorted(string))
            
            if ss in hash_table:
                hash_table[ss].append(string)
            
            else:
                hash_table[ss] = [string]
            
        return hash_table.values()
        