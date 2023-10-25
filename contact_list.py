import os
import csv
import json
import sqlite3
from tabulate import tabulate


class ContactList:
    def __init__(self):
        self.contact_list = list()

    # Method to get the number of contacts in the contact list
    def get_last_id(self):
        # Get the working directory
        working_dir = os.getcwd()

        # Check whether the "contact_list.csv" exists and get the last id from there
        if os.path.exists(working_dir + "/csv/contact_list.csv"):
            # Open the csv file
            with open(working_dir + "/csv/contact_list.csv", "r") as file:
                # Create the csv reader object
                reader = csv.reader(file)

                # Get rows in the csv file
                rows = list(reader)

                # Get the id of last contact
                last_id = int(rows[-1][0])

            return last_id
        else:
            return 0

    # Method to export contact list to CSV database
    def export_to_csv(self):
        """
        Exports the contact list to a CSV file.

        If the "contact_list.csv" file does not exist, it creates a new one and writes the header row and data to it.
        If the file already exists, it appends the data to the existing file.

        Returns:
            None
        """
        # Get the current working directory
        working_dir = os.getcwd()

        # Check whether the "contact_list.csv" exists
        if not os.path.exists(working_dir + "/csv/contact_list.csv"):
            print("CSV database cannot be found. Creating a new one...")

            if not os.path.exists(working_dir + "/csv"):
                # Create the "csv" folder if it does not exist
                os.mkdir(working_dir + "/csv")

            # If the file does not exist then we are creating the database for the first time
            with open(working_dir + "/csv/contact_list.csv", "w") as file:
                # Create the csv writer object
                writer = csv.writer(file)

                # Create the header row
                writer.writerow(
                    [
                        "ID",
                        "Name",
                        "Surname",
                        "Phone Number",
                        "Email",
                        "VIP",
                        "Date Created",
                        "Date Updated",
                    ]
                )

                # Write the data to the csv file
                for contact in self.contact_list:
                    writer.writerow(
                        [
                            contact.get("id", None),
                            contact.get("name", None),
                            contact.get("surname", None),
                            contact.get("phone_number", None),
                            contact.get("email", None),
                            contact.get("vip", None),
                            contact.get("date_created", None),
                            contact.get("date_updated", None),
                        ]
                    )

                print("CSV database created successfully!")
        else:
            print("CSV database found. Updating...")

            # If there is already a csv file then we are updating the database
            with open(working_dir + "/csv/contact_list.csv", "a") as file:
                # Create the csv writer object
                writer = csv.writer(file)

                # Write the data to the csv file
                for contact in self.contact_list:
                    writer.writerow(
                        [
                            contact.get("id", None),
                            contact.get("name", None),
                            contact.get("surname", None),
                            contact.get("phone_number", None),
                            contact.get("email", None),
                            contact.get("vip", None),
                            contact.get("date_created", None),
                            contact.get("date_updated", None),
                        ]
                    )

                print("CSV database updated successfully!")

    # Method to delete a list of contacts from the CSV database
    def remove_from_csv(self, id_list: list):
        # Get the current working directory
        working_dir = os.getcwd()

        # Open the database and remove the selected contacts
        with open(working_dir + "/csv/contact_list.csv", "r") as file:
            # Create the csv reader object
            reader = csv.reader(file)

            # Get the rows of the csv file
            rows = list(reader)

        file.close()

        # Remove the header row
        header_row = rows.pop(0)

        # Remove the selected contacts
        for row in rows:
            if int(row[0]) in id_list:
                rows.remove(row)

        # Write the data to the csv file
        with open(working_dir + "/csv/contact_list.csv", "w") as file:
            writer = csv.writer(file)

            writer.writerow(header_row)
            writer.writerows(rows)

        print("CSV database updated successfully!")

    # Method to export contact list to JSON database
    def export_to_json(self):
        # Get the current working directory
        working_dir = os.getcwd()

        # Check whether the "contact_list.json" exists
        if not os.path.exists(working_dir + "/json/contact_list.json"):
            print("JSON database cannot be found. Creating a new one...")

            if not os.path.exists(working_dir + "/json"):
                # Create the "json" folder if it does not exist
                os.mkdir(working_dir + "/json")

            # If the file does not exist then we are creating the database for the first time
            with open(working_dir + "/json/contact_list.json", "w") as file:
                # Write the data to the json file
                json.dump(self.contact_list, file)

                print("JSON database created successfully!")
        else:
            print("JSON database found. Updating...")

            # If there is already a json file then we are updating the database
            with open(working_dir + "/json/contact_list.json", "r") as file:
                # Load the json file
                data = json.load(file)

            file.close()

            # Add the new contact list to the json file
            for contact in self.contact_list:
                data.append(contact)

            # Write the data to the json file
            with open(working_dir + "/json/contact_list.json", "w") as file:
                json.dump(data, file)

            print("JSON database updated successfully!")

    # Method to delete a list of contacts from the JSON database
    def remove_from_json(self, id_list: list):
        # Get the current working directory
        working_dir = os.getcwd()

        # Open the database and remove the selected contacts
        with open(working_dir + "/json/contact_list.json", "r") as file:
            # Load the json file
            data = json.load(file)

        file.close()

        # Remove the selected contacts
        for contact in data:
            if contact["id"] in id_list:
                data.remove(contact)

        # Write the data to the json file
        with open(working_dir + "/json/contact_list.json", "w") as file:
            json.dump(data, file)

        print("JSON database updated successfully!")

    # Method to export the contact list to a ismetify database
    def export_to_ismetify(self):
        # Get the current working directory
        working_dir = os.getcwd()

        # Check whether the "contact_list.ismetify" exists
        if not os.path.exists(working_dir + "/ismetify/contact_list.ismetify"):
            print("ismetify database cannot be found. Creating a new one...")

            if not os.path.exists(working_dir + "/ismetify"):
                # Create the "ismetify" folder if it does not exist
                os.mkdir(working_dir + "/ismetify")

            # If the file does not exist then we are creating the database for the first time
            with open(working_dir + "/ismetify/contact_list.ismetify", "w") as file:
                # Create the header row
                file.write(
                    "ID | Name | Surname | Phone Number | Email | VIP | Date Created | Date Updated\n"
                )

                # Write the data to the ismetify file
                for contact in self.contact_list:
                    id = contact.get("id", None)
                    name = contact.get("name", None)
                    surname = contact.get("surname", None)
                    phone_number = contact.get("phone_number", None)
                    email = contact.get("email", None)
                    vip = contact.get("vip", None)
                    date_created = contact.get("date_created", None)
                    date_updated = contact.get("date_updated", None)

                    file.write(
                        f"{id} | {name} | {surname} | {phone_number} | {email} | {vip} | {date_created} | {date_updated}\n"
                    )

                print("ismetify database created successfully!")
        else:
            print("ismetify database found. Updating...")

            # If there is already a ismetify file then we are updating the database
            with open(working_dir + "/ismetify/contact_list.ismetify", "a+") as file:
                # Write the data to the ismetify file
                for contact in self.contact_list:
                    id = contact.get("id", None)
                    name = contact.get("name", None)
                    surname = contact.get("surname", None)
                    phone_number = contact.get("phone_number", None)
                    email = contact.get("email", None)
                    vip = contact.get("vip", None)
                    date_created = contact.get("date_created", None)
                    date_updated = contact.get("date_updated", None)

                    file.write(
                        f"{id} | {name} | {surname} | {phone_number} | {email} | {vip} | {date_created} | {date_updated}\n"
                    )

                print("ismetify database updated successfully!")

    # Method to delete a list of contacts from the ismetify database
    def remove_from_ismetify(self, id_list: list):
        # Get the current working directory
        working_dir = os.getcwd()

        # Open the database and remove the selected contacts
        with open(working_dir + "/ismetify/contact_list.ismetify", "r") as file:
            # Get the rows of the ismetify file
            rows = file.readlines()

        # Close the file
        file.close()

        # Remove the header row
        header_row = rows.pop(0)

        # Remove the selected contacts
        for row in rows:
            if int(row.split(" | ")[0]) in id_list:
                rows.remove(row)

        # Write the data to the ismetify file
        with open(working_dir + "/ismetify/contact_list.ismetify", "w") as file:
            file.write(header_row)
            file.writelines(rows)

        print("ismetify database updated successfully!")

    # Method to export the contact list to SQLite database
    def export_to_sqlite(self):
        # Get the current working directory
        working_dir = os.getcwd()

        # Check whether the "contact_list.db" exists
        if not os.path.exists(working_dir + "/sql/contact_list.sqlite3"):
            print("SQLite database cannot be found. Creating a new one...")

            if not os.path.exists(working_dir + "/sql"):
                # Create the "sql" folder if it does not exist
                os.mkdir(working_dir + "/sql")

            # Connect to the database
            connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

            # Create the cursor
            cursor = connection.cursor()

            # Create the table
            cursor.execute(
                """
                CREATE TABLE contact_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    surname VARCHAR(50),
                    phone_number BIGINT,
                    email VARCHAR(75),
                    vip BOOLEAN,
                    date_created DATE,
                    date_updated DATE
                )
                """
            )

            # Add the data to the table
            for contact in self.contact_list:
                name = contact.get("name", None)
                surname = contact.get("surname", None)
                phone_number = contact.get("phone_number", None)
                email = contact.get("email", None)
                vip = contact.get("vip", None)
                date_created = contact.get("date_created", None)
                date_updated = contact.get("date_updated", None)

                cursor.execute(
                    f"""
                    INSERT INTO contact_list (name, surname, phone_number, email, vip, date_created, date_updated)
                    VALUES ('{name}', '{surname}', {phone_number}, '{email}', {vip}, '{date_created}', '{date_updated}')
                    """
                )

            # Commit the changes
            connection.commit()

            # Close the connection
            connection.close()

            print("SQLite database created successfully!\n")
        else:
            print("SQLite database found. Updating...")

            # Connect to the database
            connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

            # Create the cursor
            cursor = connection.cursor()

            # Add the data to the table
            for contact in self.contact_list:
                name = contact.get("name", None)
                surname = contact.get("surname", None)
                phone_number = contact.get("phone_number", None)
                email = contact.get("email", None)
                vip = contact.get("vip", None)
                date_created = contact.get("date_created", None)
                date_updated = contact.get("date_updated", None)

                cursor.execute(
                    f"""
                    INSERT INTO contact_list (name, surname, phone_number, email, vip, date_created, date_updated)
                    VALUES ('{name}', '{surname}', {phone_number}, '{email}', {vip}, '{date_created}', '{date_updated}')
                    """
                )

            # Commit the changes
            connection.commit()

            # Close the connection
            connection.close()

            print("SQLite database updated successfully!\n")

    # Method to delete a list of contacts from the SQLite database
    def remove_from_sqlite(self, id_list: list):
        # Get the current working directory
        working_dir = os.getcwd()

        # Connect to the database
        connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

        # Create the cursor
        cursor = connection.cursor()

        # Remove the selected contacts
        for id in id_list:
            cursor.execute(f"DELETE FROM contact_list WHERE id = {id}")

        # Commit the changes
        connection.commit()

        # Close the connection
        connection.close()

        print("SQLite database updated successfully!")

    # Method to add a contact to the contact list
    def add_contact(self, contact: dict):
        # Add the contact to the contact list
        self.contact_list.append(contact)

        # Export the contact list to the databases
        self.export_to_csv()
        self.export_to_json()
        self.export_to_ismetify()
        self.export_to_sqlite()

        # Empty the contact list
        self.contact_list = list()

    # Method to remove a contact from the databases
    def remove_contact(self, id_list: list):
        # Remove the contact from the databases
        self.remove_from_csv(id_list)
        self.remove_from_json(id_list)
        self.remove_from_ismetify(id_list)
        self.remove_from_sqlite(id_list)

    # Method to print the contact list in a table format
    def list_contacts(self):
        # Get the working directory
        working_dir = os.getcwd()

        with open(working_dir + "/csv/contact_list.csv", "r") as file:
            reader = csv.reader(file)

            print("\n")
            print(tabulate(reader, headers="firstrow", tablefmt="fancy_grid"))

    # Method to edit a contact
    def edit_contact(self, id: int, new_contact: dict):
        # Get the working directory
        working_dir = os.getcwd()

        ### Edit the contact in the CSV database
        with open(working_dir + "/csv/contact_list.csv", "r") as file:
            # Get the rows of the csv file
            rows = list(csv.reader(file))

            # Get the header row
            header_row = rows.pop(0)

        file.close()

        with open(working_dir + "/csv/contact_list.csv", "w") as file:
            # Create the csv writer object
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(header_row)

            # Write the data to the csv file
            for row in rows:
                if int(row[0]) == id:
                    writer.writerow(
                        [
                            id,
                            new_contact.get("name", None),
                            new_contact.get("surname", None),
                            new_contact.get("phone_number", None),
                            new_contact.get("email", None),
                            new_contact.get("vip", None),
                            row[6],
                            new_contact.get("date_updated", None),
                        ]
                    )
                else:
                    writer.writerow(row)

        file.close()

        ### Edit the contact in the JSON database
        with open(working_dir + "/json/contact_list.json", "r") as file:
            # Load the json file
            data = json.load(file)

        file.close()

        with open(working_dir + "/json/contact_list.json", "w") as file:
            # Write the data to the json file
            for contact in data:
                if contact["id"] == id:
                    contact["name"] = new_contact.get("name", None)
                    contact["surname"] = new_contact.get("surname", None)
                    contact["phone_number"] = new_contact.get("phone_number", None)
                    contact["email"] = new_contact.get("email", None)
                    contact["vip"] = new_contact.get("vip", None)
                    contact["date_updated"] = new_contact.get("date_updated", None)

            json.dump(data, file)

        file.close()

        ### Edit the contact in the ismetify database
        with open(working_dir + "/ismetify/contact_list.ismetify", "r") as file:
            # Get the rows of the ismetify file
            rows = file.readlines()

            # Get the header row
            header_row = rows.pop(0)

        file.close()

        with open(working_dir + "/ismetify/contact_list.ismetify", "w") as file:
            # Write the header row
            file.write(header_row)

            # Write the data to the ismetify file
            for row in rows:
                if int(row.split(" | ")[0]) == id:
                    # Get the creation date of the contact
                    date_created = row.split(" | ")[6]

                    file.write(
                        f"{id} | {new_contact.get('name', None)} | {new_contact.get('surname', None)} | {new_contact.get('phone_number', None)} | {new_contact.get('email', None)} | {new_contact.get('vip', None)} | {date_created} | {new_contact.get('date_updated', None)}\n"
                    )
                else:
                    file.write(row)

        file.close()

        ### Edit the contact in the SQLite database
        # Connect to the database
        connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

        # Create the cursor
        cursor = connection.cursor()

        # Edit the contact
        cursor.execute(
            f"""
            UPDATE contact_list
            SET name = '{new_contact.get('name', None)}',
                surname = '{new_contact.get('surname', None)}',
                phone_number = {new_contact.get('phone_number', None)},
                email = '{new_contact.get('email', None)}',
                vip = {new_contact.get('vip', None)},
                date_updated = '{new_contact.get('date_updated', None)}'
            WHERE id = {id}
            """
        )

        # Commit the changes
        connection.commit()

        # Close the connection
        connection.close()

        print("\nContact updated successfully on all databases!")

    # Method to sort the contact list
    def sort_contacts(self, by: str):
        # Get the working directory
        working_dir = os.getcwd()

        # Open the csv file
        with open(working_dir + "/csv/contact_list.csv", "r") as file:
            # Create the csv reader object
            reader = csv.reader(file)

            # Get the rows of the csv file
            rows = list(reader)

            # Remove the header row
            header_row = rows.pop(0)

            if by == "name":
                sorted_rows = sorted(rows, key=lambda row: row[1])
            elif by == "surname":
                sorted_rows = sorted(rows, key=lambda row: row[2])
            elif by == "date_created":
                sorted_rows = sorted(rows, key=lambda row: row[6])
            elif by == "date_updated":
                sorted_rows = sorted(rows, key=lambda row: row[7])

        file.close()

        print("\n")
        print(tabulate(sorted_rows, headers=header_row, tablefmt="fancy_grid"))

    # Method to search the contact list
    def search_contacts(self, query: str):
        # Get the working directory
        working_dir = os.getcwd()

        # To make the search case insensitive we convert the query to lowercase
        query = query.lower()

        ### Make the search in the SQLite database
        # Connect to the database
        connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

        # Create the cursor
        cursor = connection.cursor()

        # Search the database
        cursor.execute(
            f"""
            SELECT * FROM contact_list
            WHERE name LIKE '%{query}%' OR surname LIKE '%{query}%' OR email LIKE '%{query}%'
            """
        )

        # Get the results
        results = cursor.fetchall()

        # Close the connection
        connection.close()

        # Print the results if there are any otherwise print a message
        if len(results) > 0:
            print("\n")
            print(
                tabulate(
                    results,
                    headers=[
                        "ID",
                        "Name",
                        "Surname",
                        "Phone Number",
                        "Email",
                        "VIP",
                        "Date Created",
                        "Date Updated",
                    ],
                    tablefmt="fancy_grid",
                )
            )

            return 1

        ### Make the search in the CSV database
        print(
            "\nNo results found in the SQLite database. Searching in the CSV database..."
        )

        # Open the csv file
        with open(working_dir + "/csv/contact_list.csv", "r") as file:
            # Create the csv reader object
            reader = csv.reader(file)

            # Get the rows of the csv file
            rows = list(reader)

            # Remove the header row
            header_row = rows.pop(0)

            # Search the csv file
            results = list()

            for row in rows:
                if (
                    query in row[1].lower()
                    or query in row[2].lower()
                    or query in row[4].lower()
                ):
                    results.append(row)

        file.close()

        # Print the results if there are any otherwise print a message
        if len(results) > 0:
            print("\n")
            print(
                tabulate(
                    results,
                    headers=header_row,
                    tablefmt="fancy_grid",
                )
            )

            return 1

        ### Make the search in the JSON database
        print(
            "\nNo results found in the CSV database. Searching in the JSON database..."
        )

        # Open the json file
        with open(working_dir + "/json/contact_list.json", "r") as file:
            # Load the json file
            data = json.load(file)

            # Search the json file
            results = list()

            for contact in data:
                if (
                    query in contact["name"].lower()
                    or query in contact["surname"].lower()
                    or query in contact["email"].lower()
                ):
                    results.append(contact)

        file.close()

        # Print the results if there are any otherwise print a message
        if len(results) > 0:
            print("\n")
            print(
                tabulate(
                    results,
                    headers=[
                        "ID",
                        "Name",
                        "Surname",
                        "Phone Number",
                        "Email",
                        "VIP",
                        "Date Created",
                        "Date Updated",
                    ],
                    tablefmt="fancy_grid",
                )
            )

            return 1

        ### Make the search in the ismetify database
        print(
            "\nNo results found in the JSON database. Searching in the ismetify database..."
        )

        # Open the ismetify file
        with open(working_dir + "/ismetify/contact_list.ismetify", "r") as file:
            # Get the rows of the ismetify file
            rows = file.readlines()

            # Remove the header row
            header_row = rows.pop(0)

            # Search the ismetify file
            results = list()

            # Define a function to select the column to improve readability
            def get_ismetify_column(row, index):
                return row.split(" | ")[index].lower()

            for row in rows:
                if (
                    query in get_ismetify_column(row, 1)
                    or query in get_ismetify_column(row, 2)
                    or query in get_ismetify_column(row, 4)
                ):
                    results.append(row)

        file.close()

        # Print the results if there are any otherwise print a message
        if len(results) > 0:
            print("\n")
            print(
                tabulate(
                    results,
                    headers=header_row.split(" | "),
                    tablefmt="fancy_grid",
                )
            )

            return 1

        print(
            "\nNo results found in the ismetify database. The contact does not exist in all of the databases!"
        )

        return 0

    def restore_from_backup_database(self):
        """
        A method to check all unique contacts in all of the databases and create new ones with all of the unique contacts.
        """
        # Get the working directory
        working_dir = os.getcwd()

        # Create an empty list to store the unique contacts
        unique_contacts = list()

        ### Check the CSV database
        try:
            # Open the csv file
            with open(working_dir + "/csv/contact_list.csv", "r") as file:
                # Create the csv reader object
                reader = csv.reader(file)

                # Get the rows of the csv file
                rows = list(reader)

                # Remove the header row
                csv_header_row = rows.pop(0)

                # Add the rows from the CSV file to the unique contacts list
                # At the last row, remove the "\n" from the "Date Updated" column
                for row in rows:
                    unique_contacts.append(
                        dict(
                            id=row[0],
                            name=row[1],
                            surname=row[2],
                            phone_number=row[3],
                            email=row[4],
                            vip=row[5],
                            date_created=row[6],
                            date_updated=row[7]
                            if row != rows[-1]
                            else row[7].replace("\n", ""),
                        )
                    )
        except:
            pass

        ### Check the JSON database
        try:
            # Open the json file
            with open(working_dir + "/json/contact_list.json", "r") as file:
                # Load the json file
                data = json.load(file)

                # Add the contacts from the JSON file to the unique contacts list
                for contact in data:
                    if contact not in unique_contacts:
                        unique_contacts.append(contact)
        except:
            pass

        ### Check the ismetify database
        try:
            # Open the ismetify file
            with open(working_dir + "/ismetify/contact_list.ismetify", "r") as file:
                # Get the rows of the ismetify file
                rows = file.readlines()

                # Remove the header row
                ismetify_header_row = rows.pop(0)

                # Add the rows from the ismetify file to the unique contacts list
                # At the last row, remove the "\n" from the "Date Updated" column
                for row in rows:
                    dict_row = dict(
                        id=row.split(" | ")[0],
                        name=row.split(" | ")[1],
                        surname=row.split(" | ")[2],
                        phone_number=row.split(" | ")[3],
                        email=row.split(" | ")[4],
                        vip=row.split(" | ")[5],
                        date_created=row.split(" | ")[6],
                        date_updated=row.split(" | ")[7]
                        if row != rows[-1]
                        else row.split(" | ")[7].replace("\n", ""),
                    )

                    if dict_row not in unique_contacts:
                        unique_contacts.append(dict_row)
        except:
            pass

        ### Check the SQLite database
        try:
            # Connect to the database
            connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

            # Create the cursor
            cursor = connection.cursor()

            # Get the contacts from the database
            cursor.execute("SELECT * FROM contact_list")

            # Get the results
            rows = cursor.fetchall()

            # Close the connection
            connection.close()

            # Add the contacts from the SQLite database to the unique contacts list
            for row in rows:
                # Convert the row to a dictionary
                dict_row = dict(
                    id=row[0],
                    name=row[1],
                    surname=row[2],
                    phone_number=row[3],
                    email=row[4],
                    vip=row[5],
                    date_created=row[6],
                    date_updated=row[7],
                )

                if dict_row not in unique_contacts:
                    unique_contacts.append(dict_row)
        except:
            pass

        print("Current unique contacts: ", unique_contacts)

        # Recreate all of the databases with the unique contacts
        ### CSV database
        with open(working_dir + "/csv/contact_list.csv", "w") as file:
            # Create the writer object
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(
                [
                    "ID",
                    "Name",
                    "Surname",
                    "Phone Number",
                    "Email",
                    "VIP",
                    "Date Created",
                    "Date Updated",
                ]
            )

            # Write the data to the csv file
            for contact in unique_contacts:
                writer.writerow(
                    [
                        contact.get("id", None),
                        contact.get("name", None),
                        contact.get("surname", None),
                        contact.get("phone_number", None),
                        contact.get("email", None),
                        contact.get("vip", None),
                        contact.get("date_created", None),
                        contact.get("date_updated", None),
                    ]
                )

        ### JSON database
        with open(working_dir + "/json/contact_list.json", "w") as file:
            # Write the data to the json file
            json.dump(unique_contacts, file)

        ### ismetify database
        with open(working_dir + "/ismetify/contact_list.ismetify", "w") as file:
            # Write the header row
            file.write(
                "ID | Name | Surname | Phone Number | Email | VIP | Date Created | Date Updated\n"
            )

            # Write the data to the ismetify file
            for contact in unique_contacts:
                file.write(
                    f"{contact.get('id', None)} | {contact.get('name', None)} | {contact.get('surname', None)} | {contact.get('phone_number', None)} | {contact.get('email', None)} | {contact.get('vip', None)} | {contact.get('date_created', None)} | {contact.get('date_updated', None)}\n"
                )

        ### SQLite database
        # Connect to the database
        connection = sqlite3.connect(working_dir + "/sql/contact_list.sqlite3")

        # Create the cursor
        cursor = connection.cursor()

        # Delete the current table
        cursor.execute(
            """
            DROP TABLE IF EXISTS contact_list
            """
        )
        connection.commit()

        # Create the new table
        cursor.execute(
            """
                CREATE TABLE contact_list (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(50),
                    surname VARCHAR(50),
                    phone_number BIGINT,
                    email VARCHAR(75),
                    vip BOOLEAN,
                    date_created DATE,
                    date_updated DATE
                )
                """
        )
        connection.commit()

        # Add the contacts to the table
        for contact in unique_contacts:
            name = contact.get("name", None)
            surname = contact.get("surname", None)
            phone_number = contact.get("phone_number", None)
            email = contact.get("email", None)
            vip = contact.get("vip", None)
            date_created = contact.get("date_created", None)
            date_updated = contact.get("date_updated", None)

            cursor.execute(
                f"""
                    INSERT INTO contact_list (name, surname, phone_number, email, vip, date_created, date_updated)
                    VALUES ('{name}', '{surname}', {phone_number}, '{email}', {vip}, '{date_created}', '{date_updated}')
                    """
            )
        connection.commit()

        print("\nAll databases are restored!")
