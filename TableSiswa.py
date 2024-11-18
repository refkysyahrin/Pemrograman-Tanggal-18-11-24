import sqlite3
from tkinter import *

# Function to submit data
def submit_data():
    nama = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Predict faculty
    if biologi > fisika and biologi > inggris:
        prediksi = "Kedokteran"
    elif fisika > biologi and fisika > inggris:
        prediksi = "Teknik"
    else:
        prediksi = "Bahasa"

    # Insert data into database
    con = sqlite3.connect("DBI.db")
    cur = con.cursor()
    cur.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?)",
                (nama, biologi, fisika, inggris, prediksi))
    con.commit()
    con.close()
    label_result.config(text=f"Data berhasil disimpan: {prediksi}")

# GUI setup
root = Tk()
root.title("Input Data Siswa")

# Create labels and entries
Label(root, text="Nama Siswa").grid(row=0, column=0)
entry_nama = Entry(root)
entry_nama.grid(row=0, column=1)

Label(root, text="Nilai Biologi").grid(row=1, column=0)
entry_biologi = Entry(root)
entry_biologi.grid(row=1, column=1)

Label(root, text="Nilai Fisika").grid(row=2, column=0)
entry_fisika = Entry(root)
entry_fisika.grid(row=2, column=1)

Label(root, text="Nilai Inggris").grid(row=3, column=0)
entry_inggris = Entry(root)
entry_inggris.grid(row=3, column=1)

# Create a submit button
Button(root, text="Submit", command=submit_data).grid(row=4, column=0, columnspan=2)

# Result label
label_result = Label(root, text="")
label_result.grid(row=5, column=0, columnspan=2)

root.mainloop()
