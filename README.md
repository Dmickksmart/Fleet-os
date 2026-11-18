# FleetOS

FleetOS is a desktop app for fleet and vehicle rentals. Records are stored in a local SQLite database.

## Requirements

- Python 3.12 or newer
- The packages in `requirements.txt`

SQLite is included with Python.

## Setup

Open a terminal in this folder and run:

```
python -m pip install -r requirements.txt
python main.py
```

The first run creates `fleetos.db` in this folder.

## Login

The login screen keeps this account available:

- Username: `admin`
- Password: `admin123`

## Screens

- **Dashboard** shows how many vehicles, customers, bookings, and payments are stored.
- **Vehicles**, **Customers**, **Bookings**, and **Payments** each have Add, Edit, and Delete.
- Add and Edit open one form. Delete asks you to confirm.
- Bookings and payments link a customer and a vehicle from dropdowns.
- Start date, end date, and payment date are chosen from year, month, and day dropdowns.
- The amount is the vehicle daily rate multiplied by the booking length, including both dates.

## Layout

- `main.py` starts the app.
- `fleet/database.py` opens SQLite and creates missing tables.
- `fleet/models.py` defines the tables.
- `fleet/app.py` owns the window. `fleet/shell.py` is the sidebar.
- `fleet/auth.py` is the login screen. `fleet/dashboard.py` is the summary.
- `fleet/records.py` lists records. `fleet/form.py` is the add and edit form.
- `fleet/store.py` saves and deletes records.
