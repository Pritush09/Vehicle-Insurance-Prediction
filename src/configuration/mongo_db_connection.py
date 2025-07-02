import pymongo
import certifi
import sys
from src.exception import ApplicationException
from src.logger import logger
from src.constants import DATABASE_NAME, MONGODB_URL_KEY  # MONGODB_URL_KEY contains full URL

# Load the certificate authority bundle for secure connection
ca = certifi.where()

class MongoDBClient:
    """
    MongoDBClient is responsible for establishing a connection to the MongoDB database.

    Attributes:
    ----------
    client : MongoClient
        A shared MongoClient instance for the class.
    database : Database
        The specific database instance that MongoDBClient connects to.

    Methods:
    -------
    __init__(database_name: str) -> None
        Initializes the MongoDB connection using the given database name.
    """

    client = None  # Shared MongoClient instance

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. Reuses an existing connection if available.

        Parameters:
        ----------
        database_name : str
            Name of the MongoDB database to connect to.
        """
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY  # ✅ Already contains the actual URL
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name

            logger.info(f"MongoDB connection to [{database_name}] successful.")

        except Exception as e:
            raise ApplicationException(e, sys.exc_info())
