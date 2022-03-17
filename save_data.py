import csv

def adding_data():
    print("[>] Save The Details For Future Use.")
    account_id = input("[>] Account ID:\t")
    account_pass = input("[>] Account Password:\t")
    try:
        with open('credentials.csv', mode="a") as csvfile:
            data_file = csv.writer(csvfile, delimiter=',')
            data_file.writerow([account_id,account_pass])

    finally:
        print(f"\n[>] Your Credentials Have Been Saved!")

adding_data()