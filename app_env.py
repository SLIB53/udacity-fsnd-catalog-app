"""
'Catalog App' application shared constants and runtime information.
"""

from os.path import abspath


# ==============================================================================
# Constants
# ==============================================================================

DB_FILE_PATH = abspath("catalog.db")
SERVER_HOST = "localhost"
SERVER_PORT = 5000


# ==============================================================================
# Runtime Context
# ==============================================================================

class AppContext:
    def __init__(self, db_uri):
        self.db_uri = db_uri


def gen_main_context():
    return AppContext(db_uri=DB_FILE_PATH)
