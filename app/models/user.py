users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

def get_all_users():
    return users

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def add_user(name, email):
    new_id = max(user["id"] for user in users) + 1 if users else 1
    user = {"id": new_id, "name": name, "email": email}
    users.append(user)
    return user

def update_user(user_id, name, email):
    user = get_user_by_id(user_id)
    if user:
        user["name"] = name
        user["email"] = email
    return user

def update_user_partial(user_id, data):
    user = get_user_by_id(user_id)
    if user:
        user.update({k: v for k, v in data.items() if k in user})
    return user

def delete_user(user_id):
    global users 
    users = [user for user in users if user["id"] != user_id]