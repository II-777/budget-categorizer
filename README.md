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

3. Update the `transactions.csv` file with your financial data. Make sure to follow the provided format (`Date; Description; Expense; Income`) and include all relevant transactions.

4. Run the Python script to analyze the transactions and generate tags. Redirect the output to a file (e.g., `out.csv`).
   ```bash
   ./budget-categorizer.py > out.csv
   ```

5. Review the tagged transactions saved in the `out.csv` file.

## Customization

You can customize the keyword mapping in the `update_tags()` function of the Python script (`budget_categorizer.py`) to better suit your transaction descriptions and categorization preferences.

## Contributors

- [ii-777](https://github.com/ii-777)

## License

This project is licensed under the MIT License.
