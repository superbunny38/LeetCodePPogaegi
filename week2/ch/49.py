class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def get_ord(letters):
        #     ord_ = 0
        #     for letter in letters:
        #         ord_ += ord(letter)
        #     return ord_
        ret = dict()
        for str_ in strs:
            ord_str_ = "".join(sorted(list(str_)))
            if ord_str_ in ret:
                ret[ord_str_].append(str_)
            else:
                ret[ord_str_] = [str_]
        return list(ret.values())
