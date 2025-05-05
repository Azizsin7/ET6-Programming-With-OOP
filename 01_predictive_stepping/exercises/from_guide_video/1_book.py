class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1
    
    def read_pages(self, num_pages):
        self.current_page += num_pages
        if self.current_page > self.pages:
            self.current_page = self.pages

# Create two book instances
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("1984", "George Orwell", 328)

# Q1: What would print here? Try to predict before running.
print(f"book1: {book1.title} by {book1.author}, page {book1.current_page}/{book1.pages}")
print(f"book2: {book2.title} by {book2.author}, page {book2.current_page}/{book2.pages}")

# Read 50 pages in book1
book1.read_pages(50)

# Q2: What is book1's current_page now? _____
assert book1.current_page == 51, "book1 should be on page 51"

# Q3: What is book2's current_page now? _____
assert book2.current_page == 1, "Changing book1 should not affect book2"

# Create a third book
book3 = book1  # What happens here? Are we creating a new instance?

# Q4: What will book3.title be? _____
assert book3.title == "The Hobbit", "book3 should have the same title as book1"

# Read 25 more pages in book3
book3.read_pages(25)

# Q5: What is book1's current_page now? Why? _____
assert book1.current_page == 76, "book1's page should have increased because book3 is the same object"

# Q6: If you change book1.title to "The Hobbit (Extended)", what will book3.title be? _____
book1.title = "The Hobbit (Extended)"
assert book3.title == "The Hobbit (Extended)", "book3.title should match book1.title"

# Bonus question: How would you create a true copy of book1 that doesn't share references?
# One way is:
# import copy
# book4 = copy.copy(book1)
