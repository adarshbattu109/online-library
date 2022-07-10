"""Class describing a Student and Enum Class for Student's status"""


from pathlib import Path
import uuid
import qrcode
from enum import Enum, auto
from typing import Optional
from dataclasses import dataclass, asdict


class StudentStatus(Enum):
    """Status describing a status a `Student's` status"""

    ACTIVE = auto()
    INACTIVE = auto()
    CANCELLED = auto()


@dataclass
class Student:
    """Class describing a status and its assiociated actions"""

    name: str
    last_name: str
    status: StudentStatus = StudentStatus.ACTIVE
    id: str = uuid.uuid4()
    qr_code: Optional[qrcode.make] = None
    qr_code_path = Path(".")

    def get_student_id(self) -> str:
        """Return the `Student` id"""
        return self.id

    def get_student_name(self) -> str:
        """Method return the `Student`'s full name

        Returns:
            str: `Student`'s full name
        """
        return f"{self.name} {self.last_name}"

    def get_student_status(self) -> StudentStatus:
        """Method to get et the `Student`'s status"""
        return self.status

    def set_student_status(self, status: StudentStatus) -> None:
        """Method to set the `Student`'s status"""
        self.status = status

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
