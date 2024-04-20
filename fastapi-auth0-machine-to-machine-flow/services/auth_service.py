# --- Library Imports ---
from fastapi import status, HTTPException
from auth0.authentication import Database
from auth0.exceptions import Auth0Error
from auth0.authentication import GetToken
# ---

# --- User Imports ---
from ..schema.auth_schema import SignupSchema, LoginSchema
from ..schema.response import ResponseSchema
from ..config.env import env 
# ---

# --- Constants ---
AUTH0_DOMAIN = env.AUTH0_DOMAIN
CLIENT_ID = env.CLIENT_ID
CLIENT_SECRET = env.CLIENT_SECRET
# ---


class AuthService:
    async def create_user(user: SignupSchema):
        try:
            # initiate auth0 db object
            database = Database(AUTH0_DOMAIN, CLIENT_ID)

            # prepare users metadata, this will be extracted and utilized in the signup script of auth0
            user_metadata = {
                "firstName": user.firstName,
                "lastName": user.lastName,
                "phoneNumber": user.phoneNumber,
                "NMLS": user.NMLS,
                "lenderId": f"{user.lenderId}",
            }

            # This calls the signup custom database script in auth0. Refer to create_user.js in auth0_database_action_scripts
            database.signup(
                email=user.email,
                password=user.password,
                user_metadata=user_metadata,
                connection="Username-Password-Authentication",
            )

            return ResponseSchema(
                status=status.HTTP_201_CREATED,
                message="User created successfully!",
                success=True,
            )
        except Auth0Error as e:
            raise HTTPException(status_code=e.status_code, detail=e.message)

    async def login_user(user: LoginSchema):
        try:
            # This calls the get user custom database script in auth0. Refer to get_user.js in auth0_database_action_scripts
            token = GetToken(
                AUTH0_DOMAIN,
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
            )

            # This calls the login custom database script in auth0. Refer to login.js in auth0_database_action_scripts
            token = token.login(
                username=user.email,
                password=user.password,
                realm="Username-Password-Authentication",
            )
            return token
        except Auth0Error as e:
            raise HTTPException(status_code=e.status_code, detail=e.message)
