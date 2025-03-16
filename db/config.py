import os

# Example config file
DB_URI = os.getenv("DB_URI", "sqlite:///my_dashboard.db")

API_EMAIL = "antoon.kamel@illa.com.eg"
API_PASSWORD = "1234567"

# The token below is the example from your response. In real usage, you might
# re-fetch it via the sign-in endpoint or store it in a safer manner.
API_TOKEN = os.getenv("API_TOKEN", "eyJhbGciOiJub25lIn0.eyJpZCI6MTg4LCJlbWFpbCI6ImFudG9vbi5rYW1lbEBpbGxhLmNvbS5lZyIsImNyZWF0ZWRfYXQiOiIyMDI0LTA0LTI5VDExOjQ3OjA3Ljc3N1oiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wNC0yOVQxMTo0NzowNy43NzdaIiwiZmlyc3RfbmFtZSI6IkFudG9vbiAiLCJsYXN0X25hbWUiOiJLYW1lbCAiLCJjcmVhdG9yX3R5cGUiOiJBZG1pblVzZXIiLCJjcmVhdG9yX2lkIjo3NiwiZGlzY2FyZGVkX2F0IjpudWxsfQ.")  # truncated example

BASE_API_URL = "https://app.illa.blue/api/v2"

