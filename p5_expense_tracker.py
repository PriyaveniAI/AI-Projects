# ============================================
# P5 Expense Tracker - No API Key Required!
# ============================================

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import datetime

# ---- Data File ----
DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)

expenses = load_expenses()

# ---- Functions ----

def add_expense():
    desc = desc_entry.get().strip()
    amount = amount_entry.get().strip()
    category = category_var.get()

    if not desc:
        messagebox.showwarning("Warning", "Please enter a description!")
        return
    if not amount:
        messagebox.showwarning("Warning", "Please enter an amount!")
        return
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid amount!")
        return

    expense = {
        "date": datetime.datetime.now().strftime("%d-%m-%Y"),
        "description": desc,
        "category": category,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    refresh_table()
    update_summary()

    desc_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"✅ Expense ₹{amount:.2f} added!")

def delete_expense():
    selected = table.selection()
    if not selected:
        messagebox.showwarning("Warning", "Please select an expense to delete!")
        return
    index = table.index(selected[0])
    expenses.pop(index)
    save_expenses(expenses)
    refresh_table()
    update_summary()
    messagebox.showinfo("Success", "🗑️ Expense deleted!")

def refresh_table():
    for row in table.get_children():
        table.delete(row)
    for i, e in enumerate(expenses):
        tag = "odd" if i % 2 == 0 else "even"
        table.insert("", "end", values=(
            e["date"],
            e["description"],
            e["category"],
            f"₹{e['amount']:.2f}"
        ), tags=(tag,))

def update_summary():
    total = sum(e["amount"] for e in expenses)
    total_label.config(text=f"💰 Total Spent: ₹{total:.2f}")

    # Category wise
    categories = {}
    for e in expenses:
        cat = e["category"]
        categories[cat] = categories.get(cat, 0) + e["amount"]

    summary_text = ""
    for cat, amt in categories.items():
        summary_text += f"{cat}: ₹{amt:.2f}\n"

    category_label.config(text=summary_text if summary_text else "No expenses yet!")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        save_expenses(expenses)
        refresh_table()
        update_summary()

# ---- Build Window ----

window = tk.Tk()
window.title("💰 Expense Tracker")
window.geometry("620x680")
window.configure(bg="#0f172a")
window.resizable(False, False)

# Header
header = tk.Frame(window, bg="#10b981", pady=14)
header.pack(fill=tk.X)
tk.Label(header, text="💰 Expense Tracker", font=("Arial", 20, "bold"),
         bg="#10b981", fg="white").pack()
tk.Label(header, text="Track your daily expenses easily!", font=("Arial", 10),
         bg="#10b981", fg="#d1fae5").pack()

# Input Frame
input_frame = tk.LabelFrame(window, text=" Add New Expense ",
                              font=("Arial", 11, "bold"),
                              bg="#1e293b", fg="#94a3b8",
                              padx=15, pady=10)
input_frame.pack(fill=tk.X, padx=15, pady=10)

# Row 1
row1 = tk.Frame(input_frame, bg="#1e293b")
row1.pack(fill=tk.X, pady=4)

tk.Label(row1, text="Description:", font=("Arial", 10, "bold"),
         bg="#1e293b", fg="#94a3b8", width=12, anchor="w").pack(side=tk.LEFT)
desc_entry = tk.Entry(row1, font=("Arial", 11), bg="#0f172a", fg="white",
                      insertbackground="white", relief=tk.FLAT, bd=6)
desc_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Row 2
row2 = tk.Frame(input_frame, bg="#1e293b")
row2.pack(fill=tk.X, pady=4)

tk.Label(row2, text="Amount (₹):", font=("Arial", 10, "bold"),
         bg="#1e293b", fg="#94a3b8", width=12, anchor="w").pack(side=tk.LEFT)
amount_entry = tk.Entry(row2, font=("Arial", 11), bg="#0f172a", fg="white",
                        insertbackground="white", relief=tk.FLAT, bd=6)
amount_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Row 3
row3 = tk.Frame(input_frame, bg="#1e293b")
row3.pack(fill=tk.X, pady=4)

tk.Label(row3, text="Category:", font=("Arial", 10, "bold"),
         bg="#1e293b", fg="#94a3b8", width=12, anchor="w").pack(side=tk.LEFT)
category_var = tk.StringVar(value="Food")
categories = ["Food", "Transport", "Shopping", "Bills", "Health", "Education", "Other"]
category_menu = ttk.Combobox(row3, textvariable=category_var, values=categories,
                              font=("Arial", 11), state="readonly", width=20)
category_menu.pack(side=tk.LEFT)

# Buttons
btn_frame = tk.Frame(input_frame, bg="#1e293b")
btn_frame.pack(fill=tk.X, pady=8)

tk.Button(btn_frame, text="➕ Add Expense", font=("Arial", 11, "bold"),
          bg="#10b981", fg="white", relief=tk.FLAT, cursor="hand2",
          padx=15, pady=8, command=add_expense).pack(side=tk.LEFT, padx=4)

tk.Button(btn_frame, text="🗑️ Delete Selected", font=("Arial", 11, "bold"),
          bg="#ef4444", fg="white", relief=tk.FLAT, cursor="hand2",
          padx=15, pady=8, command=delete_expense).pack(side=tk.LEFT, padx=4)

tk.Button(btn_frame, text="🧹 Clear All", font=("Arial", 11, "bold"),
          bg="#f59e0b", fg="white", relief=tk.FLAT, cursor="hand2",
          padx=15, pady=8, command=clear_all).pack(side=tk.LEFT, padx=4)

# Table
table_frame = tk.Frame(window, bg="#0f172a")
table_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))

columns = ("Date", "Description", "Category", "Amount")
table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#1e293b", foreground="white",
                fieldbackground="#1e293b", font=("Arial", 10), rowheight=28)
style.configure("Treeview.Heading", background="#10b981", foreground="white",
                font=("Arial", 10, "bold"))
table.tag_configure("odd", background="#1e293b")
table.tag_configure("even", background="#162032")

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=140, anchor="center")

scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=table.yview)
table.configure(yscrollcommand=scrollbar.set)
table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Summary
summary_frame = tk.Frame(window, bg="#1e293b", padx=15, pady=10)
summary_frame.pack(fill=tk.X, padx=15, pady=(0, 10))

total_label = tk.Label(summary_frame, text="💰 Total Spent: ₹0.00",
                       font=("Arial", 13, "bold"), bg="#1e293b", fg="#10b981")
total_label.pack(anchor="w")

category_label = tk.Label(summary_frame, text="No expenses yet!",
                           font=("Arial", 10), bg="#1e293b", fg="#94a3b8",
                           justify=tk.LEFT)
category_label.pack(anchor="w")

# Footer
tk.Label(window, text="💾 Data saved automatically!",
         font=("Arial", 9), bg="#0f172a", fg="#475569").pack(pady=(0, 8))

refresh_table()
update_summary()
window.mainloop()
