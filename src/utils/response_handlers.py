import traceback
import logging
from fastapi import  HTTPException
from starlette.responses import JSONResponse
from functools import wraps
# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



"""
    this wrapper function helps in keeping uniformed response across application and helps in reducing duplication of
    creating of response structure everytime and writing try catch blocks every where
"""
def response(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            # Call the endpoint function
            if len(kwargs)>0:
                data = await func(**kwargs)
            else:
                data = await func()
            # Construct and return a successful response
            return JSONResponse(
                status_code=200,
                content={"status": "success", "data": data, "error_message": None}
            )
        except HTTPException as exc:
            logger.error(f"HTTPException occurred: {exc.detail}")
            return JSONResponse(
                status_code=exc.status_code,
                content={"status": "error", "data": None, "error_message": exc.detail}
            )
        except Exception as exc:
            # If an exception occurs, construct and return an error response
            error_message = f"Internal server error: {str(exc)}"
            logger.error(error_message)
            traceback.print_exc()
            return JSONResponse(
                status_code=500,
                content={"status": "error", "data": None, "error_message": error_message}
            )

    return wrapper