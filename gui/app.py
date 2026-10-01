
import tkinter as tk
from tkinter import ttk, messagebox
import requests

API_URL = "http://127.0.0.1:5000"
API_KEY = "mysecret1234"

headers = {"X-API-Key": API_KEY}


def add_product():
    name = name_entry.get().strip()
    url = url_entry.get().strip()
    target_price = target_entry.get().strip()
    email = email_entry.get().strip()


    if not name or not url or not target_price or not email:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    try:
        target_price = float(target_price)
        if target_price <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Error", "Enter a valid positive target price"
        )
        return

    product = {
        "name": name,
        "url": url,
        "target_price": target_price,
        "email": email,
        "scraper": "selenium"
    }

    try:
        response = requests.post(
            f"{API_URL}/products",
            json=product,
            headers=headers
        )
        response.raise_for_status()

        messagebox.showinfo("Success", "Product added successfully")

        name_entry.delete(0, tk.END)
        url_entry.delete(0, tk.END)
        target_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

    except requests.RequestException as error:
        messagebox.showerror("API Error", str(error))

def view_products():
    try:
        response = requests.get(
            f"{API_URL}/products",
            headers=headers
        )
        response.raise_for_status()

        products = response.json()

        if not products:
            messagebox.showinfo("Products", "No products found")
            return

        window = tk.Toplevel(root)
        window.title("All Products")
        window.geometry("700x400")

        columns = ("ID", "Name", "Target Price", "Current Price", "Status")

        table = ttk.Treeview(
            window,
            columns=columns,
            show="headings"
        )

        for column in columns:
            table.heading(column, text=column)
            table.column(column, width=130)

        for product in products:
            table.insert(
                "",
                tk.END,
                values=(
                    product.get("id"),
                    product.get("name"),
                    product.get("target_price"),
                    product.get("current_price"),
                    product.get("status")
                )
            )

        table.pack(fill="both", expand=True, padx=10, pady=10)

    except requests.RequestException as error:
        messagebox.showerror("API Error", str(error))


def check_product_price():
    product_id = product_id_entry.get().strip()

    if not product_id.isdigit():
        messagebox.showerror("Error", "Enter a valid product ID")
        return

    try:
        response = requests.post(
            f"{API_URL}/products/{product_id}/check-price",
            headers=headers
        )
        response.raise_for_status()

        data = response.json()
        messagebox.showinfo(
            "Price Check",
            f"Product: {data['product']['name']}\n"
            f"Current Price: {data['current_price']}\n"
            f"Status: {data['status']}"
        )
    except requests.RequestException as error:
        messagebox.showerror("API Error", str(error))

def delete_product():
        product_id = product_id_entry.get().strip()

        if not product_id.isdigit():
            messagebox.showerror("Error", "Enter a valid product ID")
            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete product {product_id}?"
        )

        if not confirm:
            return

        try:
            response = requests.delete(
                f"{API_URL}/products/{product_id}",
                headers=headers
            )
            response.raise_for_status()

            messagebox.showinfo("Success", "Product deleted successfully")
            product_id_entry.delete(0, tk.END)

        except requests.RequestException as error:
            messagebox.showerror("API Error", str(error))


def update_product():
    product_id = product_id_entry.get().strip()

    if not product_id.isdigit():
        messagebox.showerror("Error", "Enter a valid product ID")
        return

    name = update_name_entry.get().strip()
    url = update_url_entry.get().strip()
    target_price = update_target_entry.get().strip()
    email = update_email_entry.get().strip()

    if not name or not url or not target_price or not email:
        messagebox.showerror("Error", "Please fill in all update fields")
        return

    try:
        target_price = float(target_price)
        if target_price <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive target price")
        return

    updated_data = {
        "name": name,
        "url": url,
        "target_price": target_price,
        "email": email
    }

    try:
        response = requests.put(
            f"{API_URL}/products/{product_id}",
            json=updated_data,
            headers=headers
        )
        response.raise_for_status()

        messagebox.showinfo("Success", "Product updated successfully")

    except requests.RequestException as error:
        messagebox.showerror("API Error", str(error))

