import unittest
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.card_repository = CardRepository()

    def test_init_attrs_set(self) -> None:
        self.assertEqual(self.card_repository.count, 0)
        self.assertListEqual(self.card_repository.cards, [])

    def test_add__when_card_valid(self) -> None:
        card = MagicCard('Card')
        self.card_repository.add(card)
        self.assertEqual(self.card_repository.count, 1)
        self.assertEqual(self.card_repository.cards, [card])

    def test_add__when_card_invalid__expect_exception(self) -> None:
        card1 = MagicCard('Card')
        card2 = MagicCard('Card')
        self.card_repository.add(card1)
        with self.assertRaises(ValueError) as context:
            self.card_repository.add(card2)

        self.assertEqual(context.exception.args[0], 'Card Card already exists!')

    def test_remove__when_card_valid(self) -> None:
        card = MagicCard('Card')
        self.card_repository.add(card)
        self.card_repository.remove('Card')
        self.assertEqual(self.card_repository.count, 0)
        self.assertEqual(self.card_repository.cards, [])

    def test_remove__when_card_invalid__expect_exception(self) -> None:
        card = MagicCard('Card')
        self.card_repository.add(card)
        with self.assertRaises(ValueError) as context:
            self.card_repository.remove('')

        self.assertEqual(context.exception.args[0], 'Card cannot be an empty string!')

    def test_find_method(self) -> None:
        card = MagicCard('Card')
        self.card_repository.add(card)
        self.assertEqual(self.card_repository.find('Card'), card)


if __name__ == '__main__':
    unittest.main()
