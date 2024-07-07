from book_manager.book_manager import BookManager
from book_manager.utils import print_welcome_message, get_user_input

def main():
    print_welcome_message()
    manager = BookManager()

    while True:
        print("\n1. Add Book")
        print("2. List Books")
        print("3. Find Book")
        print("4. Exit")
        choice = get_user_input("Choose an option: ")

        if choice == "1":
            title = get_user_input("Enter the book title: ")
            author = get_user_input("Enter the author: ")
            year = get_user_input("Enter the publication year: ")
            manager.add_book(title, author, year)
            print("Book added successfully!")
        elif choice == "2":
            manager.list_books()
        elif choice == "3":
            title = get_user_input("Enter the book title to find: ")
            book = manager.find_book(title)
            if book:
                print(book)
            else:
                print("Book not found.")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()