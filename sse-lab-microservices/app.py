from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {'id': 1, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'publication_year': 1960, 'genre': 'Southern Gothic'},
    {'id': 2, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949, 'genre': 'Dystopian Fiction'},
    {'id': 3, 'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'publication_year': 1813, 'genre': 'Romantic Novel'},
    {'id': 4, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'publication_year': 1925, 'genre': 'American Literature'},
    {'id': 5, 'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'publication_year': 2008, 'genre': 'Young Adult Dystopian'}
]

@app.route('/books', methods=['GET'])
def get_books():
    """Fetch books with optional filtering by genre."""
    genre_filter = request.args.get('genre', '').lower()

    if genre_filter:
        filtered_books = [book for book in books if genre_filter in book['genre'].lower()]
    else:
        filtered_books = books

    return jsonify({"books": filtered_books})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    """Fetch a single book by ID."""
    book = next((book for book in books if book['id'] == book_id), None)
    if book is None:
        return jsonify({"error": "Book not found"}), 404
    return jsonify({"book": book})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)