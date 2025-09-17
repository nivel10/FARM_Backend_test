def task_schema(data):
    return {
        'id': str(data['_id']),
        'created_by': str(data.get('created_by', '')) if data.get('created_by') else '',
        'title': data['title'],
        'description': data['description'],
        'date': data.get('date', '') if data.get('date') else 0,
        'completed': data['completed'],
        'is_deleted': data['is_deleted'],
        'created_at': data['created_at'],
        'updated_at': data['updated_at'],
    }

def tasks_schema(datas):
    return [task_schema(data) for data in datas]