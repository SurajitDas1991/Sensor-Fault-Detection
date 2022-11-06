from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__ == '__main__':
    mongo=MongoDBClient()
    print(mongo.database.list_collection_names())
