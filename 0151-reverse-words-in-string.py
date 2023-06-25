class Solution:
    """
    could replace all tokenization with the following:
    tokens = [word for word in s.split(" ") if word]
    but it's a little slower...
    """
    def reverseWords(self, s: str) -> str:
        tokens = []
        cur = ""
        for c in s:
            if c == " ":
                if cur:
                    tokens.append(cur)
                    cur = ""
            else:
                cur += c

        if cur:
            tokens.append(cur)

        return " ".join(tokens[::-1])
