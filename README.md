
# Ice Cream App

This is an Ice Cream App built using Python, SQLite, and Tkinter for the GUI. Below are the instructions to set up and run the application in Visual Studio Code.

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/downloads) (for cloning the repository)

## Installation

1. **Clone the Repository**

    Open your terminal and clone the repository using Git:

    ```bash
    git clone https://github.com/Swethasrilp/icecream_app_python.git
    ```

2. **Navigate to the Project Directory**

    Change to the project directory:

    ```bash
    cd icream_l7_
    ```

3. **Create a Virtual Environment**

    It's a good practice to create a virtual environment for your project. Run the following command to create one:

    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment**

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

5. **Install the Required Packages**

    Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Open the Project in Visual Studio Code**

    Open Visual Studio Code and open the project folder you just cloned.

2. **Run the Application**

    With the virtual environment activated and the necessary packages installed, you can run the application by executing the main script. In VS Code terminal, run:

    ```bash
    python main.py
    ```

## SQLite Database

The SQLite database is already configured in the application. Ensure the database file is present in the project directory. If the database file is not included in the repository, you can create one using an SQLite database browser or script.

### Troubleshooting

- Ensure your virtual environment is activated before running the application.
- Make sure all dependencies are installed correctly from the `requirements.txt` file.
- Verify that the database file exists in the specified location.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.
