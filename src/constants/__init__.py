import os
from datetime import date
from dotenv import load_dotenv
load_dotenv()
username = os.getenv("MongoDB_Username")
password = os.getenv("MongoDB_Password")

# MongoDB connection details
DATABASE_NAME = "insurance_db"  # Name of the MongoDB database
COLLECTION_NAME = "customer_policies"  # Name of the MongoDB collection
# MongoDB connection URL. This should be a f-string where `username` and `password` are securely provided.
# For production, these credentials should be loaded from environment variables or a secure configuration system.
MONGODB_URL_KEY = f"mongodb+srv://{username}:{password}@cluster0.nwjhptf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


# Pipeline and artifact related constants
PIPELINE_NAME: str = ""  # Name of the machine learning pipeline (can be left empty if not specifically named)
ARTIFACT_DIR: str = "artifact"  # Directory where all pipeline artifacts (processed data, models, etc.) will be stored

# Model and preprocessing file names
MODEL_FILE_NAME = "model.pkl"  # Name of the trained machine learning model file
TARGET_COLUMN = "Response"  # Name of the target variable column in the dataset
CURRENT_YEAR = date.today().year  # Current year, used for potential feature engineering or data filtering
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"  # Name of the preprocessing object file (e.g., StandardScaler, OneHotEncoder)

# Data file names
FILE_NAME: str = "data.csv"  # Default name for the raw data file
TRAIN_FILE_NAME: str = "train.csv"  # Name for the training dataset file
TEST_FILE_NAME: str = "test.csv"  # Name for the testing dataset file
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")  # Path to the data schema YAML file, defining expected data types and columns

# AWS credentials and region
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"  # Environment variable name for AWS Access Key ID
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"  # Environment variable name for AWS Secret Access Key
REGION_NAME = "us-east-1"  # AWS region to be used for services like S3

"""
Data Ingestion related constants
"""
DATA_INGESTION_COLLECTION_NAME: str = "customer_policies"  # MongoDB collection name specifically for data ingestion (redundant if same as COLLECTION_NAME)
DATA_INGESTION_DIR_NAME: str = "data_ingestion"  # Directory for data ingestion artifacts
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"  # Directory within data ingestion to store raw data/feature store
DATA_INGESTION_INGESTED_DIR: str = "ingested"  # Directory within data ingestion to store ingested data (e.g., train/test splits)
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25  # Ratio for splitting data into training and testing sets

"""
Data Validation related constants
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"  # Directory for data validation artifacts
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"  # Name of the data validation report file

"""
Data Transformation related constants
"""
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"  # Directory for data transformation artifacts
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"  # Directory within data transformation to store transformed data
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"  # Directory within data transformation to store the transformation object (e.g., preprocessor)

"""
Model Trainer related constants
"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"  # Directory for model training artifacts
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"  # Directory within model trainer to store the trained model
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"  # Name of the trained model file (redundant if same as MODEL_FILE_NAME)
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6  # Expected minimum performance score for the trained model
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")  # Path to the model configuration YAML file
MODEL_TRAINER_N_ESTIMATORS = 200  # Number of trees in the forest for tree-based models (e.g., RandomForest)
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7  # Minimum number of samples required to split an internal node
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6  # Minimum number of samples required to be at a leaf node
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 10  # Maximum depth of the tree
MIN_SAMPLES_SPLIT_CRITERION: str = 'entropy'  # Function to measure the quality of a split (e.g., 'gini' or 'entropy')
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101  # Seed used by the random number generator for reproducibility

"""
Model Evaluation related constants
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.02  # Threshold for significant change in model performance during evaluation
MODEL_BUCKET_NAME = "my-model-mlopsproj"  # Name of the S3 bucket for storing models
MODEL_PUSHER_S3_KEY = "model-registry"  # Key (folder) within the S3 bucket for model registry

# Application host and port for serving the model (e.g., with Flask or FastAPI)
APP_HOST = "0.0.0.0"  # Host address for the application (0.0.0.0 makes it accessible externally)
APP_PORT = 5000  # Port number for the application