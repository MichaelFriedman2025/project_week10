import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()


class Contact:

    @staticmethod
    def get_db_connection():
        try:
            connection = mysql.connector.connect(
                host=os.getenv("DB_HOST"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME"),
            )
            return connection
        except Error as e:
            raise e

    @staticmethod
    def get_all_contacts():
        connection = Contact.get_db_connection()
        cursor = connection.cursor()
        try:
            query = (
                "SELECT id,first_name,last_name,phone_number FROM contacts ORDER BY id"
            )
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Error as e:
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def create_contact(first_name, last_name, phone_number):
        connection = Contact.get_db_connection()
        cursor = connection.cursor()
        try:
            query = "INSERT INTO contacts(first_name,last_name,phone_number) VALUES(%s, %s, %s)"
            cursor.execute(query, (first_name, last_name, phone_number))
            connection.commit()
            return cursor.lastrowid
        except Error as e:
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def update_contact(id, first_name, last_name, phone_number):
        connection = Contact.get_db_connection()
        cursor = connection.cursor()
        try:
            query = "UPDATE contacts SET first_name = %s,last_name= %s,phone_number= %s WHERE id = %s"
            cursor.execute(query, (first_name, last_name, phone_number, id))
            connection.commit()
            return True
        except Error as e:
            raise e
        finally:
            cursor.close()
            connection.close()

    @staticmethod
    def delete_contact(id):
        connection = Contact.get_db_connection()
        cursor = connection.cursor()
        try:
            query = "DELETE FROM contacts WHERE id = %s"
            cursor.execute(query, (id,))
            connection.commit()
        except Error as e:
            raise e
        finally:
            cursor.close()
            connection.close()
