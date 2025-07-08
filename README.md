# Python Online Restaurant Ordering System

This project is an online restaurant ordering system developed as part of **ITSC 3155 – Software Engineering** at UNC Charlotte in Fall 2024.

It allows customers to browse menus, place orders, and manage their carts. It also includes admin features for managing restaurant data.

---

## Features

- User registration and login
- Menu browsing
- Online order placement
- Cart management
- Admin dashboard for managing menu items
- API documentation with Swagger UI

---

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- MySQL / MariaDB (via PyMySQL)
- Uvicorn (server)
- Pytest (testing)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/DivineMobote/Python_Online_Restaurant_Ordering_System.git
cd Python_Online_Restaurant_Ordering_System

---

## Installing Necessary Packages:  
* `pip install fastapi`
* `pip install "uvicorn[standard]"`  
* `pip install sqlalchemy`  
* `pip install pymysql`
* `pip install pytest`
* `pip install pytest-mock`
* `pip install httpx`
* `pip install cryptography`
Or install from requirements.txt if available: pip install -r requirements.txt

---

## Run The Server:
`uvicorn api.main:app --port 8000 --reload`
### Test API by built-in docs:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)#

---

## Security note:
 Database passwords and sensitive information have been removed from the repository for security purposes. Please update configuration files with your own credentials to run the project locally.

---

## Demo Video:
Download and unzip the demo folder to view demonstration presentation.

---

## Project Information:
* Course: ITSC 3155 - Software Engineering
* Semster: Fall 2024
* Team Members: Alejandro Murillo, Ayden Hocking, Deeksha Marpadaga, Shyam Pedibhotla



