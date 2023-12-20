## Data-Representation-Big_Project


### Introduction

This project was developed as a part of the Data Representation module for the Higher Diploma in Science in Data Analytics course. The primary task of this project is to create a Web application using Flask, featuring a RESTful API. This application is designed to interface with one or more database tables, with a key focus on its ability to perform CRUD (Create, Read, Update, Delete) operations on the data. The user-friendly web interface not only displays the data but also enables user interaction, leveraging the capabilities of the RESTful API for efficient data handling.

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

