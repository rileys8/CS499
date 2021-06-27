

# Import CRUD module
from MongoDB_Modules import AnimalShelter
from datetime import datetime
import pprint

ans = ""
# Loop until exit.
while ans != 1:
    # Print menu options for the user to choose from.
    print("""
          Please enter an option below.

          1. Test connection
          2. Create new document
          3. Read document
          4. Update document
          5. Delete document
          6. Ages
          0. Exit
          """)
    # Request input from the user. This selection will determine what action the program takes.
    ans = (input("Enter option: ").lower())

    # If the user entered test or number 1, test the connection.
    if (ans == "test") or (ans == "test connection") or (ans == "1"):
        print("Test")
        # Exception below will catch error if AnimalShelter.test is not imported correctly.
        try:
            # This will test if the MongoDB_Module is correctly imported and also will test the connection to mongoDB.
            print(AnimalShelter.test())
        except:
            # If MongoDB_Module not correctly imported or not found, print an error.
            print("Error. MongoDB_Modules file not found.")

    # If the user entered create the number 2, create a new document.
    elif (ans == "create") or (ans == "create new document") or (ans == "create document") or (ans == "2"):
        print("Create a new document")
        i = 0
        # First loop to allow user to re-enter variables if needed.
        while i == 0:
            # Input variables below create the dictionary that will be passed into the create function.
            ID = input("Enter animal ID: ")
            Name = input("Enter name: ")
            DOB = input("Enter date of birth (mm/dd/yyyy): ")
            Outcome = input("Enter outcome type: ")
            AnimalType = input("Enter animal type: ")
            Sex = input("Enter sex and if fixed (Neutered Male): ")
            Age = input("Enter animal age: ")
            Breed = input("Enter animal breed: ")
            Color = input("Enter animal color: ")
            # Dictionary for the create function.
            my_dict = {
                "Animal ID": ID,
                "Name": Name,
                "DateTime": datetime.utcnow(),
                "MonthYear": datetime.utcnow(),
                "Date of Birth": DOB,
                "Outcome Type": Outcome,
                "Animal Type": AnimalType,
                "Sex upon Outcome": Sex,
                "Age upon Outcome": Age,
                "Breed": Breed,
                "Color": Color
            }
            # Print the dictionary so user can verify the correct entries were made.

            p = ""
            # Loop until user verifies that my_dictionary is correct.
            while p != 1:
                # Converts entry to lowercase so values are not case sensitive.
                p = (input("Is this correct?: ")).lower()

                if (p == "yes") or (p == "y") or (p == "1"):
                    # Send dictionary data above to the MongoDB_Module and create document.
                    i = 1
                    AnimalShelter.create(my_dict)
                    break
                # If not correct, break this while loop to re-enter my_dict variables.
                elif (p == "no") or (p == "n") or (p == "2"):
                    print("Try again.")
                    break
                # Back will break both while loops and return to main menu. No doc is created.
                elif (p == "back") or (p == "go back") or (p == "back to main") or (p == "main") or (p == "3"):
                    p = 1
                    i = 1
                    print("Document not created. Going back to menu.")
                # Catch any unacceptable variable. Loop back until user enters yes, no, etc.
                else:
                    p = ""
                    print("Entry not recognized. Please try again.")

    # If the user entered read or the number 3, execute read function.
    elif (ans == "read") or (ans == "read document") or (ans == "3"):
        print("Reading document")
        # Request the user enter a name to search for.
        key1 = input("Enter search key: ")
        value1 = input("Enter " + key1 + " value: ")
        print("Searching for: " + key1 + " : " + value1)
        a = ""
        # Option for user to enter one key value pair or two. Loop until user answers yes or no.
        while a != 1:
            # Initial prompt
            if a == "":
                a = input("Would you like to enter a second search pair?: ").lower()

            # If user entry is yes, enter second key value pair.
            elif (a == "yes") or (a == "y"):
                print(a)
                key2 = input("Enter search key: ")
                value2 = input("Enter " + key2 + " value: ")
                print("Searching for: " + key1 + " : " + value1 + " and " + key2 + " : " + value2)
                break
            # If user entry is no, set second key value pair to null value.
            # The second key value pair must be defined since read requires four arguments.
            elif (a == "no") or (a == "n"):
                key2 = ""
                value2 = ""
                print("Searching for: " + key1 + " : " + value1)
                break
            elif (a == "back") or (a == "go back"):
                print("Going back to main menu.")
                break
            # Prompt until user enters either yes or no.
            else:
                print("Please enter yes or no.")
                a = input("Would you like to enter a second search pair?: ")

        # Send user entered name to the read function in the CRUD Module. It will return the document data.
        AnimalShelter.read(key1, value1, key2, value2)

    # If the user entered update or the number 4, execute update function.
    elif (ans == "update") or (ans == "update document") or (ans == "4"):
        temp = ""
        print("Update document")
        # Loop so user can re-enter parameters for read/update function if needed.
        while temp != "done":
            # Use read function first to print documents. Helps user find the document that needs to be updated.
            print("Enter the key and value to find the document you want to update")
            searchKey = input("Search key: ")
            searchValue = input("Search value for " + searchKey + ": ")
            null = ""
            print("Searching for: " + searchKey + " : " + searchValue)
            AnimalShelter.read(searchKey, searchValue, null, null)

            # To refine search, require user to specify the animal ID number.
            key = "Animal ID"
            value = input("Enter the Animal ID of the document you wish to update. (back to return): ")
            # Escape update and return to main menu if desired.
            if (value == "back") or (value == "Back"):
                break
            # Run read function with Animal ID and initial key value pair.
            AnimalShelter.read(searchKey, searchValue, key, value)
            q = ""
            # While loop until user confirms document printed from read function above is correct.
            while q != 1:
                # Initial inquiry.
                if q == "":
                    q = input("Is this the right document?: ").lower()
                # If document is correct, ask for key value pair to update and run update function.
                elif (q == "yes") or (q == "y"):
                    updateKey = input("Enter key to update: ")
                    updateValue = input("Enter " + updateKey + " value: ")
                    AnimalShelter.update(key, value, updateKey, updateValue)
                    temp = "done"
                    break
                # If doc not correct, break this while loop; return back to read function and retry.
                elif (q == "no") or (q == "n"):
                    print("Sorry, please try again.")
                    break
                # Break this loop and initial while loop; escape back to main menu.
                elif (q == "back") or (q == "go back"):
                    print("Going back to main menu.")
                    temp = "done"
                    break
                else:
                    print("Please enter yes or no.")
                    q = input("Is this the right document?: ")

    # If the user entered delete or the number 5, execute delete function.
    elif (ans == "delete") or (ans == "delete document") or (ans == "5"):
        temp = ""
        print("Deleting document")
        # Loop so user can re-enter delete key value variables if needed.
        while temp != "done":
            # Run read function to find document to delete.
            print("Enter the key and value to find the document you want to delete")
            deleteKey = input("Search key: ")
            deleteValue = input("Search value for " + deleteKey + ": ")
            null = ""
            print("Searching for: " + deleteKey + " : " + deleteValue)
            AnimalShelter.read(deleteKey, deleteValue, null, null)
            # Require user to enter animal ID to specify which doc to delete.
            key = "Animal ID"
            value = input("Enter the Animal ID of the document that needs to be deleted (back to return): ")
            # Escape back to main menu.
            if (value == "back") or (value == "Back"):
                break
            # Run read function with Animal ID and delete parameters.
            AnimalShelter.read(deleteKey, deleteValue, key, value)
            q = ""
            # Loop until user confirms the doc printed from read function is correct or not.
            while q != 1:
                # Initial inquiry.
                if q == "":
                    q = input("This document will be deleted. Is this the right document?: ").lower()
                # If document is correct, run delete function. Exit loop and return to main.
                elif (q == "yes") or (q == "y"):
                    AnimalShelter.delete(key, value)
                    temp = "done"
                    break
                # If document is not correct, break this while loop; return to re-enter delete key value pair.
                elif (q == "no") or (q == "n"):
                    print("Sorry, please try again.")
                    break
                # Break both loops returning to main menu.
                elif (q == "back") or (q == "go back"):
                    print("Going back to main menu.")
                    temp = "done"
                    break
                else:
                    print("Please enter yes or no.")
                    q = input("Is this the right document?: ")

    # If the user entered exit, exit script and terminate program.
    elif (ans == "exit") or (ans == "0"):
        print("Goodbye")
        # Ends the while loop, terminating the program.
        break

    # If user entered anything other than an acceptable option, print error and allow the user to enter a new number.
    else:
        print("Invalid entry. Please try again")







