from fastapi import FastAPI
from api.users import user_route
import uvicorn

app = FastAPI()

app.include_router(user_route,prefix='/api')


if __name__ == '__main__':
    uvicorn.run("main:app",host='localhost',port=8088, reload=True)


