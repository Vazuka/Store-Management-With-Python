# Store-Management-With-Python

## Overview

The Store Management System is a Python-based application that allows you to efficiently manage a store's product inventory and sales records. This program is designed to help administrators add, search, update, and delete products, view sales data, and visualize profit trends. It also includes secure user authentication for admin access.

## Key Features

- **User Authentication:** Admins can securely log in with their usernames and passwords.
- **Product Management:** Easily add new products, search for existing ones, update details, or remove products from inventory.
- **Sales Records:** View sales data, including total profit, on a yearly or monthly basis.
- **Data Visualization:** Generate visual representations of yearly and monthly profit trends using Matplotlib.
- **Database Integration:** Utilizes MySQL for storing admin credentials, product information, and sales data.
- **Password Security:** Implements password hashing for secure storage of admin passwords.

## Prerequisites

Before running the Store Management System on your computer, ensure you have the following prerequisites installed:

- **Python:** You will need Python 3.x installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

- **MySQL Database:** Set up a MySQL database on your local machine or a remote server. Make sure you have the necessary credentials (host, username, password) and a database named `store_management`.

## Getting Started

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/store-management-system.git
    cd store-management-system
    ```

2. Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. Create the necessary tables in your MySQL database by running the `create_tables.sql` script provided in the repository:

    ```bash
    mysql -u your-mysql-username -p store_management < create_tables.sql
    ```

4. Configure Database Connection:
   
   Update the database connection details in the `initialize_db` function of the `store_management.py` script. Replace the default values with your own database credentials.

5. Run the program:

    ```bash
    python store_management.py
    ```

6. Follow the on-screen menu options to interact with the system. You can log in as an existing admin or create a new admin account.

## Usage

- **Admin Login:** Existing admins can log in with their username and password to access the admin menu.

- **Admin Menu:** In the admin menu, you can perform various tasks, including adding products, searching for products, updating product details, deleting products, checking sales status, and visualizing sales data.

- **Data Visualization:** The program allows you to visualize sales data on a yearly and monthly basis using Matplotlib.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository: `git push origin feature-name`
5. Create a Pull Request to the `main` branch of this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the Python and MySQL communities for their excellent documentation and support.

## Contact

If you have any questions or need further assistance, please feel free to contact us at [nikhilvishnoi23@gmail.com](mailto:nikhilvishnoi23@gmail.com).
