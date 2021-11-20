from user import User

user=[
    User(1,"Mangesh","mangesh123")

]
username_mapping={u.username:u for u in user}
userid_mapping={u.id:u for u in user}


def authenticate(username,password):
    user1=username_mapping.get(username,None)
    if user1 and user1.password==password:
        return user1

def identity(payload):
    user_id=payload['identity']
    return userid_mapping.get(user_id,None)