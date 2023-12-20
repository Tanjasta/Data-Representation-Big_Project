## Data-Representation-Big_Project


### Introduction

Create a Web application in Flask that has a RESTful API, the application
should link to one or more database tables.
You should also create the web pages that can consume the API. I.e. performs
CRUD operations on the data.

### Features

Interactive Car Viewer **(carviewer.html)**: A web-based interface for viewing, creating, updating, and deleting car records. It uses AJAX to communicate with the server backend.

Server Backend **(a_server.py)**: A Flask web server that handles HTTP requests for CRUD operations on car data.

Database Access Object **(carDAO.py)**: A Python class for handling database operations related to car data.
Setup and Running the Project


### Prerequisites

Python 3.x

pip

Virtual Environment (venv)

### Setting up a Virtual Environment

#### Create a Virtual Environment:

python -m venv venv

#### Activate the Virtual Environment: 

On Windows: venv\Scripts\activate

On Unix or MacOS: source venv/bin/activate

#### Install Dependencies:

pip install flask mysql-connector

### Running the Application

#### Start the Flask Server:

python a_server.py

This command runs the Flask server, making the application accessible on http://127.0.0.1:5000/.

#### Access the Car Viewer:
Open a web browser and navigate to http://127.0.0.1:5000/ to use the car viewer interface.

### Dependencies

Flask

MySQL Connector

jQuery

Bootstrap

