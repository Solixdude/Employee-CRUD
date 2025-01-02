This program implements a CRUD (Create, Read, Update, Delete) application using Tkinter for the graphical interface and MySQL for data storage. The application manages employee information, allowing users to insert, update, fetch, and delete data.
Key Features

    Insert:
        Adds a new employee to the database.
        All fields (ID, Name, Department) are mandatory.
        Displays a warning if any field is left empty.

    Update:
        Updates the details of an existing employee in the database.
        Requires all fields to be filled for successful processing.

    Fetch Data:
        Retrieves and displays the details of an employee based on their ID.
        Shows a notification if the ID is not found.

    Delete:
        Deletes an employee from the database based on their ID.
        Ensures a warning is displayed if the field is left empty.

    Reset Fields:
        Clears all input fields in the application.

    Show Employees:
        Displays a list of all employees in the database using a Listbox widget.
