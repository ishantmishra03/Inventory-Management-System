import uvicorn
from app.core.config import PORT
from app.db.session import engine
from app.db.base_class import Base

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=PORT, reload=True)