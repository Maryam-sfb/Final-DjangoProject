from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView,   # to produce token for the first time
                                            TokenRefreshView)   # to produce token after it is expired


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('api-token-auth/', obtain_auth_token),  # to produce a unique token for every user
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('oauth/', include('social_django.urls', namespace='social')),
]


# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTM3ODQ3NCwianRpIjoiOGQ5MTQ3YmY2MThkNDc4OGFmZWZiMmU0NDM2ZWVkMjQiLCJ1c2VyX2lkIjoxfQ.MZCll0DmUxQwXNRTCJhp8ZFIF5eMi5BIy-WFRFxtNfk",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5MjkyMzc0LCJqdGkiOiJjYjBkNWM3ZDY2Mjk0N2FhODY1MzdlYWUyODQ0YmRhNSIsInVzZXJfaWQiOjF9.EAUKs9w0lyMPT9i9NybzBxp1RfjdRP6UtqXAE7uElsc"
# }
