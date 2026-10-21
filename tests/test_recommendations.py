import unittest

from src.recommendations import parse_budget, recommend


class RecommendationTests(unittest.TestCase):
    def test_budget_boundary_and_sort_order(self):
        outfits = recommend("98")
        self.assertEqual([row["total_cents"] for row in outfits], [6700, 9800])
        self.assertEqual(len(recommend("97.99")), 1)

    def test_style_and_occasion_together(self):
        self.assertEqual(recommend("200", "sporty", "gym")[0]["name"], "Simple activewear")
        self.assertEqual(recommend("200", "sporty", "presentation"), [])

    def test_item_prices_add_up(self):
        for outfit in recommend("200"):
            self.assertEqual(sum(item["price_cents"] for item in outfit["items"]),
                             outfit["total_cents"])

    def test_no_matches_for_small_budget(self):
        self.assertEqual(recommend("10"), [])

    def test_invalid_budget(self):
        for value in ("", "abc", "NaN", "Infinity", "-1", "0", "100001", "9.999"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_budget(value)

    def test_decimal_cents_are_exact(self):
        self.assertEqual(parse_budget("67.01"), 6701)

    def test_unknown_style_has_no_matches(self):
        self.assertEqual(recommend("200", "unknown"), [])
