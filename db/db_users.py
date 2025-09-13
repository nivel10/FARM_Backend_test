from db.database import collection_users
from models.user import User
from bson import ObjectId

async def create_db_user(user: User):
    data_dict = dict(user)
    if 'id' in data_dict:
        del data_dict['id']

    new_user = await collection_users.insert_one(data_dict)
    new_user = await collection_users.find_one({'_id': new_user.inserted_id, })
    return new_user

async def get_db_one_user(key: str, value: any):
    user: any = any
    if key == '_id':
        user = await collection_users.find_one({'_id': ObjectId(value), })
    else:
        user = await collection_users.find_one({key: value, })
    
    return user