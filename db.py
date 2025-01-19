"""
This module handles database connections and operations for the Where Is Parking app.
It uses Google Cloud SQL connector to establish a connection to a MySQL database.
The module provides functions for inserting new user data into the 'Users' table.
It also demonstrates basic database querying.  Note that error handling and security
best practices are minimal in this example and should be enhanced for production use.
"""
import uuid
import sqlalchemy
from google.cloud.sql.connector import Connector

DATABASE_URL = "mysql+pymysql://wipdb:@dmin$4321@where-is-parking-app:asia-south1:wip-dev-gcp-csql/wip"

def insert_user(fname, lname, email, city, gen, mob, pswd):
    """Inserts a new user into the Users table."""
    try:
        # Create a connection pool using sqlalchemy.create_engine
        engine = sqlalchemy.create_engine(DATABASE_URL)

        # Define the insert query
        insert_query = sqlalchemy.text(
            "INSERT INTO Users(UUID,LastName,FirstName,EmailID,City,Gender,Mobile,PassD) VALUES (:UUID,:LastName,:FirstName,:EmailID,:City,:Gender,:Mobile,:PassD)"
        )

        # Prepare the insert values
        insert_values = {
            "UUID": str(uuid.uuid4()),
            "LastName": lname,
            "FirstName": fname,
            "EmailID": email,
            "City": city,
            "Gender": gen,
            "Mobile": mob,
            "PassD": pswd,
        }

        # Establish a connection and execute the query
        with engine.connect() as connection:
            result = connection.execute(insert_query, insert_values)
            connection.commit()
            print(f"User inserted successfully: {result.rowcount}")

    except Exception as e:
        print(f"Error inserting user: {e}")

def get_user():
    """Fetches all users from the Users table."""
    engine = sqlalchemy.create_engine(DATABASE_URL)
    with engine.connect() as connection:
        result = connection.execute(sqlalchemy.text("SELECT * FROM Users")).fetchall()
        print(result)


