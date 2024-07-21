from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int


class Scoreboard[T]:
    def __init__(self, size: int = 10):
        self._n = 0  # Number of currently stored Scores
        self._board = [None] * size

    def __getitem__(self, index: int) -> T:
        return self._board[index]

    def __str__(self) -> str:
        return "\n".join(f"{i}. {str(record)}" for i, record in enumerate(self._board))

    def read(self) -> list[T]:
        return [obj for obj in self._board if obj is not None]

    def add(self, obj: T) -> None:
        # Is score is high enough to qualify for Scoreboard?
        if not (self._n < len(self._board) or obj.score >= self._board[-1].score):
            return

        if self._n < len(self._board):  # Scoreboard is not full, add additional record
            self._n += 1

        i = self._n - 1
        while i > 0 and self._board[i - 1].score <= obj.score:
            self._board[i] = self._board[i - 1]
            i -= 1
        self._board[i] = obj


def test_Scoreboard():
    scoreboard = Scoreboard(size=5)

    player1 = Player("a", 10)
    player2 = Player("b", 5)
    player3 = Player("c", 3)
    player4 = Player("d", 5)
    player5 = Player("e", 5)
    player6 = Player("f", 10)

    scoreboard.add(player1)
    assert len(scoreboard.read()) == 1
    assert scoreboard.read()[0] == player1

    scoreboard.add(player2)
    scoreboard.add(player3)
    scoreboard.add(player4)

    assert len(scoreboard.read()) == 4
    assert scoreboard.read()[1] == player4

    scoreboard.add(player5)
    scoreboard.add(player6)

    assert scoreboard.read()[0] == player6
    assert scoreboard.read()[4] == player2


def insertion_sort(array: list) -> list:
    array = array.copy()

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


def test_insertion_sort():
    array = [5, 4, 3, 2, 1]
    sorted_array = insertion_sort(array)
    assert sorted_array == [1, 2, 3, 4, 5]

    array = [2, 5, 345, 32, 12, 231, 32]
    sorted_array = insertion_sort(array)
    assert sorted_array == [2, 5, 12, 32, 32, 231, 345]


class CaesarCipher:
    def __init__(self, shift: int) -> None:
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord("A"))
            decoder[i] = chr((i - shift) % 26 + ord("A"))

        self._encoder = "".join(encoder)
        self._decoder = "".join(decoder)

    def encode(self, plaintext: str) -> str:
        return self._transform(plaintext, self._encoder)

    def decode(self, ciphertext: str) -> str:
        return self._transform(ciphertext, self._decoder)

    def _transform(self, text: str, code: str) -> str:
        transformed = list(text)
        for i, letter in enumerate(text):
            if not letter.isupper():
                continue
            transformed[i] = code[ord(letter) - ord('A')]
        return "".join(transformed)


def test_CaesarCipher():
    caesar_cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    assert caesar_cipher.encode(message) == "WKH HDJOH LV LQ SODB; PHHW DW MRH'V."
