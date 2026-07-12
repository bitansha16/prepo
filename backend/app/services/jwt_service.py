from jose import jwt

from datetime import (
    datetime,
    timedelta
)



SECRET_KEY = "PREPO_SECRET_KEY"

ALGORITHM = "HS256"



def create_token(data:dict):


    user_data = data.copy()


    expire = datetime.utcnow() + timedelta(
        hours=24
    )


    user_data.update(
        {
            "exp":expire
        }
    )


    token = jwt.encode(
        user_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return token
