import mysql.connector
import streamlit as st
from mysql.connector import Error

def get_connection():
    try:
        st.write(st.secrets.db_credentials.DB_USERNAME)
        connection = mysql.connector.connect(user=st.secrets.db_credentials.DB_USERNAME, password=st.secrets.db_credentials.DB_PASSWORD, host=st.secrets.db_credentials.DB_HOST, database=st.secrets.db_credentials.DB_DATABASE)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def fetch_unique_values(column, table):
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        query = f"SELECT DISTINCT {column} FROM {table}"
        cursor.execute(query)
        values = cursor.fetchall()
        cursor.close()
        conn.close()
        return [value[0] for value in values]
    else:
        return []

def fetch_beans(path, value):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        if path == 'manufacturer':
            query = "SELECT * FROM beans WHERE manufacturer = %s"
        elif path == 'brew_method':
            query = """
                SELECT beans.* FROM beans
                JOIN brewing_details ON beans.id = brewing_details.bean_id
                JOIN equipment ON brewing_details.equipment_id = equipment.id
                WHERE equipment.type = %s
            """
        elif path == 'origin':
            query = "SELECT * FROM beans WHERE origin = %s"
        cursor.execute(query, (value,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    else:
        return []

def fetch_brewing_methods(bean_id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT brewing_details.*, equipment.type AS equipment_type FROM brewing_details
            JOIN equipment ON brewing_details.equipment_id = equipment.id
            WHERE brewing_details.bean_id = %s
        """
        cursor.execute(query, (bean_id,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    else:
        return []

def fetch_tasting_notes(bean_id, brewing_detail_id):
    conn = get_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT * FROM tasting_notes
            WHERE bean_id = %s AND brewing_detail_id = %s
        """
        cursor.execute(query, (bean_id, brewing_detail_id))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    else:
        return []
