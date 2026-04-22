# API imports
from ninja_extra import NinjaExtraAPI ## api with authentication
from ninja_jwt.controller import NinjaJWTDefaultController


# step1: initialize API
api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
# The above line adds the following endpoints:
# 1- api/token/pair     ==> obtain token (same as /login basically)
# 2- api/token/refresh  ==> refresh token
# 3- api/token/verify   ==> verify token
# it will automatically use the AUTH_USER_MODEL defined in the settings and use 
# the authentication backend [as if you are using the django.contrib.auth.authenticate method]


# step2: adding routers with endpoints defined in each app 
# api.add_router("auth", "ms0_usersAndAuth.api.router")

