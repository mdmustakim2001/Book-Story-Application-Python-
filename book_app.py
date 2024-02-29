class Book:
    def __init__(self, title, author, summary):
        self.title = title
        self.author = author
        self.summary = summary

class BookStoryApp:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, summary):
        book = Book(title, author, summary)
        self.books.append(book)

    def browse_books(self):
        print("Available Books:")
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.title} by {book.author}")

    def read_summary(self, book_index):
        if 1 <= book_index <= len(self.books):
            book = self.books[book_index - 1]
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print("Summary:")
            print(book.summary)
        else:
            print("Invalid book index.")

def main():
    app = BookStoryApp()

    # Adding sample books
    app.add_book("The Very Hungry Caterpillar", "Eric Carle", "A classic children's picture book about a caterpillar's journey to transformation.")
    app.add_book("Where the Wild Things Are", "Maurice Sendak", "A story about a young boy named Max who sails to an island inhabited by imaginary creatures known as the Wild Things.")
    app.add_book("Goodnight Moon", "Margaret Wise Brown", "A bedtime story that depicts a rabbit saying goodnight to various objects in the room.")
    app.add_book("The Cat in the Hat", "Dr. Seuss", "A lively and entertaining story of a cat wearing a hat who visits children on a rainy day.")

    # Adding more stories
    app.add_book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "The magical tale of a young wizard, Harry Potter, and his adventures at Hogwarts School of Witchcraft and Wizardry.")
    app.add_book("The Hobbit", "J.R.R. Tolkien", "The enchanting story of Bilbo Baggins, a hobbit who embarks on a grand adventure to reclaim the treasure guarded by the dragon Smaug.")
    app.add_book("Matilda", "Roald Dahl", "The heartwarming story of a gifted girl named Matilda, who uses her intelligence and telekinetic powers to overcome adversity.")
    app.add_book("Charlotte's Web", "E.B. White", "A touching tale of friendship between a pig named Wilbur and a spider named Charlotte, who saves him from being slaughtered.")
    app.add_book("The Secret Garden", "Frances Hodgson Burnett", "The story of Mary Lennox, a young girl who discovers a hidden garden and learns about the magic of friendship and nature.")
    app.add_book("Alice's Adventures in Wonderland", "Lewis Carroll", "A whimsical journey of a young girl named Alice, who falls down a rabbit hole into a fantastical world filled with peculiar creatures.")
    app.add_book("The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "C.S. Lewis", "The gripping tale of four siblings who discover a magical wardrobe leading to the land of Narnia, ruled by the White Witch.")
    app.add_book("Winnie-the-Pooh", "A.A. Milne", "The charming adventures of Winnie-the-Pooh, a bear with a love for honey, and his friends in the Hundred Acre Wood.")
    app.add_book("Peter Pan", "J.M. Barrie", "The timeless story of Peter Pan, the boy who never grows up, and his adventures with Wendy, John, Michael, and the Lost Boys in Neverland.")

    while True:
        print("\n1. Browse Books")
        print("2. Read Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            app.browse_books()
        elif choice == '2':
            book_index = int(input("Enter the index of the book to read the summary: "))
            app.read_summary(book_index)
        elif choice == '3':
            print("Exiting the application...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
