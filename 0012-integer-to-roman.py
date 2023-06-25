class Solution:
    """
    Completed w/o hardcoding in "combination" values.
    """
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M",),
            (500, "D",),
            (100, "C",),
            (50, "L",),
            (10, "X",),
            (5, "V",),
            (1, "I",),
        ]
        res = ""
        for i, roman in enumerate(values):
            if num == 0:
                break
            while roman[0] <= num:
                res += roman[1]
                num -= roman[0]

            if i < len(values) - 1:
                combo_index = i + 2 - (i % 2)
                combo_val = roman[0] - values[combo_index][0]
                if combo_val <= num:
                    res += values[combo_index][1] + roman[1]
                    num -= (roman[0] - values[combo_index][0])

        return res
