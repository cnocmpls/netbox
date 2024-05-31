###  Project Setup Guide

Follow these steps to set up the project on your local machine.

##  Prerequisites

- A Linux-based system

- Python 3 installed


##  Clone the Repository

# First, clone the repository to your local machine:

    git clone https://github.com/yourusername/your-repo-name.git

    cd your-repo-name

    Open in Code Editor


# Open the project in your desired code editor.

- Create a Python Virtual Environment

    python3 -m venv yourenvname

- Activate the Virtual Environment

    source yourenvname/bin/activate


# Install Dependencies

- Navigate to the folder containing the requirements.txt file and install the required dependencies:

    cd path/to/requirements.txt

    python -m pip install -r requirements.txt


# Configuration and Setting Update

- After downloading dependencies, update the configuration and settings:

    Navigate to the root directory and then to netbox/netbox.

    Create the configuration.py file and copy the contents of configuration_example.py to configuration.py.

    Add your own database connection credentials and enable the debugger (set DEBUG to True).

    Navigate to settings.py and enable the debugger (set DEBUG to True) and disable development mode (set DEVELOPMENT to False).



# Run the Project

- Navigate to the folder containing the manage.py file and run the following commands:

- Collect static files:

    python3 manage.py collectstatic

- Start the development server on port 8000:

    python3 manage.py runserver


You're all set! Your project should now be running on http://127.0.0.1:8000.

