import csv

def reading_data():
    print("[>] Reading Previous Account Credentials.")
    account_id = ''
    account_pass = ''
    try:
        with open('credentials.csv', mode="r") as csvfile:
            data_file = csv.reader(csvfile, delimiter=',')
            for lines in data_file:
                print(lines)
    finally:
        print(f"\n[>] Your Credentials Have Been Saved!")

reading_data()
