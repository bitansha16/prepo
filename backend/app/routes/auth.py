from app.services.jwt_service import create_token
from fastapi import APIRouter, HTTPException

from app.models.user import (
    UserRegister,
    UserLogin
)

from app.database.mongodb import users_collection

from app.services.auth_service import (
    hash_password,
    verify_password
)


router = APIRouter()



@router.post("/register")
async def register(user:UserRegister):


    existing = await users_collection.find_one(
        {"email":user.email}
    )


    if existing:

        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )


    new_user={

        "name":user.name,

        "email":user.email,

        "password":hash_password(
            user.password
        )

    }


    await users_collection.insert_one(
        new_user
    )


    return {

        "message":
        "User registered successfully"

    }



@router.post("/login")
async def login(user: UserLogin):

    db_user = await users_collection.find_one(
        {
            "email": user.email
        }
    )


    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )


    valid = verify_password(
        user.password,
        db_user["password"]
    )


    if not valid:

        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )


    token = create_token(
        {
            "email": user.email
        }
    )


    return {

        "message": "Login successful",

        "access_token": token,

        "token_type": "bearer"

    }