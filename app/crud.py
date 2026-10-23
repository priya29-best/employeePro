from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    # Check: Email already hai kya?
    existing = db.query(models.Employee).filter(models.Employee.email == employee.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    db_emp = models.Employee(**employee.model_dump())
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

def get_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee_by_id(db: Session, emp_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail=f"Employee with id {emp_id} not found")
    return emp

def delete_employee(db: Session, emp_id: int):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(emp)
    db.commit()
    return {"message": f"Employee {emp_id} deleted"}

def update_employee(db: Session, emp_id: int, updated_data: schemas.EmployeeCreate):
    emp = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Not found")
    
    # Naya data purane par daal do
    for key, value in updated_data.model_dump().items():
        setattr(emp, key, value)
    
    db.commit()
    db.refresh(emp)
    return emp