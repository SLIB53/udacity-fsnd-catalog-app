class CatalogAppError(Exception):
    pass


class ApplicationError(CatalogAppError):
    """Base class for application layer level exceptions."""
    pass


class JSONBodyError(ApplicationError):
    pass


class APIError(CatalogAppError):
    """Base class for API layer level exceptions."""
    pass


# class ArgumentTypeError(APIError):
#     pass


class DBError(CatalogAppError):
    """Base class for data layer level exceptions."""
    pass
