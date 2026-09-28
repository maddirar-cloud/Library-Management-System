# Library Management System

## Project Description

The Library Management System is a Python program that replicates and manages the inventory of a library.

You can add books to the library, view all books, search for a book by title or author, and exit the program.

## Files
 **book.py**

Contains the `Book` class used to represent individual books.

Each `Book` object contains:

1. Title
2. Author
3. ISBN

The class includes methods for displaying and retrieving book information.

### `library_manager.py`

Contains the main program to manage said library.

The main functions are:

1. `add_book(library)` - Prompts the user for book information and adds a new `Book` object to the library.
2. `list_books(library)` - Displays all books currently stored in the library.
3. `find_book(library, query)` - Searches for a book by its title or author.
4. `main()` - Runs the menu and controls the program.

## How to Run

1. Make sure Python is installed on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python library_manager.py
```

5. Follow the menu instructions in the terminal.

## Program Features

1. Add a new book
2. List all books
3. Search for a book by title or author
4. Store books as `Book` objects
5. Display book information using the `__str__` method
6. Retrieve book information using the `get_details` method
7. Uses separate Python modules for better organization
8. Uses functions and parameters to manage the library


## Screencast

Screencast link: https://www.loom.com/share/8652815e9c97452f846636dc8c2c6898

