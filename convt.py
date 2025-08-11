import tkinter as tk
from tkinter import messagebox
import requests

def get_crypto_price(crypto_id, vs_currency):
    """
    Fetch the current price for the given cryptocurrency in the specified currency.
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={vs_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if crypto_id in data and vs_currency in data[crypto_id]:
            return data[crypto_id][vs_currency]
        else:
            return None
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
        return None

def convert():
    crypto = crypto_entry.get().strip().lower()
    vs_cur = vs_currency_entry.get().strip().lower()
    try:
        amount = float(amount_entry.get().strip())
    except ValueError:
        messagebox.showerror("Input Error", "Invalid amount: must be a number.")
        return
    
    price = get_crypto_price(crypto, vs_cur)
    if price is None:
        messagebox.showerror("Conversion Error", "Error fetching conversion rate for provided values.")
        return

    result = f"1 {crypto.capitalize()} = {price} {vs_cur.upper()}\n" \
             f"{amount} {crypto.capitalize()} = {amount * price} {vs_cur.upper()}"
    result_text.set(result)

# Set up the main window
root = tk.Tk()
root.title("Real-Time Cryptocurrency Converter")
root.geometry("450x220")
root.configure(padx=20, pady=20)

# Create input fields and labels
crypto_label = tk.Label(root, text="Cryptocurrency (bitcoin, ethereum, etc.):")
crypto_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
crypto_entry = tk.Entry(root, width=30)
crypto_entry.grid(row=0, column=1, pady=(0, 5))

vs_currency_label = tk.Label(root, text="Conversion Currency (usd, eur, etc.):")
vs_currency_label.grid(row=1, column=0, sticky="w", pady=(0, 5))
vs_currency_entry = tk.Entry(root, width=30)
vs_currency_entry.grid(row=1, column=1, pady=(0, 5))

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
amount_entry = tk.Entry(root, width=30)
amount_entry.grid(row=2, column=1, pady=(0, 5))

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert, width=15, bg="#4CAF50", fg="white")
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label to display results
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()