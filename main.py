import uvicorn
from sugarvany_api.interface.api.app import app

if __name__ == "__main__":
    uvicorn.run("sugarvany_api.interface.api.app:app", host="0.0.0.0", port=8000, reload=True) 