def view_price_history():
    product_id = product_id_entry.get().strip()

    if not product_id.isdigit():
        messagebox.showerror("Error", "Enter a valid product ID")
        return

    try:
        response = requests.get(
            f"{API_URL}/products/{product_id}/history",
            headers=headers
        )
        response.raise_for_status()

        history = response.json()

        if not history:
            messagebox.showinfo(
                "Price History",
                "No price history found"
            )
            return

        history_text = ""

        for entry in history:
            history_text += (
                f"Price: {entry['price']}\n"
                f"Time: {entry['timestamp']}\n\n"
            )

        messagebox.showinfo(
            "Price History",
            history_text
        )

    except requests.RequestException as error:
        messagebox.showerror("API Error", str(error))


def view_report():
    try:
        response = requests.get(
            f"{API_URL}/report",
            headers=headers
        )
        response.raise_for_status()

        report = response.json()[0]

        report_text = (
            f"Total Products: {report['total_products']}\n"
            f"Target Price Reached: {report['target_reached']}\n"
            f"Average Price: {report['average_price']}\n"
            f"Highest Price: {report['highest_price']}\n"
            f"Lowest Price: {report['lowest_price']}\n"
            f"Largest Price Drop: {report['largest_price_drop']}"
        )

        messagebox.showinfo(
            "Product Report",
            report_text
        )

    except requests.RequestException as error:
        messagebox.showerror("API Error", str(error))

root = tk.Tk()
root.title("Smart Deal Tracker")
root.geometry("500x450")

title = ttk.Label(
    root,
    text="Smart Deal Tracker",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

form = ttk.Frame(root, padding=20)
form.pack(fill="x")

ttk.Label(form, text="Product Name").grid(
    row=0, column=0, sticky="w", pady=8
)
name_entry = ttk.Entry(form, width=35)
name_entry.grid(row=0, column=1, pady=8)

ttk.Label(form, text="Product URL").grid(
    row=1, column=0, sticky="w", pady=8
)
url_entry = ttk.Entry(form, width=35)
url_entry.grid(row=1, column=1, pady=8)

ttk.Label(form, text="Target Price").grid(row=2, column=0, sticky="w", pady=8)
target_entry = ttk.Entry(form, width=35)
target_entry.grid(row=2, column=1, pady=8)

ttk.Label(form, text="Email").grid(row=3, column=0, sticky="w", pady=8)
email_entry = ttk.Entry(form, width=35)
email_entry.grid(row=3, column=1, pady=8)

add_button = ttk.Button(
    root,
    text="Add Product",
    command=add_product
)
add_button.pack(pady=20)
view_button = ttk.Button(
    root,
    text="View Products",
    command=view_products
)
view_button.pack(pady=10)


price_frame = ttk.Frame(root, padding=10)
price_frame.pack()

ttk.Label(price_frame, text="Product ID").pack(side="left")

product_id_entry = ttk.Entry(price_frame, width=15)
product_id_entry.pack(side="left", padx=5)

check_button = ttk.Button(
    price_frame,
    text="Check Price",
    command=check_product_price
)
check_button.pack(side="left")
delete_button = ttk.Button(
    price_frame,
    text="Delete Product",
    command=delete_product
)
delete_button.pack(side="left", padx=5)

history_button = ttk.Button(
    price_frame,
    text="Price History",
    command=view_price_history
)
history_button.pack(side="left", padx=5)

report_button = ttk.Button(
    root,
    text="View Report",
    command=view_report
)
report_button.pack(pady=10)

update_frame = ttk.LabelFrame(root, text="Update Product", padding=10)
update_frame.pack(fill="x", padx=10, pady=10)

ttk.Label(update_frame, text="New Name").grid(row=0, column=0, sticky="w")
update_name_entry = ttk.Entry(update_frame, width=25)
update_name_entry.grid(row=0, column=1, pady=3)

ttk.Label(update_frame, text="New URL").grid(row=1, column=0, sticky="w")
update_url_entry = ttk.Entry(update_frame, width=25)
update_url_entry.grid(row=1, column=1, pady=3)

ttk.Label(update_frame, text="New Target Price").grid(row=2, column=0, sticky="w")
update_target_entry = ttk.Entry(update_frame, width=25)
update_target_entry.grid(row=2, column=1, pady=3)

ttk.Label(update_frame, text="New Email").grid(row=3, column=0, sticky="w")
update_email_entry = ttk.Entry(update_frame, width=25)
update_email_entry.grid(row=3, column=1, pady=3)

update_button = ttk.Button(
    update_frame,
    text="Update Product",
    command=update_product
)
update_button.grid(row=4, column=0, columnspan=2, pady=8)
root.mainloop()

