import os
import sys

TEST_DIR   = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from falcon import testing
from run    import Main
import pytest

@pytest.fixture(scope="module")
def client():
	api = Main().create()
	print(api)
	return testing.TestClient(Main().create())

def test_get(client):
	result = client.simulate_get("/status/Kaskus%20Crawler")
	assert result.json[0]["crawler_name"] == "Kaskus Crawler"
	assert result.status_code == 200