class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #brute force approach will be check every characters within each elements
        #more optimization can be done by..

        #first we will check the length of list
            #if length of list > 1 we can start comparison otherwise return the str straight away
        #

        if len(strs) < 2:
            print(len(strs))
            return [strs]

        else:

            anagram_map = defaultdict(list)

            for word in strs:
                # 1. Sort the characters of the word to create a unique key
                # 'cat' and 'act' both become 'act'
                sorted_key = "".join(sorted(word))
        
                # 2. Append the original word to the matching hash table list
                anagram_map[sorted_key].append(word)
        
                # Return just the grouped lists from the hash table
            return list(anagram_map.values())


