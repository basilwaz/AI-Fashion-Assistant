"""Small, repeatable sample catalog for the first prototype."""

from decimal import Decimal, InvalidOperation


CATALOG = (
    {"name": "Campus casual", "style": "casual", "occasion": "everyday",
     "items": [("T-shirt", "Demo Basics", 1800), ("Jeans", "Demo Denim", 3500),
               ("Sneakers", "Demo Shoes", 4500)]},
    {"name": "Simple activewear", "style": "sporty", "occasion": "gym",
     "items": [("Training shirt", "Demo Active", 2000),
               ("Joggers", "Demo Active", 3000), ("Trainers", "Demo Shoes", 5000)]},
    {"name": "Class presentation", "style": "smart", "occasion": "presentation",
     "items": [("Polo", "Demo Basics", 2800), ("Chinos", "Demo Denim", 4200),
               ("Loafers", "Demo Shoes", 5500)]},
    {"name": "Budget casual", "style": "casual", "occasion": "everyday",
     "items": [("Plain shirt", "Demo Basics", 1200),
               ("Casual trousers", "Demo Denim", 2500), ("Canvas shoes", "Demo Shoes", 3000)]},
)


def parse_budget(value):
    """Return whole cents. Reject invalid values before filtering."""
    try:
        amount = Decimal(str(value))
    except InvalidOperation as error:
        raise ValueError("Enter a positive budget, such as 100.") from error
    if not amount.is_finite() or not Decimal("0") < amount <= Decimal("100000"):
        raise ValueError("Budget must be between $0.01 and $100,000.")
    if amount.as_tuple().exponent < -2:
        raise ValueError("Use no more than two decimal places.")
    return int(amount * 100)


def total_cents(outfit):
    return sum(price for _, _, price in outfit["items"])


def recommend(budget, style="any", occasion="any"):
    limit = parse_budget(budget)
    matches = [outfit for outfit in CATALOG
               if style in ("any", outfit["style"])
               and occasion in ("any", outfit["occasion"])
               and total_cents(outfit) <= limit]
    return [{"name": outfit["name"], "total_cents": total_cents(outfit),
             "items": [{"name": name, "brand": brand, "price_cents": price}
                       for name, brand, price in outfit["items"]]}
            for outfit in sorted(matches, key=total_cents)]
