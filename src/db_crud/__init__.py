"""Initilizer to create the databases for Books and Students"""

import sqlite3
from sqlite3 import Error
from pathlib import Path
from typing import Any


db_type: dict[Any, str] = {None: "NULL", int: "INTEGER", float: "REAL", str: "TEXT", bytes: "BLOB"}


def create_connection(db_file: Path) -> sqlite3.connect:
    """create a database connection to a SQLite database and return the connection object

    Args:
        db_file (Path): Path to create the Database

    Returns:
        (sqlite3.connect): sqlite3 Connection object
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn


def create_table(connection: sqlite3.connect, table_object: object) -> None:
    """Method to create table using a datastructure

    Args:
        connection (sqlite3.connect): connection to use to create the table
        db_name (str): _description_

    Returns:
        sqlite3.Cursor: _description_
    """
    classname: str = table_object.__class__.__name__
    classname = classname.upper()
    cursor = connection.cursor()
    create_command: str = f"""CREATE TABLE IF NOT EXISTS {classname} (Title TEXT, Director TEXT, Year INT)"""
    cursor.execute(create_command)
    connection.commit()
    connection.close()
