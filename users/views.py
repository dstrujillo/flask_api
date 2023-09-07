from flask import Response
from flask_restful import Resource, marshal_with
from flask import request, make_response
from users.service import create_user, reset_password_email_send, login_user, reset_password
from users.models import *



class SignUpApi(Resource):
    @swagger.operation(
            notes='POST response method for creating user.',
            responseClass = User.__name__,
            nickname = 'Register User',
    )
    @staticmethod
    def post() -> Response:
        """
        POST response method for creating user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)


class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for login user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)


class ForgotPassword(Resource):
    @staticmethod
    def post() -> Response:
        """
        POST response method for forgot password email send user.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password_email_send(request, input_data)
        return make_response(response, status)


class ResetPassword(Resource):
    @swagger.operation(
            notes='POST response method for save new password.',
            responseClass = User.__name__,
            nickname = 'Reset Password',
            responseMessage=[
                {
                    "code" : 201,
                    "message":"Reset Password success"
                },
                {
                    "code" : 401,
                    "message":"Not allowed"
                }
            ]
    )
    @staticmethod
    def post(token) -> Response:
        """
        POST response method for save new password.

        :return: JSON object
        """
        input_data = request.get_json()
        response, status = reset_password(request, input_data, token)
        return make_response(response, status)
