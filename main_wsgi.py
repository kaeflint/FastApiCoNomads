from application import *
import uvicorn

if __name__=='__main__':
    uvicorn.run("application:app", port=5000, reload=True, access_log=False,log_level="info")
    #uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info",reload=True, workers=-1)