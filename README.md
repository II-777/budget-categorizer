# Budget Categorizer

This repository contains a Python script (`budget_categorizer.py`) for financial transactions classification and tagging, along with an Excel template (`budget-template.xlsx`) for organizing your personal budget. The script helps categorize expenses and incomes based on predefined keywords and generates tags accordingly.

## Features

- **Automatic Tagging**: The script categorizes transactions based on keywords specified in the `update_tags()` function. You can customize these keywords to suit your preferences.
- **Expense/Income Differentiation**: Transactions are tagged with `#expense` or `#income` based on their nature.
- **Excel Template**: The Excel template (`budget-template.xlsx`) provides a structured format for tracking and visualizaton of transaction data.

## Usage

### Prerequisites

- Python 3 installed on your system
- pandas library installed (`pip install pandas`)

### Instructions

1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/personal-budget-tracker.git
   ```

2. Navigate to the repository directory.
   ```bash
   cd personal-budget-tracker
   ```

3. Save transactions from your bank account as `transactions.csv`. Make sure to follow the provided format (`Date; Description; Expense; Income`).

4. Ajust the `keyword_mapping` dictionary in the `budget-categorizer.py` according to your preference.

5. Run the Python script to analyze the transactions and generate tags. Redirect the output to a file (e.g., `out.csv`).
   ```bash
   ./budget-categorizer.py > out.csv
   ```

6. Copy the unique category names from `out.csv` into the `budget-template.xls`
   
8. Copy the tagged transactions saved in the `out.csv` file into the `budget-template.xlsx`.

## Customization

You can customize the keyword mapping in the `update_tags()` function of the Python script (`budget_categorizer.py`) to better suit your transaction descriptions and categorization preferences.

## Contributors

- [ii-777](https://github.com/ii-777)

## License

This project is licensed under the MIT License.
