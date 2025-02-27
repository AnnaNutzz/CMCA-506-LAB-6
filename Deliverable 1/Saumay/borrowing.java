package bookborrowing;

import java.util.ArrayList;
import java.util.List;

// User class to represent library users
class User {
    private String name;
    private String id;
    private String contact;

    public User(String name, String id, String contact) {
        this.name = name;
        this.id = id;
        this.contact = contact;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "User{name='" + name + "', id='" + id + "', contact='" + contact + "'}";
    }
}

// Book class to represent books in the catalog
class Book {
    private String title;
    private String author;
    private String isbn;
    private boolean isAvailable;

    public Book(String title, String author, String isbn) {
        this.title = title;
        this.author = author;
        this.isbn = isbn;
        this.isAvailable = true; // Default to available
    }

    public String getIsbn() {
        return isbn;
    }

    public String getTitle() {
        return title;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    @Override
    public String toString() {
        return "Book{title='" + title + "', author='" + author + "', isbn='" + isbn + "', available=" + isAvailable + "}";
    }
}

// LibraryManagement class to manage users and books
class LibraryManagement {
    private List<User> users;
    private List<Book> books;

    public LibraryManagement() {
        this.users = new ArrayList<>();
        this.books = new ArrayList<>();
    }

    public void registerUser(String name, String id, String contact) {
        User user = new User(name, id, contact);
        users.add(user);
        System.out.println("User registered: " + user);
    }

    public void addBook(String title, String author, String isbn) {
        Book book = new Book(title, author, isbn);
        books.add(book);
        System.out.println("Book added: " + book);
    }

    public void searchBookByTitle(String title) {
        for (Book book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                System.out.println("Found: " + book);
                return;
            }
        }
        System.out.println("Book with title '" + title + "' not found.");
    }
}

// Main class to test Deliverable 1
public class borrowing {
    public static void main(String[] args) {
        LibraryManagement library = new LibraryManagement();

        // Register users
        library.registerUser("Alice Smith", "U001", "alice@example.com");
        library.registerUser("Bob Jones", "U002", "bob@example.com");

        // Add books to catalog
        library.addBook("The Great Gatsby", "F. Scott Fitzgerald", "1234567890");
        library.addBook("1984", "George Orwell", "0987654321");

        // Search for a book
        library.searchBookByTitle("1984");
        library.searchBookByTitle("Harry Potter");
    }
}



