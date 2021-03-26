import unittest

from ..project.hero import Hero


class HeroTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('steve', 5, 100, 50)

    def test_init_arguments__expect_valid(self) -> None:
        self.assertEqual(self.hero.username, 'steve')
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

    def test_battle__when_enemy_hero_is_self_hero__expect_exception(self) -> None:
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)
        self.assertEqual(context.exception.args[0], 'You cannot fight yourself')

    def test_battle__when_health_is_0_or_lower__expect_exeption(self) -> None:
        enemy_hero = Hero('Whither', 10, 300, 75)
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], 'Your health is lower than or equal to 0. You need to rest')
        self.hero.health = -10
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], 'Your health is lower than or equal to 0. You need to rest')

    def test_battle__when_enemy_health_is_0_or_lower(self) -> None:
        enemy_hero = Hero('Whither', 10, 0, 75)
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], 'You cannot fight Whither. He needs to rest')
        enemy_hero.health = -10
        with self.assertRaises(ValueError) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(context.exception.args[0], 'You cannot fight Whither. He needs to rest')

    def test_battle__when_draw__expect_draw_conditions(self) -> None:
        enemy_hero = Hero('Zombie', 5, 100, 50)
        self.assertEqual(self.hero.battle(enemy_hero), 'Draw')
        self.assertEqual(self.hero.health, -150)
        self.assertEqual(enemy_hero.health, -150)

    def test_battle__when_win__expect_win_conditions(self) -> None:
        enemy_hero = Hero('Zombie', 1, 100, 50)
        self.assertEqual(self.hero.battle(enemy_hero), 'You win')
        self.assertEqual(enemy_hero.health, -150)
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 55)
        self.assertEqual(self.hero.damage, 55)

    def test_battle__when_lose__expect_lose_conditions(self) -> None:
        enemy_hero = Hero('Wither', 5, 300, 50)
        self.assertEqual(self.hero.battle(enemy_hero), 'You lose')
        self.assertEqual(self.hero.health, -150)
        self.assertEqual(enemy_hero.level, 6)
        self.assertEqual(enemy_hero.health, 55)
        self.assertEqual(enemy_hero.damage, 55)

    def test_str_representation_method(self) -> None:
        self.assertEqual(str(self.hero), f"Hero steve: 5 lvl\nHealth: 100\nDamage: 50\n")


if __name__ == '__main__':
    unittest.main()
