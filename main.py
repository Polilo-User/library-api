from flask import Flask, request, jsonify
 

books = [
    {"id":1, "title":"1", "author":"1"},
    {"id":2, "title":"2", "author":"2"},
    {"id":3, "title":"3", "author":"3"}
]

app = Flask(__name__)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data.get("title"),
        "author": data.get("author")
    }

    books.append(new_book)
    return jsonify(new_book), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)