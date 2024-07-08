import sqlite3
from datetime import datetime
def insert_multiple_records(records):
    try:
        sqlite_connection = sqlite3.connect('db.sqlite3')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_query = """INSERT INTO tournaments_tournaments
                                 ( name, picture, organizer, tournament_start_date, tournament_end_date, registration_start_date, registration_end_date,
                                  status, format_of_tournament, type_of_tournament, format_of_participation, prize_fund, game, max_teams)
                                  VALUES ( ?, ?, ?, ?, ?, ?, ?, 
                                          ?, 'Single Elimination', 'Online', '5', '0', ?, ?);"""

        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()
        print("Записи успешно вставлены в таблицу sqlitedb_developers", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

records_to_insert = []

for i in range(50):
    name = 'Test ' + str(i)
    current_dateTime = datetime.now()
    records_to_insert.append((name, 'images/tournaments/HS.jpg', 'BMSTU', '2024-06-19 15:40', current_dateTime,
                              current_dateTime, current_dateTime, 'Active', 'HS', 250))

insert_multiple_records(records_to_insert)