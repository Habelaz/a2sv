class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = []
        minn = float('inf') 
        in_dict = {word: i for i, word in enumerate(list1)}
        for j, word in enumerate(list2):
            if word in in_dict:
                current_ind = in_dict[word] + j

                
                if current_ind < minn:
                    minn = current_ind
                    common_strings = [word]
                elif current_ind == minn:
                    common_strings.append(word)

        return common_strings
        
