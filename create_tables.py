from app.db.base_class import Base
import app.db.base
from app.db.session import engine

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")
