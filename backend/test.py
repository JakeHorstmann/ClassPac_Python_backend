from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

# SEE https://fastapi.tiangolo.com/tutorial/testing/
