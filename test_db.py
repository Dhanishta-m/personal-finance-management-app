import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Dhanishta1810",
        database="finance_db"
    )

    print("Connected Successfully!")

except Exception as e:
    print("Error:", e)