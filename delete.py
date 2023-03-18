import tkinter as tk
import mysql.connector



db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="disha2003",
    database="collegedb"
)
def delete():
    username = username_entry.get()
    password = password_entry.get()


    cursor = db.cursor()
    sql =  "DELETE FROM studnt WHERE username=%s AND password=%s"
    values = (username,password)
    cursor.execute(sql,values)
    db.commit()
    message_label.config(text="Data successfully deleted!")


root = tk.Tk()
root.title("DELETE PAGE")
root["bg"]="black"
root.geometry("400x150")


username_label = tk.Label(root, text="Username")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()


login_button = tk.Button(root, text="Delete", command=delete)
login_button.pack()
message_label = tk.Label(root, text="")
message_label.pack()



root.mainloop()
