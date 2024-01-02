import pandas as pd

def csv_to_xlsx(csv_file, xlsx_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Write to an Excel file
    df.to_excel(xlsx_file, index=False)

# Example usage
csv_file = r'INPUT'  # Replace with your CSV file path
xlsx_file = r'OUTPUT'       # Output Excel file path
csv_to_xlsx(csv_file, xlsx_file)
