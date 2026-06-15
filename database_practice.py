import sqlite3

# 1. Connect to a local test database file (creates it automatically)
connection = sqlite3.connect("company_ledger.db")
cursor = connection.cursor()

# 2. SQL Command: Create the INVOICES database table
cursor.execute("""
CREATE TABLE IF NOT EXISTS INVOICES (
    ClientID INTEGER PRIMARY KEY AUTOINCREMENT,
    ClientName TEXT,
    InvoiceAmount REAL,
    PaymentStatus TEXT,
    InvoiceDate TEXT
);
""")

# 3. SQL Command: Clear old mock data and insert fresh accounting records
cursor.execute("DELETE FROM INVOICES;")
mock_data = [
    ("Acme Corporate Solutions", 4500.00, "Unpaid", "2026-06-01"),
    ("Global Logistics Inc", 1200.50, "Paid", "2026-06-05"),
    ("Midwest Retail Partners", 3200.00, "Unpaid", "2026-06-10"),
    ("TechStart Ventures", 950.00, "Unpaid", "2026-06-12"),
    ("Summit Hospitality Group", 7800.00, "Paid", "2026-06-14")
]
cursor.executemany("INSERT INTO INVOICES (ClientName, InvoiceAmount, PaymentStatus, InvoiceDate) VALUES (?, ?, ?, ?);", mock_data)
connection.commit()

# ==========================================
# 4. YOUR TASK: Write the SQL query to find high-value unpaid balances
# ==========================================
sql_query = """
SELECT ClientName, InvoiceAmount, InvoiceDate
FROM INVOICES
WHERE PaymentStatus = 'Unpaid' 
  AND InvoiceAmount >= 2500.00
ORDER BY InvoiceAmount DESC;
"""

# Execute your SQL script and print the filtered spreadsheet rows
cursor.execute(sql_query)
results = cursor.fetchall()

print("\n--- HIGH-VALUE OUTSTANDING INVOICES REPORT ---")
print(f"{'Client Name':<30} | {'Amount':<10} | {'Invoice Date'}")
print("-" * 60)
for row in results:
    print(f"{row[0]:<30} | ${row[1]:<9.2f} | {row[2]}")
print("----------------------------------------------\n")

connection.close()
