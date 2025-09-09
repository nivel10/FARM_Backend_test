def task_schema(data):
    return {
        "id": str(data["_id"]),
        "title": data["title"],
        "description": data["description"],
        "completed": data["completed"],
        "is_deleted": data["is_deleted"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
    }

def tasks_schema(datas):
    return [task_schema(data) for data in datas]