'''Yacht dice game'''
# Score categories.
# Change the values as you see fit.
YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full house"
FOUR_OF_A_KIND = "four-of-a-kind"
LITTLE_STRAIGHT = "little-straight"
BIG_STRAIGHT = "big-straight"
CHOICE = "choice"


def score(dice, category):
    """
    Given a list of values for five dice and a category, your
    solution should return the score of the dice for that category.
    If the dice do not satisfy the requirements of the category your
    solution should return 0. You can assume that five values will
    always be presented, and the value of each will be between one
    and six inclusively. You should not assume that the dice are
    ordered.
    :param dice: list of values for five dice
    :param category: category to score the dice against
    :return: score of the dice for that category
    """
    
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    elif category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        return sum(dice) if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3) else 0
    elif category == FOUR_OF_A_KIND:
        """
        At least four dice showing the same face
        return Total of the four dice
        4 4 4 4 6 scores 16 (4+4+4+4)
        """
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 4 or dice.count(dice[0]) == 1):
        # return Total of the four dice
            if dice.count(dice[0]) == 4:
                return dice[0] * 4
            else:
                return dice[1] * 4
        elif len(set(dice)) == 1:
            return dice[0] * 4
        else: return 0
    elif category == LITTLE_STRAIGHT:
        """
        1-2-3-4-5
        """
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    elif category == BIG_STRAIGHT:
        """
        2-3-4-5-6
        """
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    elif category == CHOICE:
        return sum(dice)
    else:
        return 0
