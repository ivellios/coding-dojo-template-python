import unittest
from potter import *

class TestPotter(unittest.TestCase):

    def test_basket_is_empty(self):
        empty_basket = Basket()
        self.assertEquals(empty_basket.total(), 0)

    def test_can_add_item_to_basket(self):
        basket = Basket()
        basket.add(BOOK_ONE)

        total = basket.total()

        self.assertEquals(total, DEFAULT_PRICE)

    def test_can_add_two_identical_books_to_basket(self):
        basket = Basket.create()
        basket.add(BOOK_ONE)
        basket.add(BOOK_ONE)

        total = basket.total()

        self.assertEquals(total, DEFAULT_PRICE * 2)

    def test_includes_discount_for_two_different_books_in_basket(self):
        basket = Basket.create(BOOK_ONE, BOOK_TWO)

        total = basket.total()

        self.assertAlmostEquals(total, DEFAULT_PRICE * 2 * 0.95)

    def test_includes_discount_for_two_different_books_in_basket_with_duplicates(self):
        basket = Basket.create(BOOK_ONE, BOOK_ONE, BOOK_TWO)

        total = basket.total()

        self.assertAlmostEquals(total, DEFAULT_PRICE * 2 * 0.95 + DEFAULT_PRICE)

    def test_includes_discount_for_three_different_books_in_basket(self):
        basket = Basket.create(BOOK_ONE, BOOK_TWO, BOOK_TWO, BOOK_THREE)

        total = basket.total()

        self.assertAlmostEquals(total, DEFAULT_PRICE * 3 * 0.9 + DEFAULT_PRICE)

    def test_includes_discount_for_four_different_books_in_basket(self):
        basket = Basket.create(
            BOOK_ONE,
            BOOK_TWO, BOOK_TWO,
            BOOK_THREE, BOOK_THREE,
            BOOK_FOUR)

        total = basket.total()

        self.assertAlmostEquals(total, DEFAULT_PRICE * 4 * 0.8 + DEFAULT_PRICE * 2 * 0.95)

    def test_includes_discount_for_five_different_books_in_basket(self):
        basket = Basket.create(
            BOOK_ONE,
            BOOK_TWO, BOOK_TWO,
            BOOK_THREE, BOOK_THREE,
            BOOK_FOUR,
            BOOK_FIVE, BOOK_FIVE, BOOK_FIVE)

        total = basket.total()

        self.assertAlmostEquals(total, DEFAULT_PRICE * 5 * 0.75 + DEFAULT_PRICE * 3 * 0.9 + DEFAULT_PRICE)

    # test price of one book

if __name__ == '__main__':
    unittest.main()
