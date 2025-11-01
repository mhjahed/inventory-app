📦 Inventory Management Web App

A complete web application for managing inventory, tracking items, expenses, revenue, customer purchases, and invoices. Built with Django, HTML, CSS, and JavaScript.

🌟 Features
Inventory & Items Tracking

Add, edit, and delete items

Track stock levels in real-time

Categorize items by type, brand, or supplier

Automated alerts for low stock

Customer Management

Add and manage customers

Track customer purchases and history

Generate customer-specific reports

Sales & Revenue Tracking

Record sales and automatically update inventory

Track daily, weekly, and monthly revenue

Expense tracking for purchases or operational costs

Generate revenue and expense reports

Invoice Management

Create invoices for each customer purchase

Save and print invoices in PDF format

Auto-fill invoice details from items and customers

Track outstanding payments

Synchronization & Automation

Real-time updates for inventory, sales, and invoices

Data consistency between items, stock levels, and customer purchases

🛠️ Technologies Used

Backend: Python, Django

Frontend: HTML5, CSS3, JavaScript

Database: SQLite / PostgreSQL

Libraries & Tools:

django-allauth for authentication

django-multiselectfield for item categories

django-js-asset for JS asset management

whitenoise for static files in production

📸 Screenshots

Dashboard / Items Tracker


Customer Purchase History


Invoice Creator


Revenue & Expense Tracker


🚀 Installation

Clone the repository

git clone https://github.com/yourusername/inventory-app.git
cd inventory-app


Create & activate virtual environment

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create superuser (optional)

python manage.py createsuperuser


Run the development server

python manage.py runserver


Open in browser

http://127.0.0.1:8000

🌐 Deployment

Can be deployed on Heroku, AWS, or VPS.

Uses Whitenoise for static files in production.

Fully production-ready with synchronized data management.

📂 Project Structure
inventory_app/
│
├── inventory/              # Django app
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, images
│   ├── models.py           # Items, customers, invoices
│   ├── views.py            # Application views
│   ├── urls.py             # App URLs
│   └── admin.py            # Admin configurations
│
├── .venv/                  # Python virtual environment
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies

⚙️ Notes

Tracks items, stock, sales, and expenses in real-time.

Invoice generator automatically updates inventory and customer purchase records.

Multi-user system with super admin and manager roles for better control.

Perfect for small businesses, retail shops, or warehouses.

💡 Future Enhancements

Email invoices to customers automatically

Barcode scanner integration for faster stock management

Analytics dashboard for sales trends, profit, and losses

Multi-warehouse support

📜 License

This project is licensed under MIT License.

🙌 Author

MH JAHED | https://github.com/mhjahed
