def user_schema(data):
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

def user_resgister_response_schema(data):
    return {
        'id': str(data['_id']),
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'email': data['email'],
        'is_deleted': data['is_deleted'],
        'created_at': data['created_at'],
        'updated_at': data['updated_at'],
    }

