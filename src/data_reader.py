import pandas as pd


def read_csv_files(csv_file_path: str) -> list[dict]:
    '''Считывает финансовые операции из CSV'''
    try:
        transactions_file = pd.read_csv(csv_file_path, sep=';')
        result = []
        for index, row in transactions_file.iterrows():
            result.append(dict(row))
        return result

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


# result_1 = read_csv_files("../data/transactions.csv")
# print(result_1)

def read_excel_files(excel_file_path: str) -> list[dict]:
    '''Считывает финансовые операции из Excel'''
    try:
        transactions_file = pd.read_excel(excel_file_path)
        result = []
        for index, row in transactions_file.iterrows():
            result.append(dict(row))
        return result

    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []

# result_2 = read_excel_files("../data/transactions_excel.xlsx")
# print(result_2)
