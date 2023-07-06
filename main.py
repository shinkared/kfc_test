import requests
import sqlite3


def bd_ini(stores: list):
    # Подключение к БД
    try:
        sqlite_connection = sqlite3.connect('kfc.db')
        cursor = sqlite_connection.cursor()
        # Запрос создания таблицы
        create_t = f"""CREATE TABLE IF NOT EXISTS kfc_nsk (
    storeId INTEGER PRIMARY KEY,
    title_en TEXT,
    title_ru TEXT,
    streetAddress TEXT,
    city TEXT,
    coordinates_x REAL,
    coordinates_y REAL,
    startTimeLocal TIME,
    endTimeLocal TIME,
    breakfastStartTime TIME,
    breakfastEndTime TIME);"""
        cursor.execute(create_t)
        # Запись в ресторанов в БД
        for i in stores:
            write_to_bd(cursor, i["store"])
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при подключении к sqlite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


def write_to_bd(cursor, store):
    # Составление запроса и последующая запись
    query = f"""INSERT OR IGNORE INTO kfc_nsk (storeId, title_en, title_ru, streetAddress, city, coordinates_x, 
    coordinates_y, startTimeLocal, endTimeLocal, breakfastStartTime, breakfastEndTime) VALUES (
    {store["storeId"]},
    '{store["title"]["en"]}', 
    '{store["title"]["ru"]}', 
    '{store["contacts"]["streetAddress"]["ru"]}', 
    '{store["contacts"]["city"]["ru"]}', 
    {store["contacts"]["coordinates"]["geometry"]["coordinates"][0]}, 
    {store["contacts"]["coordinates"]["geometry"]["coordinates"][1]},
    '{store["openingHours"]["regular"]["startTimeLocal"]}',
    '{store["openingHours"]["regular"]["endTimeLocal"]}', 
    '{store["menues"][0]["availability"]["regular"]["startTimeLocal"]}', 
    '{store["menues"][0]["availability"]["regular"]["endTimeLocal"]}');"""
    cursor.execute(query)


def main():
    # Составление запроса
    body = {"coordinates": [55.004174, 82.894257], "radiusMeters": 130000, "channel": "website", "showClosed": True}
    headers = {"Content-Length": '155', "Host": "api.kfc.digital"}
    response = requests.post('https://api.kfc.digital/api/store/v2/store.geo_search', headers=headers, json=body)
    if response.status_code == 200:
        data = response.json()
        stores = data["searchResults"]
        bd_ini(stores)
    print(response.status_code)


if __name__ == '__main__':
    main()
