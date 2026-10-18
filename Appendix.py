# Exercise 1: Engineering Test Data Organizer[cite: 12]
last_name = "Magtalas"
seed_num = 6

test_records = [
    {"source": f"{last_name} T1", "category": "TEMPERATURE", "value": seed_num * 5},
    {"source": f"{last_name} T2", "category": "VOLTAGE", "value": seed_num * 10},
    {"source": f"{last_name} T3", "category": "CURRENT", "value": seed_num * 3},
    {"source": f"{last_name} T4", "category": "PRESSURE", "value": seed_num * 8},
    {"source": f"{last_name} T5", "category": "SPEED", "value": seed_num * 12},
    {"source": f"{last_name} T1", "category": "TEMPERATURE", "value": seed_num * 5} # Repeated record
]

print("=== Exercise 1 Output ===")
for record in test_records:
    print(record)


# Exercise 2: Student Performance Data Analyzer[cite: 13]
students = [f"{last_name} Student {i}" for i in range(1, 6)]
subjects = ["PROGRAMMING", "MATHEMATICS", "ELECTRONICS", "PHYSICS", "ENGLISH"]

performance_records = [
    {"student": students[0], "subject": subjects[0], "score": seed_num * 15},
    {"student": students[1], "subject": subjects[1], "score": seed_num * 14},
    {"student": students[2], "subject": subjects[2], "score": seed_num * 12},
    {"student": students[3], "subject": subjects[3], "score": None}, # Incomplete record
    {"student": students[0], "subject": subjects[0], "score": seed_num * 15} # Repeated record
]

print("\n=== Exercise 2 Output ===")
for record in performance_records:
    print(record)


# Exercise 3: Transaction History Analyzer[cite: 14]
customers = [f"{last_name} C{i}" for i in range(1, 6)]
product_prices = {"NOTEBOOK": 50, "PEN": 20, "USB": 300, "HEADPHONES": 500, "CALCULATOR": 750}

transactions = [
    {"customer": customers[0], "product": "NOTEBOOK", "quantity": seed_num},
    {"customer": customers[1], "product": "PEN", "quantity": seed_num * 2},
    {"customer": customers[2], "product": "USB", "quantity": 2},
    {"customer": customers[0], "product": "NOTEBOOK", "quantity": seed_num} # Repeated purchase
]

print("\n=== Exercise 3 Output ===")
for tx in transactions:
    tx["total_value"] = tx["quantity"] * product_prices[tx["product"]]
    print(tx)
