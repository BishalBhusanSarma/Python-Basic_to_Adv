from fastapi import FastAPI, middleware, Request

import time
app = FastAPI()

# example of middleware
# @app.middleware("http")
# async def my_middleware(request: Request, call_next):
#     print("Request received")


#     response = await call_next(request)

#     print("Response sent")
#     return response

#example of logging middleware(tracking)

@app.middleware("http")
async def tracking_middleware(request: Request, call_next):
    current_time = time.time()

    

    print("Request received")

    response = await call_next(request)
    response_time = time.time()-current_time

    print(f"path: {request.url.path} | time : {response_time}")
    return response