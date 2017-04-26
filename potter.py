
DEFAULT_PRICE = 8

class Book():
    def __init__(self, price=DEFAULT_PRICE):
        self.price = price

BOOK_ONE = Book()
BOOK_TWO = Book()
BOOK_THREE = Book()
BOOK_FOUR = Book()
BOOK_FIVE = Book()

DISCOUNTS = {
    0: 0,
    1: 0,
    2: 0.05,
    3: 0.1,
    4: 0.2,
    5: 0.25
}

class Basket():
    def __init__(self):
        self._books = {}

    @staticmethod
    def create(*books):
        basket = Basket()
        for book in books:
            basket.add(book)
        return basket

    def total(self):
        return BooksCheckout(self._books).total()

    def add(self, book):
        if book not in self._books:
            self._books[book] = 0

        self._books[book] += 1


class BooksCheckout():
    def __init__(self, books):
        self._books = books.copy()

    @staticmethod
    def price_multiplier(unique_count):
        return 1 - DISCOUNTS[unique_count]

    def total(self):
        total = 0
        while self.get_unique_count() > 0:
            total += self.discounted_total()
        return total

    def discounted_total(self):
        unique_count = self.get_unique_count()
        subtotal = self.get_subtotal()
        self.pop_unique_books()
        return subtotal * BooksCheckout.price_multiplier(unique_count)

    def pop_unique_books(self):
        for book in self._books.keys():
            if self._books[book] > 0:
                self._books[book] -= 1

    def get_subtotal(self):
        subtotal = 0
        for book in self._books.keys():
            if self._books[book] > 0:
                subtotal += book.price
        return subtotal

    def get_unique_count(self):
        unique_count = 0
        for book in self._books.keys():
            if self._books[book] > 0:
                unique_count += 1
        return unique_count
