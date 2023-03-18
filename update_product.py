import tkinter as tk
import mysql.connector

# Create a connection to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="disha2003",
  database="collegedb"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Define a function to update a product in the database
def update_product():
    # Get the product name, price, and stocks from the user input
    product = product_entry.get()
    price = price_entry.get()
    stock = stock_entry.get()
    
    # Define the SQL query to update the product
    sql = "UPDATE stocks SET price = %s, stock = %s WHERE product = %s"
    values = (price, stock, product)
    
    # Execute the SQL query
    mycursor.execute(sql, values)
    
    # Commit the changes to the database
    mydb.commit()
    
    # Print a message to the user indicating that the update was successful
    message_label.config(text="Product updated successfully!")

# Create a tkinter window
window = tk.Tk()
window.geometry=("800x900")
window["bg"]="black"

# Add some labels and entry boxes for the user input
product_label = tk.Label(window, text="Product name:")
product_label.pack()
product_entry = tk.Entry(window)
product_entry.pack()

price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

stock_label = tk.Label(window, text="Stocks:")
stock_label.pack()
stock_entry = tk.Entry(window)
stock_entry.pack()

# Add a button to submit the user input and update the product in the database
update_button = tk.Button(window, text="Update Product", command=update_product)
update_button.pack()

# Add a label to display messages to the user
message_label = tk.Label(window, text="")
message_label.pack()

# Start the tkinter mainloop
window.mainloop()
