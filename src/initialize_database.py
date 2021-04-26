from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists questions;
    ''')
    cursor.execute('''
        drop table if exists series;
    ''')
    cursor.execute('''
        drop table if exists series_questions;
    ''')
    connection.commit()


def create_users_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL UNIQUE,
            is_admin INTEGER NOT NULL
        );
    ''')
    connection.commit()


def create_questions_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table questions (
            id TEXT PRIMARY KEY,
            truth INTEGER NOT NULL,
            statement TEXT NOT NULL,
            comment TEXT
        );
    ''')
    connection.commit()


def create_series_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table series (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL
        );
    ''')
    connection.commit()


def create_series_questions_table(connection):
    cursor = connection.cursor()
    cursor.execute('''
        create table series_questions (
            id TEXT PRIMARY KEY,
            id_series TEXT NOT NULL,
            id_question TEXT NOT NULL
        );
    ''')
    connection.commit()


def create_tables(connection):
    create_users_table(connection)
    create_questions_table(connection)
    create_series_table(connection)
    create_series_questions_table(connection)


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
