import csv
import os

def ensure_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")

def append_row(filename, row, header=None):
    ensure_data_folder()
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if header and not file_exists:
            writer.writerow(header)
        writer.writerow(row)
