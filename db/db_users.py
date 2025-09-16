from db.database import collection_users
from models.user import User
from bson import ObjectId
from datetime import datetime

async def get_db_users(key: str = '', value: any = None) -> list:
    users: list = []

    if key != '' and value != '':
        documents = collection_users.find({key: value})
    else:
        documents = collection_users.find({})
    
    async for document in documents:
        users.append(document)
        
    return users

async def create_db_user(user: User) -> User:
    data_dict = dict(user)
    if 'id' in data_dict:
        del data_dict['id']

    new_user = await collection_users.insert_one(data_dict)
    new_user = await collection_users.find_one({'_id': new_user.inserted_id, })
    return new_user

async def update_db_user(id: str, user: User) -> User: 
    user_dict = dict(user)
    if 'id' in user_dict:
        del user_dict['id']
    
    user_dict = {
        **user_dict,
        'updated_at': int(datetime.timestamp(datetime.now())),
    }

    await collection_users.update_one({'_id': ObjectId(id)}, {'$set': user_dict})
    return await get_db_one_user(key='_id', value=id, key_2='', value_2=None)

async def delete_db_user(id: str):
    return await collection_users.delete_one({'_id': ObjectId(id)})

async def get_db_one_user(key: str = '', value: any = None, key_2: str = '', value_2: any = None ):
    user: User = User
    if key != '' and key_2 != '':
        if key == '_id':
            user = await collection_users.find_one({'_id': ObjectId(value), key_2: value_2, })
        else:
            user = await collection_users.find_one({key: value, key_2: value_2, })
    else:
        if key == '_id':
            user = await collection_users.find_one({'_id': ObjectId(value), })
        else:
            user = await collection_users.find_one({key: value, })
    
    return user