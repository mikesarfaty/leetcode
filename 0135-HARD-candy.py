class Solution:
    """
    Modified search alorithm: Spread right and left, stop when
    I have a better rating but fewer candies than my neighbor,
    and begin search again
    """
    def candy(self, ratings: List[int]) -> int:
        bot_i = None
        bot_r = float("+inf")
        for idx, r in enumerate(ratings):
            if r < bot_r:
                bot_r = r
                bot_i = idx
            if r == 0:
                break

        candies = [1 for _ in range(len(ratings))]
        total_candies = len(ratings)

        search = [bot_i]
        while search:
            search_i = search.pop()
            nextr = self.spread(search_i, ratings, candies, 1)
            nextl = self.spread(search_i, ratings, candies, -1)
            if nextr is not None and nextr not in search:
                search.append(nextr)
            if nextl is not None and nextl not in search:
                search.append(nextl)

        return sum(candies)

    def spread(self, start, ratings, candies, direction):
        prev_rating = ratings[start]
        prev_candies = candies[start]
        new_c = 0

        i = start + direction
        while 0 <= i < len(ratings):
            i_rating = ratings[i]
            i_candies = candies[i]
            if i_rating > prev_rating:
                if i_candies <= prev_candies:
                    new_c += 1
                    candies[i] = prev_candies + 1
            elif i_rating < prev_rating:
                if i_candies >= prev_candies:
                    return i

            prev_rating = i_rating
            prev_candies = candies[i]
            i += direction

        return None
