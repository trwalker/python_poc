from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from pythonweb.services.userservice import UserService


class UserController(APIView):
    def get(self, request, userid, format=None):
        user = self.get_user(userid)
        return Response(user.serialize(), status=status.HTTP_200_OK)

    def get_user(self, userid):
        userService = UserService()
        return userService.get_user(userid)


