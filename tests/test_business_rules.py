from business_rules import (
    calculate_quote,
    calculate_rental_cost,
    get_rental_discount,
    needs_inspection,
    requires_deposit,
)


def test_calculate_rental_cost():
    assert round(calculate_rental_cost(60.0, 2), 2) == 120.00


def test_discount_under_three_days_non_contractor():
    assert get_rental_discount(2, contractor=False) == 0.0


def test_discount_boundary_three_days():
    assert get_rental_discount(3, contractor=False) == 0.10


def test_discount_boundary_six_days():
    assert get_rental_discount(6, contractor=False) == 0.10


def test_discount_boundary_seven_days():
    assert get_rental_discount(7, contractor=False) == 0.20


def test_discount_contractor_under_three_days():
    assert get_rental_discount(2, contractor=True) == 0.10


def test_quote_with_damage_waiver_under_threshold():
    # 60 * 2 = 120. Under 150, so add 25 waiver fee -> 145.00
    assert round(calculate_quote(60.0, 2, contractor=False), 2) == 145.00


def test_quote_boundary_at_damage_waiver_threshold():
    # 50 * 3 days = 150. 10% discount = 135. Under 150 -> 160.00
    # 150.00 flat with no discount: 75 * 2 days = 150. Exactly at 150, no waiver added
    assert round(calculate_quote(75.0, 2, contractor=False), 2) == 150.00


def test_deposit_under_threshold():
    assert requires_deposit(999.99) is False


def test_deposit_boundary_at_limit():
    assert requires_deposit(1000.00) is True


def test_deposit_over_threshold():
    assert requires_deposit(1000.01) is True


def test_inspection_both_conditions_met():
    assert needs_inspection(5, 800.01) is True


def test_inspection_days_boundary_under():
    # Hold quote over threshold so days decides
    assert needs_inspection(4, 900.00) is False


def test_inspection_days_boundary_at_limit():
    # Hold quote over threshold
    assert needs_inspection(5, 900.00) is True


def test_inspection_quote_boundary_at_limit():
    # Hold days valid; exactly 800.00 is not 'over' 800
    assert needs_inspection(6, 800.00) is False


def test_inspection_quote_boundary_over_limit():
    # Hold days valid; one cent above 800 triggers inspection
    assert needs_inspection(6, 800.01) is True
