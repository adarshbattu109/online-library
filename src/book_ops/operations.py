"""Module to house all opertions pertaining to Books in the Library"""

import qrcode
from typing import Any
from data_structures.book import Book, BookStatus
from data_structures.student import Student

from qr_code.generate_qr import generate_QR_code_object, save_QR_object

from constants.filepaths import QR_CODE_BOOKS_PATH


def issue_book(book: Book, student: Student) -> None:
    """Method to assign a `Book` to a `Student`"""
    book.set_issued_to(student=student)
    book.set_status(BookStatus.ISSUED)


def return_book(book: Book) -> None:
    """Method to return the `Book` back to Library and mark it `Available`"""
    book.set_issued_to = None
    book.set_status(BookStatus.AVAILABLE)


def mark_book_as_lost(book: Book) -> None:
    """Method to set the `Book` as `Lost`

    Args:
        book (Book): `Book` object
    """
    book.set_status(BookStatus.LOST)


def mark_book_as_damaged(book: Book) -> None:
    """Method to set the `Book` as `Damaged`

    Args:
        book (Book): `Book` object
    """
    book.set_status(BookStatus.DAMAGED)


def generate_book_qr(book: Book) -> qrcode.make:
    """Method to generate a QR object and save to a book

    Args:
        book (Book): `Book` object

    Returns:
        (qrcode.make): Data to generate QR as Image
    """
    data = book.get_qr_data()
    qr_obj = generate_QR_code_object(data)
    book.set_qr_data(qr_obj)
    return qr_obj


def download_book_qr(book: Book) -> Any:
    """Method to download the QR Code representing a `Book` object"""
    file_name = book.get_id()
    qr_data = book.get_qr_data()
    if qr_data is None:
        # Generate the QR Code and then save
        qr_data = generate_book_qr(book)
    return save_QR_object(qr_data, QR_CODE_BOOKS_PATH, file_name)
