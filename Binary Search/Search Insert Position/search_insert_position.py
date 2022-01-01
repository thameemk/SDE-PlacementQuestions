#  Project : SDE Placement Questions
#  Filename : search_insert_position.py
#  Author : thameem
#  Created  time : Sat, 1 Jan 2022 at 8:10 PM India Standard Time
#  Last modified time : Sat, 1 Jan 2022 at 8:10 PM India Standard Time
from beartype import beartype


class SearchInsertPosition:
    @beartype
    def __init__(self: 'SearchInsertPosition', numbers: list[int], target: int) -> None:
        self.numbers = numbers
        self.target = target
        self.target_index = -1
        self.base_index = 0
        self.end_index = len(numbers) - 1
        self.middle_index = -1
        if target > numbers[-1]:
            self.target_index = len(numbers)
        elif target < numbers[0]:
            self.target_index = 0
        else:
            self._search()
            if self.target_index == -1:
                if target > numbers[self.base_index]:
                    self.target_index = self.base_index + 1
                elif target < numbers[self.end_index]:
                    self.target_index = self.end_index + 1

    @beartype
    def _search(self: 'SearchInsertPosition') -> None:
        if self.numbers[self.base_index] <= self.target <= self.numbers[self.end_index]:
            self.middle_index = self.base_index + (self.end_index - self.base_index) // 2
            if self.numbers[self.middle_index] == self.target:
                self.target_index = self.middle_index
            elif self.numbers[self.middle_index] > self.target:
                self.end_index = self.middle_index - 1
                self._search()
            elif self.numbers[self.middle_index] < self.target:
                self.base_index = self.middle_index + 1
                self._search()


if __name__ == '__main__':
    response = SearchInsertPosition(numbers=[1, 2, 4, 6, 7], target=3)
    print(response.target_index)
