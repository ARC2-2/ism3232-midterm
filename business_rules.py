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


def total_quoted(rentals: list) -> float:
    """Returns the sum of quotes for all rentals in the list."""
    total = 0.0
    for rental in rentals:
        total += calculate_quote(
            rental["daily_rate"],
            rental["days"],
            rental.get("contractor", False),
        )
    return total


def largest_rental(rentals: list) -> str:
    """Returns the customer of the rental with the largest quote."""
    if not rentals:
        return ""
    largest_customer = ""
    largest_amount = -1.0
    for rental in rentals:
        quote = calculate_quote(
            rental["daily_rate"],
            rental["days"],
            rental.get("contractor", False),
        )
        if quote > largest_amount:
            largest_amount = quote
            largest_customer = rental["customer"]
    return largest_customer


def format_rental_line(
    customer: str, quote: float, deposit: bool, inspection: bool
) -> str:
    """Returns one formatted line for the rental report."""
    deposit_str = "yes" if deposit else "no"
    inspection_str = "yes" if inspection else "no"
    return f"{customer}: ${quote:.2f} | deposit: {deposit_str} | inspection: {inspection_str}"
