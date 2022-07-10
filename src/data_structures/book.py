"""Class to describe a Book and associated properties"""

from pathlib import Path
import uuid
from enum import Enum, auto
import qrcode
from typing import Any, Optional
from data_structures.student import Student

from dataclasses import dataclass, asdict


class BookStatus(Enum):
    ISSUED = auto()
    AVAILABLE = auto()
    OVERDUE = auto()
    LOST = auto()
    DAMAGED = auto()


@dataclass(frozen=False, order=True)
class Book:
    """Class describing a Book"""

    title: str
    sub_title: str
    author: str
    publisher: str
    price: int
    id: str = uuid.uuid4()
    status: BookStatus = BookStatus.AVAILABLE
    issued_to: Optional[Student] = None
    qr_code: Optional[qrcode.make] = None
    qr_code_path = Path(".")

    def get_id(self) -> str:
        """Method to get ID of the `Book`"""
        return self.id

    def get_title(self) -> str:
        """Method to get title of the `Book`"""
        return self.title

    def get_sub_title(self) -> str:
        """Method to get sub title of the `Book`"""
        return self.sub_title

    def get_author(self) -> str:
        """Method to get author of the `Book`"""
        return self.author

    def get_publisher(self) -> str:
        """Method to get Publisher of the `Book`"""
        return self.publisher

    def get_price(self) -> int:
        """Method to get price of the `Book`"""
        return self.price

    def get_status(self) -> BookStatus:
        """Method to get status of the `Book`"""
        return self.status

    def set_status(self, status: BookStatus) -> None:
        """Method to set status of the `Book`"""
        self.status = status

    def set_issued_to(self, student: Student) -> None:
        """Method to set status of the `Book`"""
        self.assigned_to = student

    def get_qr_data(self) -> dict:
        """Method to get `Book`'s data to represented as QR Code

        Returns:
            dict: `Book` object represented as dictionary
        """
        return asdict(self, dict_factory=dict)

    def set_qr_data(self, qr_data: qrcode.make) -> None:
        """Method to set `Book`'s data to represented as QR Code"""
        self.qr_code = qr_data

    def get_qr_code_path(self) -> Path:
        """Method to return QR Path Path"""
        return self.qr_code_path

    def set_qr_code_path(self, path=Path) -> None:
        """Method to set the generated QR Code Path"""
        self.qr_code_path = path


if __name__ == "__main__":
    book = Book(title="First Book", sub_title="First Book subtitle", author="Adarsh Battu", publisher="In House", price=100)
