import MySQLdb

try:
    print("Connecting to MySQL...")
    db = MySQLdb.connect(host="localhost", user="root", passwd="")
    cursor = db.cursor()
    print("Creating database if not exists...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS placement_guide")
    print("Database `placement_guide` created or already exists.")
    db.close()
except Exception as e:
    print(f"Error creating database: {e}")
