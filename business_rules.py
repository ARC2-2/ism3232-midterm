MID_TIER_DAYS = 3
TOP_TIER_DAYS = 7
MID_TIER_DISCOUNT = 0.10
TOP_TIER_DISCOUNT = 0.20
DAMAGE_WAIVER_FEE = 25.00
DAMAGE_WAIVER_THRESHOLD = 150.00
DEPOSIT_THRESHOLD = 1000.00
INSPECTION_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.00


def calculate_rental_cost(daily_rate: float, days: int) -> float:
    """Returns the rental cost before any discount."""
    return daily_rate * days


def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Returns the discount rate as a decimal."""
    if days >= TOP_TIER_DAYS:
        return TOP_TIER_DISCOUNT
    if days >= MID_TIER_DAYS or contractor:
        return MID_TIER_DISCOUNT
    return 0.0


def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Returns the quote including the damage waiver fee."""
    cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    discounted_cost = cost * (1.0 - discount)
    if discounted_cost < DAMAGE_WAIVER_THRESHOLD:
        return discounted_cost + DAMAGE_WAIVER_FEE
    return discounted_cost


def requires_deposit(quote: float) -> bool:
    """Returns true when the quote requires a deposit."""
    return quote >= DEPOSIT_THRESHOLD


def needs_inspection(days: int, quote: float) -> bool:
    """Returns true when the rental needs a pickup inspection."""
    return days >= INSPECTION_DAYS and quote > INSPECTION_QUOTE_THRESHOLD
