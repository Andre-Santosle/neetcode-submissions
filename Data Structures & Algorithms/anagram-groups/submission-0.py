class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_list = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in sorted_list:
                sorted_list[sorted_word] = []

            sorted_list[sorted_word].append(word)

        return list(sorted_list.values())
