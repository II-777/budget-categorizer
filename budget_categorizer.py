#!/usr/bin/python3
import pandas as pd


def update_tags(row):
    # Adjust the keyword mapping below according to your preference:
    keyword_mapping = {
        # hosting
        "NAME-CHEAP.COM": '#hosting',
        # groceries
        'HONG KONG EXPRESS': '#groceries',
        # gas
        'SHELL': '#transportation',
        # charity
        "SERHIY.PRYTULA": '#charity',
        # ignore
        "Internet Banking": '#ignore',
    }

    matched_keyword = None

    for keyword in keyword_mapping.keys():
        if keyword in row['Description']:
            matched_keyword = keyword
            break

    tag = keyword_mapping.get(matched_keyword, '#other')

    # Income / Expense Tagging
    if pd.notna(row['Expense']) and row['Expense'] != 0:
        tag += '; #expense'

    if pd.notna(row['Income']) and row['Income'] != 0:
        tag += '; #income'

    return tag


def display_csv_contents(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=';', names=[
                         'Date', 'Description', 'Expense', 'Income'])
        df['Tag'] = df.apply(update_tags, axis=1)
        df.fillna(0, inplace=True)
        df.loc[df['Expense'] > 0, 'Expense'] *= -1
        df = df[~df['Tag'].str.contains('#ignore')]

        # Set the delimiter for the output (semicolon in this example)
        delimiter = ';'

        # Print the contents with delimiter
        for index, row in df.iterrows():
            # Ensure Description column is quoted
            description = f'"{row["Description"]}"'
            print(delimiter.join([row['Date'], description, str(
                row['Expense']), str(row['Income']), row['Tag']]))

    except FileNotFoundError:
        print(f"[-] Error: {file_path} not found")
    except pd.errors.EmptyDataError:
        print(f"[-] Error: {file_path} is empty.")
    except pd.errors.ParserError:
        print(f"[-] Error: {file_path} unable to parse.")


file_path = 'transactions.csv'
display_csv_contents(file_path)
