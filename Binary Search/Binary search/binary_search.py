#  Project : SDE Placement Questions
#  Filename : binary_search.py
#  Author : thameem
#  Created  time : Wed, 29 Dec 2021 at 12:54 AM India Standard Time
#  Last modified time : Wed, 29 Dec 2021 at 12:30 AM India Standard Time

from beartype import beartype


class BinarySearch:
    @beartype
    def __init__(self: 'BinarySearch', numbers: list[int], target_number: int) -> None:
        self.numbers = numbers
        self.target_number = target_number
        self.target_index = -1
        self.base_index = 0
        self.end_index = len(numbers) - 1
        self.middle_index = -1
        self._search()

    @beartype
    def _search(self: 'BinarySearch') -> None:
        if self.numbers[self.base_index] <= self.target_number <= self.numbers[self.end_index]:
            self.middle_index = self.base_index + (self.end_index - self.base_index) // 2
            if self.numbers[self.middle_index] == self.target_number:
                self.target_index = self.middle_index
            elif self.numbers[self.middle_index] > self.target_number:
                self.end_index = self.middle_index - 1
                self._search()
            elif self.numbers[self.middle_index] < self.target_number:
                self.base_index = self.middle_index + 1
                self._search()


if __name__ == '__main__':
    result = BinarySearch(numbers=[-1, 0, 3, 5, 9, 12], target_number=13)
    print(result.target_index)
