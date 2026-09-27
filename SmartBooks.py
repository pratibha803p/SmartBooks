import json
import os

DATA_FILE = "smartbook_data.json"

BOOKS = [

    {
        "id": 1,
        "title": "Harry Potter And The Sorcerer's Stone",
        "author": "J.K. Rowling",
        "category": "Fiction / Fantasy",
        "useful_for": "Imagination And English skills"
    },
    {
        "id": 2,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Inspiration",
        "useful_for": "Motivation And Life Goals"
    },
    {
        "id": 3,
        "title": "Wings Of Fire",
        "author": "A.P.J. Abdul Kalam",
        "category": "Autobiography",
        "useful_for": "Inspiration And Career Growth"
    },
    {
        "id": 4,
        "title": "The Diary Of Young Girl",
        "author": "Anne Frank",
        "category": "History / Biography",
        "useful_for": "Understanding History And Emotion"
    },
    {
        "id": 6,
        "title": "Head Held High",
        "author": "Vishwas Nangre Patil",
        "category": "Autobiography / Inspirational And Motivational",
        "useful_for": "UPSC and Civil Services Aspirants"
    }
]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE,"r") as file:
            return json.load(file)
    return {"users": {}}

def save_data(data):
    with open(DATA_FILE,"w") as file:
        json.dump(data, file, indent=4)

def create_profile(data):
    print("\n--- CREATE PROFILE ---")
    username = input("Enter username: ").strip()

    if username in data["users"]:
        print("Username already exists!")
        return None

    password = input("Enter Password: ").strip()

    data["users"][username] = {  # FIXED: was data["user"]
        "password": password,
        "favourites": []
        }
    save_data(data)
    print("Profile created successfully!")  # FIXED: spelling
    return username

def login(data):
    print("\n--- LOGIN ---")  # FIXED: was /n instead of \n
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in data["users"] and data["users"][username]["password"] == password:
        print(f"\n Welcome back, {username}!")
        return username
    print("Invalid username or password.")
    return None

def show_all_books():
    print("\n--- ALL BOOKS CATALOGUE ---")
    for book in BOOKS:
        print(f"{book['id']}.  {book['title']} by {book['author']} [{book['category']}]")

def search_book():
    print("\n--- SEARCH BOOK ---")
    query = input("Enter book title author: ").lower()
    found = False

    for book in BOOKS:
        if query in book['title'].lower() or query in book['author'].lower():
            print(f" {book['title']} - {book['author']} ({book['category']})")
            print(f"   Useful for: {book['useful_for']}")
            found = True
            
    if not found:
        print("No matching book found.")


def add_favourite(data, username):
    show_all_books()
    try:
        book_id = int(input("\nEnter book number to add to favourites: "))
        # FIXED: Check if book_id exists in BOOKS instead of using len(BOOKS)
        valid_ids = [book['id'] for book in BOOKS]
        if book_id in valid_ids:
            if book_id not in data["users"][username]["favourites"]:
                data["users"][username]["favourites"].append(book_id)  # FIXED: indentation
                save_data(data)
                print("Added to favourites!")
            else:
                print("Already in your favourites!")
        else:
            print("Invalid book number.")

    except ValueError:
        print("Please enter a valid number.")

def view_favourites(data, username):
    print("\n--- YOUR FAVOURITE BOOKS ---")
    favs = data["users"][username]["favourites"]

    if not favs:
        print("No favourites added yet.")

    else:
        for book_id in favs:
            for book in BOOKS:
                if book["id"] == book_id:
                    print(f"   {book['title']} by {book['author']}")

def user_menu(data, username):
    while True:
        print(f"\n=============================")
        print(f"    SMARTBOOK MENU  ({username})")
        print(f"=============================")
        print("1. VIEW ALL BOOKS")
        print("2. Search Book")
        print("3. Add to Favourites")
        print("4. View Favourites")
        print("5. Logout")

        choice = input("Enter choice(1-5): ").strip()

        if choice == "1":
            show_all_books()
        elif choice == "2":
            search_book()
        elif choice == "3":
            add_favourite(data, username)
        elif choice == "4":
            view_favourites(data, username)  # FIXED: was view_favourite
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid option. Try again.")

def main():
    data = load_data()

    while True:
        print("\n=============================")
        print("   WELCOME TO SMARTBOOK")
        print("=============================")
        print("1. Login")
        print("2. Create New Profile")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            username = login(data)
            if username:
                user_menu(data, username)
        elif choice == "2":
            username = create_profile(data)
            if username:
                user_menu(data, username)
        elif choice == "3":
            print ("Goodbye! ")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

