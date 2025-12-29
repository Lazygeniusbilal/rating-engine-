# this file is used to create database connection 
from supabase import create_client
from src.config import settings
from ensure import ensure_annotations
import pandas as pd


def create_database_connection():
    """this function is used to connect to the database """
    # get the credentials need to create connection
    try:
        supabase_url= settings.supabase_url
        supabase_key= settings.supabase_key
        # create connection
        return create_client(supabase_url, supabase_key)
    except Exception as e:
        print("Error in creating database connection")

@ensure_annotations
def fetch_data(table_name: str):
    """this function is used to get data from the table """
    try:
        # create connection using function
        client = create_database_connection()
        # get the table using client
        result = client.table(table_name).select("*").execute()
        # check if data exists or not if exists convert it into df so we can do modeling
        if result.data:
            return pd.DataFrame(result.data)
        else:
            raise ValueError(f"No data returned from table '{table_name}'")
    except Exception as e:
        print(f"Error fetching data from table '{table_name}': {e}")
        raise