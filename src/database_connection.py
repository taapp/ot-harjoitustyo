import sqlite3
from pathlib import Path

DATABASE_FILE_PATH = Path(__file__).parent / "data" / "database.db"
CONNECTION = sqlite3.connect(DATABASE_FILE_PATH)
CONNECTION.row_factory = sqlite3.Row


def get_database_connection():
    return CONNECTION
