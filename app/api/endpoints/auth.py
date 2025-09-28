from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserLogin, UserOut
from app.db.crud import user as crud_user
from app.core import security
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.api.dependencies import get_current_user
from app.db.deps import get_db

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register(user_in: UserCreate, response: Response, db: Session = Depends(get_db)):
    if crud_user.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud_user.create_user(db, user_in)

    token = security.create_access_token(data={"sub": user.email})

    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        secure=False, 
        samesite="lax",
        max_age=60 * ACCESS_TOKEN_EXPIRE_MINUTES,
        path="/",
    )

    return {"success": True, "message": "Registered Successfully"}


@router.post("/login")
def register(user_in: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = crud_user.authenticate_user(db, user_in.email, user_in.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    token = security.create_access_token(data={"sub": user.email})

    response.set_cookie(
        key="token",
        value=token,
        httponly=True,
        secure=False, 
        samesite="lax",
        max_age=60 * ACCESS_TOKEN_EXPIRE_MINUTES,
        path="/",
    )

    return {"success": True, "message": "Login Successfully"}

@router.post("/logout")
def logout(response: Response, current_user=Depends(get_current_user)):
    response.delete_cookie(key="token", path="/")
    return {"success": "true", "message": "Logged out"}

@router.get("/me", response_model=UserOut)
def read_current_user(current_user=Depends(get_current_user)):
    return current_user