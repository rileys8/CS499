from pymongo import MongoClient
from pprint import pprint

# MongoDB database
client = MongoClient('mongodb://localhost:27017')
database = client["AAC"]
collection = database["animals"]


# Init Animal Shelter class
# noinspection PyMethodParameters
class AnimalShelter(object):

    # Test connection to MongoDB database
    def test():
        # Print message will only display if this file is imported correctly.
        print("Connected to MongoDB_Modules.py")
        print("Checking mongoDB database connection...")
        try:
            # Below code will throw an error if not connected to the mongoDB database.
            client.server_info()
            print("Connected to mongoDB database")
        except:
            # Error will print if the code above fails.
            print("Connection Error")

    # The create function pulls a dictionary variable from an external file.
    def create(data):
        collection.database.animals.insert(data)
        done = "Done"
        return done

    # This function provides the ability to search for a name within the database.
    def read(key1, value1, key2, value2):
        # Count var to record number of documents found. n var is dictionary to store documents.
        count = 0
        n = []
        # If user provided two key value pairs, run pymongo find method with two key value pairs.
        # _id false will prevent the mongoDB provided unique id from printing as well.
        if key2 != "":
            i = collection.find({str(key1): str(value1), str(key2): str(value2)}, {"_id": False})
            # For loop will pull each document individually and store in dict n; count number of documents.
            for animals in i:
                n.append(animals)
                count = count + 1
            # Count will increase one with each itteration of loop above.
            print("Number of results:  " + str(count) + ".")
            pprint(n)
            print("Number of results above: " + str(count))
        # If user provided only one key value pair, run pymongo find method with only one key value pair.
        # These two are separated since searching for key value pair {"" : ""} will yield no results.
        else:
            i = collection.find({str(key1): str(value1)}, {"_id": False})
            # Loop functions same as above.
            for animals in i:
                n.append(animals)
                count = count + 1
            print("Showing " + str(count) + " results.")
            pprint(n)
            print("Number of results above: " + str(count))

    # Function will input the search values to read the document first, then will update the values specified.
    def update(searchKey, searchValue, updateKey, updateValue):
        # Try and except to keep program running in the event of an error.
        try:
            # Consolidate update method into one variable.
            valueUpdate = collection.update_one({str(searchKey): str(searchValue)},
                                                {"$set": {str(updateKey): str(updateValue)}})
            print(valueUpdate)
            # Display new document with updates using pymongo find_one method.
            searchResult = collection.find_one({str(searchKey): str(searchValue)})
            pprint(searchResult)
            print("Document updated")
        except:
            print("Error.")

    # This function will delete a document specified by the user.
    def delete(key, value):
        print("Deleting document")
        # Using pymongo delete method, remove document from database.
        deleteDoc = collection.delete_one({str(key): str(value)})
        # Prints pymongo delete cursor.
        print(deleteDoc)
        print("Document deleted")







