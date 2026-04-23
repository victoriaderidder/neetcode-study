class Solution:

    def encode(self, strs: List[str]) -> str:
        # count len(i) in each strs[i] item
        # use count + delimiter to tell us where to decode
        # ex. 4#leet5#co#de
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # i is a pointer here
        res, i = [], 0
        while i < len(s):
            # second pointer
            j = i
            while s[j] != '#':
                j += 1
            # we don't include j in str_len
            # (btw we need the delimiter in case of multi digit str_len)
            # (ex. i == 190)
            str_len = int(s[i:j])
            res.append(s[j+1:j+1+str_len])
            i = j+1+str_len
        return res
