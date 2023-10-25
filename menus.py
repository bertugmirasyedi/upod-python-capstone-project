import os
from datetime import datetime
from simple_term_menu import TerminalMenu
from contact_list import ContactList


class SortContactsMenu(TerminalMenu):
    OPTIONS = [
        "Sort by Name",
        "Sort by Surname",
        "Sort by Date Created",
        "Sort by Date Updated",
        "Back",
    ]
    TITLE = "\nBy which do you want to sort the list?\n"

    def __init__(self):
        super().__init__(
            menu_entries=SortContactsMenu.OPTIONS, title=SortContactsMenu.TITLE
        )
        self.contact_list_client = ContactList()

    def show(self):
        menu_entry_index = super().show()

        if menu_entry_index == 0:
            sort_by = "name"
        elif menu_entry_index == 1:
            sort_by = "surname"
        elif menu_entry_index == 2:
            sort_by = "date_created"
        elif menu_entry_index == 3:
            sort_by = "date_updated"
        elif menu_entry_index == 4:
            ListContactsMenu().show(run_first_time=False)

        self.contact_list_client.sort_contacts(sort_by)

        SortContactsMenu().show()


class ListContactsMenu(TerminalMenu):
    OPTIONS = ["Sort", "Search", "Back"]
    TITLE = "\nList Submenu: Please select the task\n"
    WORKING_DIRECTORY = os.getcwd()

    def __init__(self):
        super().__init__(
            menu_entries=ListContactsMenu.OPTIONS, title=ListContactsMenu.TITLE
        )
        self.contact_list_client = ContactList()

    def is_list_empty(self):
        if (
            os.stat(
                ListContactsMenu.WORKING_DIRECTORY + "/csv/contact_list.csv"
            ).st_size
            == 0
        ):
            return True
        else:
            return False

    def show(self, run_first_time=True):
        if self.is_list_empty() is False:
            if run_first_time:
                # List the contacts
                self.contact_list_client.list_contacts()

            # Get the selected menu entry index
            menu_entry_index = super().show()

            if menu_entry_index == 0:
                SortContactsMenu().show()

            elif menu_entry_index == 1:
                query = input("\nPlease enter the query you want to search: ")
                self.contact_list_client.search_contacts(query)

                ListContactsMenu().show(run_first_time=False)
            elif menu_entry_index == 2:
                MainMenu().show()
        else:
            print("\nThere is no contact to list!")
            MainMenu().show()


# Create a class for the main menu
class MainMenu(TerminalMenu):
    OPTIONS = [
        "Add Contact",
        "Remove Contact",
        "Edit Contact",
        "List Contacts",
        "Restore Contacts",
        "Exit",
    ]
    TITLE = "\nContact List: Please select the task\n"

    def __init__(self):
        super().__init__(menu_entries=MainMenu.OPTIONS, title=MainMenu.TITLE)
        self.contact_list_client = ContactList()

    def input_with_checks(self, column):
        if column == "phone_number":
            while True:
                try:
                    return int(
                        input(f"\nPlease enter the phone number of the contact: ")
                    )
                except ValueError:
                    print("Please enter a valid phone number!")
        elif column == "vip":
            while True:
                value = input(
                    f"\nPlease enter whether the contact is VIP (True / False): "
                )
                if value.lower() not in ["true", "false"]:
                    print("Please enter a valid value!")
                else:
                    return value.title()
        elif column == "email":
            while True:
                value = input(f"\nPlease enter the email of the contact: ")
                if "@" not in value:
                    print("Please enter a valid email!")
                else:
                    return value
        else:
            while True:
                value = input(f"\nPlease enter the {column} of the contact: ")
                if value.isalpha():
                    return value
                else:
                    print(f"Please enter a valid {column}!")

    def show(self):
        menu_entry_index = super().show()

        # Implement the add contact method
        if menu_entry_index == 0:
            contact_name = self.input_with_checks("name")
            contact_surname = self.input_with_checks("surname")
            contact_phone_number = self.input_with_checks("phone_number")
            contact_email = self.input_with_checks("email")
            contact_vip = self.input_with_checks("vip")

            last_id = self.contact_list_client.get_last_id()

            self.contact_list_client.add_contact(
                dict(
                    id=last_id + 1,
                    name=contact_name,
                    surname=contact_surname,
                    phone_number=contact_phone_number,
                    email=contact_email,
                    vip=contact_vip,
                    date_created=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    date_updated=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                )
            )

            MainMenu().show()

        # Implement the remove contact method
        elif menu_entry_index == 1:
            # Get the ids of contacts to be removed
            id_list = input(
                "\nPlease enter the IDs of the contacts you want to remove (separated by spaces): "
            ).split()

            # Convert the ids to int
            id_list = [int(id) for id in id_list]

            # Remove them from the contact list
            self.contact_list_client.remove_contact(id_list)

            # Show the menu again
            MainMenu().show()

        # Implement the edit contact method
        elif menu_entry_index == 2:
            # Get the id of the contact to be edited
            id = int(input("\nPlease enter the ID of the contact you want to edit: "))

            # Get the new contact information
            contact_name = self.input_with_checks("name")
            contact_surname = self.input_with_checks("surname")
            contact_phone_number = int(self.input_with_checks("phone_number"))
            contact_email = self.input_with_checks("email")
            contact_vip = self.input_with_checks("vip")

            self.contact_list_client.edit_contact(
                id,
                dict(
                    name=contact_name,
                    surname=contact_surname,
                    phone_number=contact_phone_number,
                    email=contact_email,
                    vip=contact_vip,
                    date_updated=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                ),
            )

            # Show the menu again
            MainMenu().show()

        # Implement the list contacts method
        elif menu_entry_index == 3:
            ListContactsMenu().show(run_first_time=True)

        # Implement the restore contacts method
        elif menu_entry_index == 4:
            self.contact_list_client.restore_from_backup_database()
            MainMenu().show()

        # Implement the exit method
        elif menu_entry_index == 5:
            exit()
