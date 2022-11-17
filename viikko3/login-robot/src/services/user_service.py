from entities.user import User
import re, sys, pdb


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        
        # pdb.Pdb(stdout=sys.__stdout__).set_trace()

        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if not re.match("^[a-z]{3,}$", username):
            raise UserInputError("Username must consist of letters a-z and be atleast 3 characters long")

        if not re.match("^(?=.+[A-Za-z])(?=.+\d)[A-Za-z\d]{8,}$", password):
            raise UserInputError("Password must consist of letters a-Z digits 0-9, be atleast 8 characters long and contain at least 1 character and 1 digit")
