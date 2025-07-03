import sys
import pandas as pd
import numpy as np
from typing import Optional
from src.logger import logger
from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import ApplicationException

class InsuranceData:
    """
    A class to export MongoDB records as a pandas DataFrame.
    """

    def __init__(self) -> None:
        """
        Initializes the MongoDB client connection.
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise ApplicationException(e, sys.exc_info())

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        """
        Exports an entire MongoDB collection as a pandas DataFrame.

        Parameters:
        ----------
        collection_name : str
            The name of the MongoDB collection to export.
        database_name : Optional[str]
            Name of the database (optional). Defaults to DATABASE_NAME.

        Returns:
        -------
        pd.DataFrame
            DataFrame containing the collection data, with '_id' column removed and 'na' values replaced with NaN.
        """
        try:
            # Access specified collection from the default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # Convert collection data to DataFrame and preprocess
            print("Fetching data from mongoDB")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fecthed with len: {len(df)}")
            
            logger.info(f"Columns present inside the database before droping the _id column {df.columns.to_list()}")
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            
            logger.info(f"Columns present inside the database after droping the _id column {df.columns.to_list()}")

            #replacing the na value with np.nan
            df.replace({"na":np.nan},inplace=True)
            
            return df

        except Exception as e:
            raise ApplicationException(e, sys.exc_info())