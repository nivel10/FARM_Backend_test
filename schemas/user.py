def user_schema(data) -> dict:
    return {
        'id': str(data['_id']),
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'password': data['password'],
        'is_deleted': data['is_deleted'],
        'created_at': data['created_at'],
        'updated_at': data['updated_at'],
    }

def user_resgister_response_schema(data) -> dict:
    return {
        'id': str(data['_id']),
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        # 'password': data['password'],
        'is_deleted': data['is_deleted'],
        'created_at': data['created_at'],
        'updated_at': data['updated_at'],
    }

def users_register_respose_schema(datas) -> list[dict]:
    return [user_resgister_response_schema(user) for user in datas]
