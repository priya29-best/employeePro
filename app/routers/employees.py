from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, crud

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=schemas.EmployeeResponse)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db=db, employee=employee)

@router.get("/", response_model=list[schemas.EmployeeResponse])
def get_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db=db)

@router.get("/{emp_id}", response_model=schemas.EmployeeResponse)
def get_one_employee(emp_id: int, db: Session = Depends(get_db)):
    return crud.get_employee_by_id(db=db, emp_id=emp_id)

@router.delete("/{emp_id}")
def delete_emp(emp_id: int, db: Session = Depends(get_db)):
    return crud.delete_employee(db=db, emp_id=emp_id)

@router.put("/{emp_id}", response_model=schemas.EmployeeResponse)
def update_emp(emp_id: int, employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.update_employee(db=db, emp_id=emp_id, updated_data=employee)