## AirBnB Clone - The Console ✨

Welcome to the AirBnB Clone project! This repository houses the foundation for a command-line interface designed to manage objects within an AirBnB clone application. This project serves as the first crucial step toward building a comprehensive web application.

**Project Overview:**

This project lays the groundwork for a robust and scalable AirBnB clone by providing the following core features:

- **Object Management:** Create, retrieve, update, and delete (CRUD) operations on various AirBnB entities like users, places, states, cities, amenities, and reviews.
- **Command-Line Interface:** A user-friendly console interface built using the `cmd` module, enabling interactive object management.
- **Data Persistence:**  Utilize a file storage mechanism to store and retrieve object data.
- **Object Serialization & Deserialization:** Leverage JSON to serialize and deserialize objects, facilitating data transfer and storage.
- **Unit Testing:** Comprehensive test suite to ensure code quality and maintainability.

**Key Concepts:**

- **Object-Oriented Programming:** Utilizes Python's OOP concepts for modularity and code reusability.
- **Data Structures & Algorithms:** Efficient data structures and algorithms are employed for data storage and retrieval.
- **File Handling:**  Interacts with files to store and retrieve object data.
- **JSON Serialization/Deserialization:** Efficiently converts objects into JSON format for data storage and transfer.

**Project Structure:**

```
*AirBnB_clone*
├── AUTHORS
├── console.py
├── file.json
├── __init__.py
├── *models*
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── *engine*
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── *tests*
    ├── __init__.py
    ├── test_console.py
    └── *test_models*
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── *test_engine*
        │   ├── __init__.py
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

**Getting Started:**

1. **Clone the repository:** 
   ```bash
   git clone https://github.com/OusamaTheCoder/AirBnB_clone
   ```
2. **Navigate to the project directory:**
   ```bash
   cd AirBnB_clone
   ```

**Running the Console:**

To start the interactive command interpreter, run the `console.py` script:

```bash
python3 console.py
```

You'll be greeted with the `(hbnb)` prompt, ready to execute commands.

**Available Commands:**

- **`help`:** Displays a list of available commands and their usage.
- **`create <class_name>`:** Creates a new instance of the specified class.
- **`show <class_name> <id>`:** Displays details of an object with the given ID.
- **`destroy <class_name> <id>`:** Deletes an object with the given ID.
- **`all <class_name>`:** Displays all objects of the specified class.
- **`update <class_name> <id> <attribute_name> <attribute_value>`:** Updates an attribute of an object with the given ID.
- **`count <class_name>`:** Counts the number of objects of the specified class.
- **`quit`:** Exits the console.

**Example Usage:**

```
(hbnb) create User
51f22861-e842-4764-af4c-eca5b9dfa837
(hbnb) User.show("51f22861-e842-4764-af4c-eca5b9dfa837")
[User] (51f22861-e842-4764-af4c-eca5b9dfa837) {'id': '51f22861-e842-4764-af4c-eca5b9dfa837', 'created_at': datetime.datetime(2024, 5, 18, 18, 16, 36, 400055), 'updated_at': datetime.datetime(2024, 5, 18, 18, 16, 36, 400065)}
(hbnb) User.destroy("51f22861-e842-4764-af4c-eca5b9dfa837")
(hbnb) Place.all()
(hbnb) User.update("51f22861-e842-4764-af4c-eca5b9dfa837") first_name John
(hbnb) User.count()
1
(hbnb) quit
```

**Unit Testing:**

The project includes a comprehensive test suite located in the `tests` directory. To run the tests:

```bash
python3 -m unittest discover tests
```

**Documentation:**

- All modules, classes, and functions are thoroughly documented with docstring, explaining their purpose, parameters, and functionality.

**License:**

This project is licensed under the MIT License.

**Contribution:**

We welcome contributions! If you'd like to contribute, please feel free to open an issue or submit a pull request.

#Disclaimer

If you happen to use this repo, we scored 117%

**Authors:**

- `Basmala Hussein`
- `Ousama Oujaber`

**Let's build a fantastic AirBnB clone together! 🚀** 
