"""Configuration file for the app."""
import os

BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed?"
API_KEY = os.environ.get("NASA_API_KEY")