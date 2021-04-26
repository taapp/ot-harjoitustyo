from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
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
            truth TEXT NOT NULL,
            statement TEXT NOT NULL,
            comment TEXT
        );
    ''')
    connection.commit()



def create_tables(connection):
    create_users_table(connection)
    create_questions_table(connection)


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
