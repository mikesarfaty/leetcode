from itertools import zip_longest

class Solution:
    """
    Lots of helpers, without using ljust/rjust
    """
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        rows = []
        cur_row = [words[0]]
        cur_row_len = len(words[0])
        for word in words[1:]:
            if cur_row_len + len(word) + 1 <= maxWidth: # add to current row
                cur_row_len += len(word) + 1
                cur_row.append(word)
            else: # row is too long, start new row
                rows.append(cur_row)
                cur_row_len = len(word)
                cur_row = [word]
        if cur_row:
            rows.append(cur_row)

        def justify_ctr(row: List[str]):
            spaces_target = maxWidth - sum([len(w) for w in row]) # amt of all space left in line
            spaces_per_word = math.floor(spaces_target / (len(row) - 1)) # amount of spaces for all words
            spaces_left_over = spaces_target % (len(row) - 1) # amount of spaces we have left
            spaces = [" " * spaces_per_word for _ in range(len(row) - 1)]
            for i in range(spaces_left_over):
                spaces[i] += " "
            r = ""
            for w, sp in zip_longest(row, spaces):
                r += w + (sp or "")

            return r

        def justify_left(row):
            l = " ".join(row)
            return l + (" " * (maxWidth - len(l)))

        ret = []
        for row in rows[:-1]:
            if len(row) == 1:
                ret.append(justify_left(row))
            else:
                ret.append(justify_ctr(row))

        ret.append(justify_left(rows[-1]))
        return ret
