# Terminal Record: Ridgeline Tool Rental
## 1. Building the project
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
activate
pip install pytest ruff
pip freeze > requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
echo '*.pyc' > .gitignore
mkdir tests
cd tests
touch __init__.py
cd ..
touch test_business_rules.py
touch main.py
touch commands. md
touch README.md
git init
git add .
git commit -m "created all the folders and files for part 1"
git branch -M main
git remote add origin [https://github.com/ARC2-2/ism3232-midterm.git](https://github.com/ARC2-2/ism3232-midterm.git)
git push -u origin main

## 2. The virtual environment
(.venv) ➜  ism3232-midterm git:(main) ✗ which python3
/Users/aaron/VS Code/ism3232-midterm/.venv/bin/python3

The output shows that the virtual environment is active because the path points to the python3 file in the project rather than the system Python path.

## 3. The project structure
(.venv) ➜  ism3232-midterm git:(main) ✗ tree -L 2
.
├── __pycache__
│   └── business_rules.cpython-313.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

.venv is excluded from the GitHub repository because it holds thousands of machine-specific files that only belong on my local computer.

## 4. Every function and test
(.venv) ➜  ism3232-midterm git:(main) ✗ rg 'def '
business_rules.py
12:def calculate_rental_cost(daily_rate: float, days: int) -> float:
17:def get_rental_discount(days: int, contractor: bool = False) -> float:
26:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
36:def requires_deposit(quote: float) -> bool:
41:def needs_inspection(days: int, quote: float) -> bool:
46:def total_quoted(rentals: list) -> float:
58:def largest_rental(rentals: list) -> str:
76:def format_rental_line(

tests/test_business_rules.py
13:def test_calculate_rental_cost():
17:def test_discount_under_three_days_non_contractor():
21:def test_discount_boundary_three_days():
25:def test_discount_boundary_six_days():
29:def test_discount_boundary_seven_days():
33:def test_discount_contractor_under_three_days():
37:def test_quote_with_damage_waiver_under_threshold():
42:def test_quote_boundary_at_damage_waiver_threshold():
48:def test_deposit_under_threshold():
52:def test_deposit_boundary_at_limit():
56:def test_deposit_over_threshold():
60:def test_inspection_both_conditions_met():
64:def test_inspection_days_boundary_under():
69:def test_inspection_days_boundary_at_limit():
74:def test_inspection_quote_boundary_at_limit():
79:def test_inspection_quote_boundary_over_limit():
84:def test_format_rental_line_all_no():
89:def test_format_rental_line_all_yes():
94:def test_total_quoted_short_list():
103:def test_largest_rental_empty_list():
107:def test_largest_rental_single_order():
112:def test_largest_rental_preserves_first_on_tie():
120:def test_calculate_quote_contractor_changes_total():

Business_rules.py defines 8 functions, and tests/test_business_rules.py defines 23 tests.

## 5. Which files print
(.venv) ➜  ism3232-midterm git:(main) ✗ rg -l 'print'
main.py
commands.md

Only main.py prints because it handles console reporting, while business_rules.py contains only business logic that returns values.

## 6. The commit history
(.venv) ➜  ism3232-midterm git:(main) ✗ git log --oneline
46f9912 (HEAD -> main, origin/main) built main report and verified output
4bff795 added aggregator functions, line formatter, and complete tests
2cf95ed added deposit and inspection functions with boundary tests
e6eb6f2 added first three pricing functions and initial tests
cdf59af created all the folders and files for part 1

