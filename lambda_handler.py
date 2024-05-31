from mangum import Mangum
from main import app

# Create a Mangum handler instance with your FastAPI app
handler = Mangum(app)
