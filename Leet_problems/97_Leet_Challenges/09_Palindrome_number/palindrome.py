class Number:
    def __init__(self, x: int):
        self.x = x

    def is_palindrome(self) -> bool:
        if self.x < 0:
            return False
        else:
            str_x = str(self.x)
            # TODO Could you solve it without converting the integer to a string?
            if str_x == str_x[::-1]:
                return True
        return False
