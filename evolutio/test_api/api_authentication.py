from rest_framework import authentication


class TokenAuthentication(authentication.TokenAuthentication):
    """
    Overridden auth keyword to be compitable with OpenAPIv3 specification
    """

    keyword = 'Bearer'
