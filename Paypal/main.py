import tkinter as tk

# Calculate the PayPal fee
def calculate_fee():
    amount = float(amount_entry.get())
    currency = currency_combobox.get()
    fee_rate = get_fee_rate(currency)
    fee = amount * fee_rate
    total = amount + fee
    fee_formatted = format_currency(fee, currency)
    total_formatted = format_currency(total, currency)
    tk.messagebox.showinfo('PayPal fee calculation', f'PayPal fee: {fee_formatted}\nTotal amount: {total_formatted}')

# Get the fee rate based on the currency
def get_fee_rate(currency):
    if currency == 'USD':
        return 0.029
    elif currency == 'EUR':
        return 0.035
    else:
        return 0.039

# Format the currency
def format_currency(amount, currency):
    if currency == 'USD':
        return f'${amount:.2f}'
    elif currency == 'EUR':
        return f'€{amount:.2f}'
    else:
        return f'{amount:.2f} {currency}'

# Show the popup window for selecting the bill type
def select_bill_type():
    bill_type = tk.simpledialog.askstring('Select bill type', 'What type of bill is this?')
    tk.messagebox.showinfo('Bill type', f'You selected {bill_type} as the bill type.')

# Create the GUI
root = tk.Tk()
root.title('PayPal Fee Calculator')

# Create the input elements
amount_label = tk.Label(root, text='Amount:')
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()
currency_label = tk.Label(root, text='Currency:')
currency_label.pack()
currency_combobox = ttk.Combobox(root, values=['USD', 'EUR', 'GBP'])
currency_combobox.pack()
currency_combobox.current(0)
calculate_button = tk.Button(root, text='Calculate', command=calculate_fee)
calculate_button.pack()
bill_type
