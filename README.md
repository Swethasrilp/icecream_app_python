
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

    
    git clone https://github.com/yourusername/ice-cream-app.git
    

2. **Navigate to the Project Directory**

    Change to the project directory:

    ```bash
    cd ice-cream-app
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

If your application requires an SQLite database file, make sure it is present in the project directory. If it's not included, you can create one using the following steps:

1. **Create the SQLite Database**

    You can create the database and the necessary tables using a script or manually using an SQLite database browser.

2. **Ensure Database Configuration**

    Make sure the database configuration in your code (`main.py` or the relevant file) points to the correct path of your SQLite database.

## Troubleshooting

- Ensure your virtual environment is activated before running the application.
- Make sure all dependencies are installed correctly from the `requirements.txt` file.
- Check the database path and ensure the database file exists in the specified location.

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

