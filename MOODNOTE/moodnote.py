import datetime

DATA_FILE = "mood_data.txt"

def save_mood():
    mood = input("How are you feeling today? ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(DATA_FILE, "a", encoding="utf-8") as file:
        file.write(f"{date} - {mood}\n")
    print("Mood saved!")

def view_history():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            print("\nMood History:")
            print(content if content else "No entries yet.")
    except FileNotFoundError:
        print("Mood history file not found. Make your first entry!")

def main():
    print("📝 Welcome to Mood Journal!")
    while True:
        print("\nChoose an action:")
        print("1. Record today's mood")
        print("2. View mood history")
        print("3. Exit")

        choice = input("Your choice: ")

        if choice == "1":
            save_mood()
        elif choice == "2":
            view_history()
        elif choice == "3":
            print("Goodbye! Take care ❤️")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

