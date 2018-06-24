import sqlite3
from config import DB_ADDRESS


def set_up_and_connect():
    db_connection = sqlite3.connect(DB_ADDRESS)
    db_connection.execute('CREATE TABLE IF NOT EXISTS images '
                          '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                          'content BLOB, '
                          'url TEXT, '
                          'average_red_lvl REAL, '
                          'average_green_lvl REAL, '
                          'average_blue_lvl REAL )')

    return db_connection


def insert_image_entity(db_connection, image_blob, url, avg_red_lvl, avg_green_lvl, avg_blue_lvl):
    db_connection.execute(
        'INSERT INTO images(content, url, average_red_lvl, average_green_lvl, average_blue_lvl) VALUES(?,?,?,?,?)',
        [image_blob, url, avg_red_lvl, avg_green_lvl, avg_blue_lvl])
    db_connection.commit()
