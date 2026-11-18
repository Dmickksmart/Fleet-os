from fleet.dashboard import DashboardView
from fleet.vehicles import VehiclesView
from fleet.customers import CustomersView
from fleet.bookings import BookingsView
from fleet.payments import PaymentsView

PAGES = {
    "Dashboard": DashboardView,
    "Vehicles": VehiclesView,
    "Customers": CustomersView,
    "Bookings": BookingsView,
    "Payments": PaymentsView,
}
