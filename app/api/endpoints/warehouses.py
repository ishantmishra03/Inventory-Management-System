from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.warehouse import WareHouseCreate, WareHouseUpdate, WareHouseOut
from app.db.crud import warehouse as crud_warehouse
from app.db.deps import get_db

router = APIRouter(prefix="/api/warehouses", tags=["warehouses"])

@router.get("/", response_model=List[WareHouseOut])
def list_warehouses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    warehouses = crud_warehouse.get_warehouses(db, skip=skip, limit=limit)
    return {"success": True, "warehouses": warehouses}

@router.get("/{warehouse_id}", response_model=WareHouseOut)
def get_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse = crud_warehouse.get_warehouse_by_id(db, warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")
    return {"success": True, "warehouse": warehouse}

@router.post("/", response_model=WareHouseOut, status_code=status.HTTP_201_CREATED)
def create_warehouse(warehouse_in: WareHouseCreate, db: Session = Depends(get_db)):
    warehouse = crud_warehouse.create_warehouse(db, warehouse_in)
    return {"success": True, "message": "Warehouse created"}

@router.put("/{warehouse_id}", response_model=WareHouseOut)
def update_warehouse(warehouse_id: int, warehouse_in: WareHouseUpdate, db: Session = Depends(get_db)):
    warehouse = crud_warehouse.update_warehouse(db, warehouse_id, warehouse_in)
    if not warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")
    return {"success": True, "message": "Warehouse updated"}

@router.delete("/{warehouse_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warehouse(warehouse_id: int, db: Session = Depends(get_db)):
    warehouse = crud_warehouse.get_warehouse_by_id(db, warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")
    crud_warehouse.delete_warehouse(db, warehouse_id)
    return None  
