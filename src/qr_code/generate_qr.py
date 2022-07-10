"""Common methods to generate the QR Code"""

import qrcode
from pathlib import Path
from typing import Any


def generate_QR_code_object(data: dict) -> Any:
    """Method to generate QR Code containing the data requested"""
    qrcode.make(data)


def save_QR_object(qr_obj: qrcode.make, directory: Path, filename: str) -> Path:
    """Method saves the QR Code in the `data` folder"""
    rel_path = Path(directory, filename)
    qr_obj.save(rel_path)
    return rel_path
