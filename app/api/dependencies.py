from sqlalchemy.orm import Session
from fastapi import Request, HTTPException, status, Depends
from app.core.security import verify_token
from app.schemas.user import UserOut
from app.db.crud.user import get_user_by_email
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from typing import Generator
from app.db.deps import get_db
        
async def get_current_user(request: Request, db: Session = Depends(get_db)) -> UserOut:
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not Autneticated")
    
    token_data = verify_token(token)
    email: str = token_data.get("sub")
    user_doc = get_user_by_email(db, email)
    if not user_doc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    
    
    return UserOut(**user_doc)

