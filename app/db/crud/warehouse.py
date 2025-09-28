from sqlalchemy.orm import Session
from app.db.models.warehouse import WareHouse
from app.schemas.warehouse import WareHouseCreate, WareHouseUpdate

def get_warehouse_by_id(db: Session, warehouse_id: int) -> WareHouse | None:
    return db.query(WareHouse).filter(WareHouse.id == warehouse_id).first()

def get_warehouses(db: Session, skip: int = 0, limit: int =100) -> list[WareHouse]:
    return db.query(WareHouse).offset(skip).limit(limit).all()

def create_warehouse(db: Session, warehouse_in: WareHouseCreate) -> WareHouse:
    db_warehouse = WareHouse(
        name=warehouse_in.name,
        location=warehouse_in.location,
    )
    db.add(db_warehouse)
    db.commit()
    db.refresh(db_warehouse)
    return db_warehouse

def update_warehouse(db: Session, warehouse_id: int, warehouse_in: WareHouseUpdate) -> WareHouse | None:
    warehouse = db.query(WareHouse).filter(WareHouse.id == warehouse_id).first()
    if not warehouse:
        return None
    
    for field, value in ['name', 'location']:
        value = getattr(warehouse_in, field, None)
        if value is not None:
            setattr(warehouse, field, value)

        db.commit()
        db.refresh(warehouse)
        return warehouse


def delete_warehouse(db: Session, warehouse_id: int) -> None:
    warehouse = db.query(WareHouse).filter(WareHouse.id == warehouse_id).first()
    if warehouse:
        db.delete(warehouse)
        db.commit()