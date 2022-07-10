"""Module to house all opertions pertaining to Books in the Library"""

from pathlib import Path
import qrcode
from typing import Any
from data_structures.book import Book
from data_structures.student import Student, StudentStatus

from qr_code.generate_qr import generate_QR_code_object, save_QR_object

from constants.filepaths import QR_CODE_STUDENT_PATH


def register_student(student: Student) -> None:
    """Method to register student and generate QR Code for the Student

    Args:
        student (Student): `Student` Object
    """
    student.set_student_status(StudentStatus.ACTIVE)
    data = student.get_qr_data()
    qr_obj = generate_QR_code_object(data)
    student.set_qr_data(qr_obj)
    return qr_obj


def generate_student_qr(student: Student) -> qrcode.make:
    """Method to generate a QR object and save to a book

    Args:
        book (Book): `Book` object

    Returns:
        (qrcode.make): Data to generate QR as Image
    """
    data = student.get_qr_data()
    qr_obj = generate_QR_code_object(data)
    student.set_qr_data(qr_obj)
    return qr_obj


def download_student_ID_qr(student: Student) -> Path:
    """Method to download the QR Code representing a `Book` object"""
    file_name = student.get_id()
    qr_data = student.get_qr_data()
    if qr_data is None:
        # Generate the QR Code and then save
        qr_data = generate_student_qr(student)
    file_path = save_QR_object(qr_data, QR_CODE_STUDENT_PATH, file_name)
    return file_path
