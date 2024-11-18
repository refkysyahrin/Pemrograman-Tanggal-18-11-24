import sqlite3

# Connect to SQLite database
con = sqlite3.connect("DBI.db")
cur = con.cursor()

# Create table nilai_siswa
cur.execute("""
    CREATE TABLE IF NOT EXISTS nilai_siswa (
        nama_siswa TEXT,
        biologi INT,
        fisika INT,
        inggris INT,
        prediksi_fakultas TEXT
    )
""")
con.commit()
con.close()

print("Database setup completed!")
