import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

class IceCreamApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ice Cream Parlor")
        self.geometry("800x600")
        self.configure(bg="grey")

        # Connect to SQLite database
        self.conn = sqlite3.connect('icecream.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.insert_sample_data()

        # GUI elements
        self.create_widgets()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors
                              (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory
                              (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions
                              (id INTEGER PRIMARY KEY, flavor_name TEXT, customer_name TEXT, allergy_concerns TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS allergens
                              (id INTEGER PRIMARY KEY, name TEXT)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cart
                              (id INTEGER PRIMARY KEY, flavor_id INTEGER,
                               FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors(id))''')
        self.conn.commit()

    def insert_sample_data(self):
        # Check if data already exists in seasonal_flavors table
        self.cursor.execute("SELECT COUNT(*) FROM seasonal_flavors")
        if self.cursor.fetchone()[0] > 0:
            print("Seasonal flavors already exist. Skipping insertion.")
            return

        # Insert sample flavors if no data exists
        sample_flavors = [
            ('Mango Delight', 3.99),
            ('Strawberry Fields', 4.49),
            ('Blueberry Bliss', 4.99),
            ('Chocolate Heaven', 3.49)
        ]
        self.cursor.executemany("INSERT INTO seasonal_flavors (name, price) VALUES (?,?)", sample_flavors)
        self.conn.commit()
        print("Sample flavors inserted successfully.")


    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self, text="Welcome to the Ice Cream Parlor", font=("Helvetica", 24, 'bold'), bg="grey")
        title_label.grid(row=0, column=0, columnspan=6, pady=20)
        # Order Button
        order_button = ttk.Button(self, text="Add to Cart", command=self.add_to_cart)
        order_button.grid(row=1, column=4,columnspan=1, padx=5,pady=5,sticky="ew")
        

        # Flavor Listbox
        flavor_frame = tk.Frame(self, bg="grey")
        flavor_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        flavor_label = tk.Label(flavor_frame, text="Seasonal Flavors", font=("Helvetica", 18, 'italic'), bg="grey")
        flavor_label.pack(anchor="w", padx=10, pady=10)
        self.flavor_listbox = tk.Listbox(flavor_frame, height=8, selectmode=tk.SINGLE, font=("Helvetica", 14), bg="white", fg="black", selectbackground="blue", selectforeground="white")
        self.flavor_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.populate_flavors()
        
        # Cart Listbox
        cart_frame = tk.Frame(self, bg="grey")
        cart_frame.grid(row=1, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")
        cart_label = tk.Label(cart_frame, text="My Cart", font=("Helvetica", 18, 'italic'), bg="grey")
        cart_label.pack(anchor="w", padx=10, pady=10)
        self.cart_listbox = tk.Listbox(cart_frame, height=8, selectmode=tk.SINGLE, font=("Helvetica", 14), bg="white", fg="black", selectbackground="blue", selectforeground="white")
        self.cart_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.populate_cart()
       


        # Search Section
        search_frame = tk.Frame(self, bg="grey")
        search_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        search_label = tk.Label(search_frame, text="Search Flavor", font=("Helvetica", 18, 'italic'), bg="grey")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 14))
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        search_button = ttk.Button(search_frame, text="Search", command=self.search_flavors)
        search_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        refresh_button = ttk.Button(search_frame, text="Refresh", command=self.populate_flavors)
        refresh_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        # Allergens Section
        allergen_frame = tk.Frame(self, bg="grey")
        allergen_frame.grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky="nsew")
        allergen_label = tk.Label(allergen_frame, text="Add Allergen", font=("Helvetica", 18, 'italic'), bg="grey")
        allergen_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.allergen_entry = tk.Entry(allergen_frame, font=("Helvetica", 14))
        self.allergen_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        add_allergen_button = ttk.Button(allergen_frame, text="Add", command=self.add_allergen)
        add_allergen_button.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky="ew")

        # Suggest Flavor Section
        suggest_frame = tk.Frame(self, bg="grey")
        suggest_frame.grid(row=3, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        suggest_label = tk.Label(suggest_frame, text="Suggest Flavor", font=("Helvetica", 18, 'italic'), bg="grey")
        suggest_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.suggest_flavor_entry = tk.Entry(suggest_frame, font=("Helvetica", 14))
        self.suggest_flavor_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        suggest_name_label = tk.Label(suggest_frame, text="Your Name", font=("Helvetica", 18, 'italic'), bg="grey")
        suggest_name_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.suggest_name_entry = tk.Entry(suggest_frame, font=("Helvetica", 14))
        self.suggest_name_entry.grid(row=0, column=3, padx=10, pady=10, sticky="ew")
        suggest_allergy_label = tk.Label(suggest_frame, text="Allergy Concerns", font=("Helvetica", 18, 'italic'), bg="grey")
        suggest_allergy_label.grid(row=0, column=4, padx=10, pady=10, sticky="w")
        self.suggest_allergy_entry = tk.Entry(suggest_frame, font=("Helvetica", 14))
        self.suggest_allergy_entry.grid(row=0, column=5, padx=10, pady=10, sticky="ew")
        suggest_button = ttk.Button(suggest_frame, text="Suggest", command=self.suggest_flavor)
        suggest_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Configure grid weights
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)

    def populate_flavors(self):
        self.flavor_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT name FROM seasonal_flavors")
        flavors = [row[0] for row in self.cursor.fetchall()]
        for flavor in flavors:
            self.flavor_listbox.insert(tk.END, flavor)

    def populate_cart(self):
        self.cart_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT seasonal_flavors.name FROM cart JOIN seasonal_flavors ON cart.flavor_id = seasonal_flavors.id")
        cart_items = [row[0] for row in self.cursor.fetchall()]
        for item in cart_items:
            self.cart_listbox.insert(tk.END, item)


    def add_to_cart(self):
        flavor_index = self.flavor_listbox.curselection()
        if not flavor_index:
            messagebox.showerror("Error", "Please select a flavor")
            return
        flavor = self.flavor_listbox.get(flavor_index)
        self.cursor.execute("SELECT id FROM seasonal_flavors WHERE name=?", (flavor,))
        flavor_id = self.cursor.fetchone()[0]
        self.cursor.execute("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id,))
        self.conn.commit()
        self.populate_cart()
        messagebox.showinfo("Success", "Added to cart!")

    def remove_from_cart(self):
    # Get the index of the selected item in the cart listbox
        selected_index = self.cart_listbox.curselection()

    # Check if an item is selected
        if not selected_index:
           messagebox.showerror("Error", "Please select an item to remove from the cart")
           return

    # Get the item text from the cart listbox based on the selected index
        selected_item = self.cart_listbox.get(selected_index)

    # Retrieve the flavor_id from the seasonal_flavors table
        self.cursor.execute("SELECT id FROM seasonal_flavors WHERE name=?", (selected_item,))
        flavor_id = self.cursor.fetchone()[0]

    # Delete the selected item from the cart
        self.cursor.execute("DELETE FROM cart WHERE flavor_id=?", (flavor_id,))
        self.conn.commit()

    # Update the cart listbox to reflect the changes
        self.populate_cart()

    # Show a success message
        messagebox.showinfo("Success", f"Removed '{selected_item}' from cart")



    def add_allergen(self):
        allergen = self.allergen_entry.get().strip()
        if not allergen:
            messagebox.showerror("Error", "Please enter an allergen")
            return
        self.cursor.execute("SELECT COUNT(*) FROM allergens WHERE name=?", (allergen,))
        if self.cursor.fetchone()[0] > 0:
            messagebox.showerror("Error", "Allergen already exists")
        else:
            self.cursor.execute("INSERT INTO allergens (name) VALUES (?)", (allergen,))
            self.conn.commit()
            messagebox.showinfo("Success", "Allergen added!")
        self.allergen_entry.delete(0, tk.END)

    def search_flavors(self):
        search_term = self.search_entry.get().strip()
        if not search_term:
            self.populate_flavors()
            return
        self.flavor_listbox.delete(0, tk.END)
        self.cursor.execute("SELECT name FROM seasonal_flavors WHERE name LIKE ?", ('%' + search_term + '%',))
        flavors = [row[0] for row in self.cursor.fetchall()]
        for flavor in flavors:
            self.flavor_listbox.insert(tk.END, flavor)

    def suggest_flavor(self):
        flavor_name = self.suggest_flavor_entry.get().strip()
        customer_name = self.suggest_name_entry.get().strip()
        allergy_concerns = self.suggest_allergy_entry.get().strip()
        if not flavor_name or not customer_name:
            messagebox.showerror("Error", "Please enter both flavor name and your name")
            return
        self.cursor.execute("INSERT INTO customer_suggestions (flavor_name, customer_name, allergy_concerns) VALUES (?,?,?)",
                            (flavor_name, customer_name, allergy_concerns))
        self.conn.commit()
        messagebox.showinfo("Success", "Flavor suggestion submitted!")
        self.suggest_flavor_entry.delete(0, tk.END)
        self.suggest_name_entry.delete(0, tk.END)
        self.suggest_allergy_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = IceCreamApp()
    app.mainloop()