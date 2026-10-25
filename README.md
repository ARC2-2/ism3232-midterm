# ISM3232 Midterm: Ridgeline Tool Rental

- **Name:** Aaron Contente
- **Version:** Final
- **Date:** October 25, 2026

## What This Program Does
This program handles pricing and quote calculations for Ridgeline Tool Rental. It takes customer rental details, applies the shop's discount and fee rules through functions in `business_rules.py`, and checks whether orders trigger deposits or pickup inspections. Running `main.py` processes eight sample rentals and prints out the full breakdown alongside total revenue and order stats.

## Business Rules
1. The initial rental cost equals the equipment's daily rate multiplied by the number of days rented.
2. Standard rentals receive no discount under 3 days, a 10% discount for 3 through 6 days, and a 20% discount for 7 days or more.
3. Licensed contractors always receive at least a 10% discount, even on rentals lasting fewer than 3 days.
4. A $25 damage waiver fee is added whenever the discounted rental cost falls below $150.
5. Any rental quote totaling $1,000 or more requires a customer deposit.
6. A pickup inspection is required when a rental lasts 5 days or more and has a quote exceeding $800.

## How to Run
zsh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

## How to Test
ruff format .
ruff check .
pytest -v

The test file contains 23 tests.

## Files in This Repository
business_rules.py: all the pricing rules, constants, and calculation functions.
main.py: runs through the sample rentals and prints the final report.
commands.md: the terminal commands and output used while setting up and checking the project.
README.md: project overview, setup steps, and testing instructions.
requirements.txt: packages needed to run and test the project (pytest and ruff).
.gitignore: keeps the virtual environment and cache folders out of Git.
tests/__init__.py: empty file so pytest recognizes the folder and can import the functions.
tests/test_business_rules.py: 23 unit tests checking normal cases and boundaries for every rule.

## AI Use Statement
I did not use AI on this exam.