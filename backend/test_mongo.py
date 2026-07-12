import asyncio

from app.database.mongodb import database


async def test_connection():

    print("Trying MongoDB connection...")

    try:

        collections = await database.list_collection_names()

        print("MongoDB Connected ✅")

        print(
            "Collections:",
            collections
        )


    except Exception as e:

        print("MongoDB Error ")

        print(e)



asyncio.run(
    test_connection()
)