class Book:
    """this represents a book in the class."""

    def __init__(self, title, author, isbn):
        """Initialize a Book with a title, author, and ISBN."""
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        """return a formatted string that has the details of the book."""
        return (
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"ISBN: {self.isbn}"
        )

    def get_details(self):
        """return the details as a dictionary."""
        return {    
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn
        }