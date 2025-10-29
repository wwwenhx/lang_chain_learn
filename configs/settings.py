import os
from dotenv import load_dotenv
load_dotenv(override=True)

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME", "gpt-4o-mini")
API_VERSION = "2025-01-01-preview"
APK_API_KEY = os.getenv("APK_API_KEY")