from book import Book


def add_book(library):
    """take in inputs to identify the book details."""
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")

    new_book = Book(title, author, isbn)
    library.append(new_book)

    print("Book added successfully!")


def list_books(library):
    """show current book details."""
    if not library:
        print("The library is empty.")
        return

    print("\nLibrary Books:")
    for book in library:
        print(book)


def find_book(library, query):
    """find book that matches the details."""
    for book in library:
        if query.lower() in book.title.lower():
            return book
        if query.lower() in book.author.lower():
            return book

    return None


def main():
    """Run the library management program."""
    my_library = []

    while True:
        print("\nLibrary Management System")
        print("1. Add a new book")
        print("2. List all books")
        print("3. Find a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(my_library)

        elif choice == "2":
            list_books(my_library)

        elif choice == "3":
            query = input("Enter a title or author to search for: ")
            found_book = find_book(my_library, query)

            if found_book:
                print("Book found:")
                print(found_book)
            else:
                print("No matching book was found.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()