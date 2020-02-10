from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Reviews
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

Reviews = Reviews()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    return render_template('reviews.html', reviews=Reviews)

@app.route('/book/<string:isbn>')
def book(isbn):
    return render_template('book.html', isbn=isbn)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        #book = request.form['book']
        score = request.form['score']
        comment = request.form['comment']
        #print(score, comment)
        if score == '':
            return render_template('index.html', message='Please enter required fields.')
        return render_template('success.html')

@app.route('/api/<int:isbn>')
def book_api(book_id):
    '''Return information about a book.'''

    # Make sure book exists
    book = book.query.get(book_id)
    if book is None:
        return jsonify({"error": "Invalid book_id"}), 422

    # Get all info about the book.



if __name__ == '__main__':
    app.run(debug=True)
