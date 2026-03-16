from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.users import router as user_router
from execeptions.base_exeception import base_exeception_handler
from execeptions.app_exeception import AppExeception
from sockets.user_socket import router as user_socket

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# REGISTER ENDPOINT ROUTES HERE
app.include_router(user_router, prefix="/api/users", tags=["Users"])

# REGISTER WEB_SOCKETS ROUTERS HERE
app.include_router(user_socket, prefix="/ws")


app.add_exception_handler(Exception, base_exeception_handler)
app.add_exception_handler(AppExeception, base_exeception_handler)
