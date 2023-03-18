from enum import Enum
import jwt

def get_user(request):
    token = request.POST.get('token', None)
    if (token == None):
        token = request.headers['token']
    payload = jwt.decode(token, 'secret', 'HS256')

    return (payload['user_id'], get_role(payload['user_id']))

class Role(Enum):
    Customer = 1
    Agent = 2
    Manager = 3

def get_role(user: str) -> Role:
    if (user[0] == "M"):
        return Role.Manager
    elif (user[0] == "A"):
        return Role.Agent
    elif (user[0] == 'C'):
        return Role.Customer
    else:
        raise
