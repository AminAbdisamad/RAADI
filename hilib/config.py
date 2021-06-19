from starlette.config import Config

config = Config(".env")
APP_NAME = config("APP_NAME", default=None)
DESCRIPTION = config("DESCRIPTION", default=None)
VERSION = config("VERSION", default=None)
