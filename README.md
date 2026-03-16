# Python Data Types Foundation Lab

Master Python built-in methods through **12 desi, story-based challenges**! From Guddu ki chai tapri to a Thali combo platter, each problem puts you in a real Indian scenario where you need to use built-in methods of `str`, `int/float`, `list`, and `dict` to get things done.

**Total: 100 points across 12 challenges**

---

## Prerequisites

- [Python](https://www.python.org/) v3.10 or higher
- [Git](https://git-scm.com/)
- A code editor (VS Code recommended)

---

## Getting Started

### 1. Accept the assignment

Click the GitHub Classroom invitation link shared by your instructor. This will create a **personal copy** of this repository under your GitHub account.

### 2. Clone your repository

```bash
git clone <your-repo-url>
cd py-datatypes-foundation
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify everything works

```bash
pytest
```

You should see **all tests failing** — that's expected! Your job is to make them pass.

---

## How to Solve the Challenges

### Step 1 — Open a challenge file

All challenges live in the `src/` folder. Start with `src/01_chai_order.py` and work your way up.

```
src/
├── ch01_chai_order.py         ← Start here
├── ch02_rangoli_maker.py
├── ch03_rickshaw_meter.py
├── ch04_sabzi_mandi.py
├── ch05_train_coach.py
├── ch06_kiryana_store.py
├── ch07_ration_card.py
├── ch08_paan_shop.py
├── ch09_postcard_writer.py
├── ch10_pincode_checker.py
├── ch11_parcel_service.py
└── ch12_thali_combo.py
```

### Step 2 — Read the kahani and rules

Each file has a detailed docstring at the top that explains:
- The **kahani** (story — a real Indian scenario)
- The **rules** your function must follow
- The **parameters** and **return values** with examples

Read it carefully — every edge case and requirement is described there.

### Step 3 — Write your solution

Replace `# Your code here` (and the `pass`) with your implementation:

```python
# Before (in ch01_chai_order.py)
def get_chai_order_length(order):
    # Your code here
    pass

# After (example)
def get_chai_order_length(order):
    if not isinstance(order, str):
        return -1
    return len(order.strip())
```

### Step 4 — Run the test for that challenge

```bash
pytest -v -k "ch01_chai"
```

You can match any part of the filename:

```bash
pytest -k "ch02_rangoli"
pytest -k "ch03_rickshaw"
pytest -k "sabzi"
pytest -k "train_coach"
pytest -k "kiryana"
```

### Step 5 — Fix and repeat

If tests fail, read the error messages — they tell you exactly what was expected vs. what your function returned. Fix your code and run the test again.

### Step 6 — Move to the next challenge

Once all tests pass for a challenge, move on to the next one. They get progressively harder.

### Run all tests at once

```bash
pytest
```

### Watch mode (auto re-run on save)

```bash
ptw -- -v
```

This re-runs tests every time you save a file — very handy while working.

---

## Challenges

| #  | Challenge | File | Concept | Points |
|----|-----------|------|---------|--------|
| 01 | Chai Tapri Order System | `ch01_chai_order.py` | String Basics: `len()`, `strip()`, `upper()`, `lower()`, `in`, indexing | 7 |
| 02 | Rangoli Border Maker | `ch02_rangoli_maker.py` | String Transform: `* n`, `[start:end]`, `split()`, `join()`, `replace()` | 7 |
| 03 | Auto Rickshaw Fare Calculator | `ch03_rickshaw_meter.py` | Number & Math: `int()`, `float()`, `round()`, `abs()`, `math.ceil()` | 8 |
| 04 | Sabzi Mandi Shopping Cart | `ch04_sabzi_mandi.py` | List Basics: `append()`, `pop()`, `insert()`, `in`, `len()`, `+` | 8 |
| 05 | Train Coach Finder | `ch05_train_coach.py` | List Search: list comprehension, `any()`, `all()`, `filter()`, `sorted()` | 8 |
| 06 | Kiryana Store Bill | `ch06_kiryana_store.py` | List Transform: comprehension, `map()`, `sum()`, `sorted()`, `zip()` | 9 |
| 07 | Ration Card Registry | `ch07_ration_card.py` | Dict Basics: `.keys()`, `.values()`, `.items()`, `.get()`, `del` | 9 |
| 08 | Paan Shop Menu | `ch08_paan_shop.py` | Dict Transform: dict comprehension, `.copy()`, `{**d1, **d2}` merge | 8 |
| 09 | Indian Postcard Writer | `ch09_postcard_writer.py` | String Advanced: f-strings, `startswith()`, `endswith()`, `zfill()`, `center()` | 9 |
| 10 | Pincode Type Checker | `ch10_pincode_checker.py` | Type Checking: `isinstance()`, `type()`, `int`, `str`, `bool` | 9 |
| 11 | Dak Ghar Parcel Service | `ch11_parcel_service.py` | JSON & Conversion: `json.loads()`, `json.dumps()`, `str()`, `float()` | 9 |
| 12 | Thali Combo Platter | `ch12_thali_combo.py` | Capstone: all types combined | 9 |

---

## Submitting Your Work

### 1. Check your progress

```bash
pytest
```

### 2. Stage your changes

```bash
git add src/
```

> **Important:** Only add files from `src/`. Do not modify or commit test files.

### 3. Commit your work

```bash
git commit -m "Complete datatypes foundation lab"
```

### 4. Push to GitHub

```bash
git push origin main
```

### 5. Check your grade

After pushing, go to your repository on GitHub:

1. Click the **Actions** tab
2. You'll see a workflow run in progress (or completed)
3. Click on it to see which tests passed and your total score

---

## Tips for Success

- **Docstrings dhyan se padho** — every rule and edge case is described there
- **Try methods in REPL first** — open Python REPL (`python3`) and experiment with `"hello".upper()`, `[1,2,3].pop()`, etc.
- **Python Docs are your best friend** — search "python str strip" or "python list append" for detailed explanations
- **`isinstance()` is your type-checker** — always prefer it over `type(x) ==`
- **`bool` is a subclass of `int`** — always check `isinstance(x, bool)` before `isinstance(x, int)`
- **Return types matter** — check the exact shape of what each function should return
- **Edge cases handle karo** — wrong types, empty strings, empty lists — the docstring tells you what to return for each
- **Use `print()` to debug** — add temporary prints, then remove before submitting
- **Don't modify the test files** — only edit files in `src/`

---

## Concepts Covered

- **String Basics**: `len()`, `strip()`, `upper()`, `lower()`, `in`, indexing
- **String Transform**: `* n`, slicing, `split()`, `join()`, `replace()`
- **Number & Math**: `int()`, `float()`, `round()`, `abs()`, `math.ceil()`, `min()`, `max()`
- **List Basics**: `append()`, `pop()`, `insert()`, `index()`, `in`, `len()`, `+`
- **List Search**: list comprehension, `any()`, `all()`, `sorted()`
- **List Transform**: `map()`, `filter()`, `sum()`, `sorted()`, `zip()`
- **Dict Basics**: `.keys()`, `.values()`, `.items()`, `.get()`, `del`, `in`
- **Dict Transform**: dict comprehension, `.copy()`, `{**d1, **d2}`, `.update()`
- **String Advanced**: f-strings, `startswith()`, `endswith()`, `zfill()`, `center()`, `count()`
- **Type Checking**: `isinstance()`, `type()`, `int`, `str`, `float`, `bool`, `list`, `dict`
- **JSON & Conversion**: `json.loads()`, `json.dumps()`, `str()`, `int()`, `float()`, `list()`
- **Capstone**: combining all data type methods together

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `pytest: command not found` | Run `pip install -r requirements.txt` first |
| All tests fail with `None` | You haven't written your solution yet — that's expected! |
| Tests say `AssertionError: assert None == ...` | Your function is returning `None` (forgot to add logic or `return`) |
| Tests pass locally but fail on GitHub | Make sure you pushed all your changes (`git status` to check) |
| `ModuleNotFoundError: No module named 'src'` | Run `pytest` from the project root folder |

---

Good luck! Aur haan, methods sikhte sikhte chai aur samosa lena mat bhoolna! ☕🥪
