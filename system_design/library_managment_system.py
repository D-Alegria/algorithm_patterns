"""
Actors:
-Librarian
-Members
-System

The system should be able to
- Add/Remove/Edit a book
- Search the catalog
- Register new account / cancel membership
- Checkout book
- Reserve book
- Renew a book
- Return a book

"""
from enum import Enum


class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7


class Library:
    pass


class Book:
    pass


class BookItem:
    pass


class Account:
    pass


