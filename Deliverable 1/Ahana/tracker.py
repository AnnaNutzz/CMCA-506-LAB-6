from dataclasses import dataclass
from typing import List
import uuid

# Book class to represent a tracked book
@dataclass
class Book:
    title: str
    author: str
    book_id: str = str(uuid.uuid4())  # Unique ID generated automatically
    status: str = "on shelf"  # Default status

    def __str__(self):
        return f"Book{{title='{self.title}', author='{self.author}', book_id='{self.book_id}', status='{self.status}'}}"

# BookTracking class to manage tracked books
class BookTracking:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, title: str, author: str) -> None:
        book = Book(title, author)
        self.books.append(book)
        print(f"Book added: {book}")

    def get_book_status(self, book_id: str) -> None:
        for book in self.books:
            if book.book_id == book_id:
                print(f"Status of book {book_id}: {book}")
                return
        print(f"Book with ID '{book_id}' not found.")

    def display_all_books(self) -> None:
        if not self.books:
            print("No books in the tracking system.")
        else:
            print("Tracked Books:")
            for book in self.books:
                print(book)

# Main execution to test Deliverable 1
if __name__ == "__main__":
    tracker = BookTracking()

    # Add books
    tracker.add_book("The Catcher in the Rye", "J.D. Salinger")
    tracker.add_book("Brave New World", "Aldous Huxley")
    print("")

    # Display all books
    tracker.display_all_books()
    print("")

    # Check status of a book (using the ID of the first book as an example)
    first_book_id = tracker.books[0].book_id
    tracker.get_book_status(first_book_id)
