import datetime

def write_entry():
    entry = input("Write your diary entry: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as f:
        f.write(f"\n[{date}]\n{entry}\n")

def read_entries():
    print("\n--- Your Diary Entries ---\n")
    try:
        with open("diary.txt", "r") as f:
            print(f.read())

    except FileNotFoundError:
        print("No diary entries found.")

def main():
    while True:
        print("\n1. Write Entry")
        print("2. Read Entries")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()
















