from langchain_core.tools import tool
import requests
from urllib.parse import unquote

@tool
def fetch_url_content(url: str) -> str:
    """Fetch content from a URL."""
    try:
        # Ensure the URL is decoded properly
        decoded_url = unquote(url.strip("'\""))

        # Make the HTTP request using requests.get
        response = requests.get(decoded_url)

        # Raise an error for HTTP responses like 404 or 500
        response.raise_for_status()  # This will raise an exception for bad responses (e.g., 404 or 500)

        return response.text  # Return the content of the URL

    except requests.exceptions.RequestException as e:
        return f"Error fetching URL content: {str(e)}"
