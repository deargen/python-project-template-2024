from dataclasses import dataclass


@dataclass
class TwoNumbers:
    """
    정수 두 개 더하는 클래스
    """

    num_1: int
    num_2: int

    def add(self):
        """
        Add two numbers together.

        Examples:
            >>> TwoNumbers(1, 2).add()
            4

            >>> TwoNumbers(1, -1).add()
            0

        Returns:
            (int): The sum of the two numbers.
        """
        assert isinstance(self.num_1, int)
        assert isinstance(self.num_2, int)
        return self.num_1 + self.num_2
