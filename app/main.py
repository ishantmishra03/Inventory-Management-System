from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import auth

app = FastAPI()

router = APIRouter()

origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             
    allow_credentials=True,            
    allow_methods=["*"],               
    allow_headers=["*"],   
)

@router.get("/")
def root():
    return {"success": True}

app.include_router(router)
app.include_router(auth.router)
