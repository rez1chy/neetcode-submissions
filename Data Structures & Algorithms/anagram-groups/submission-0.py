class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return []
            
        # 1. Sort the entire array using the sorted characters as the key
        sorted_list = sorted(strs, key=sorted) 
        
        result = []
        current_group = [sorted_list[0]] # Initialize with the first word
        
        # 2. Iterate up to the second-to-last element to avoid IndexError
        for i in range(len(sorted_list) - 1):
            if sorted(sorted_list[i]) == sorted(sorted_list[i+1]):
                current_group.append(sorted_list[i+1])
            else:
                result.append(current_group)
                current_group = [sorted_list[i+1]]
                
        # 3. Append the final remaining group
        result.append(current_group)
        return result

