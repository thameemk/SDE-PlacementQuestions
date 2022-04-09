#  Project : SDE Placement Questions
#  Filename : BalancedBrackets.py
#  Author : blacklist
#  Current modification time : Thu, 7 Apr 2022 at 10:44 PM India Standard Time
#  Last modified time : Thu, 7 Apr 2022 at 10:44 PM India Standard Time

class BalancedBrackets:
    def __init__(self, brackets: str) -> None:
        self.status: bool = False
        stack = []
        for bracket in brackets:
            if bracket == '[':
                stack.append(bracket)
            else:
                pass


if __name__ == '__main__':
    response = BalancedBrackets(brackets="[[[[][]]]]")
    print(response.status)


"""
Question: https://www.educative.io/courses/learn-python-3-from-scratch/gkLkzNz48Q6
"""