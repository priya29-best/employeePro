from pydantic import BaseModel, EmailStr
from typing import Optional

# 1. Bouncer for CREATE - Kya chahiye jab naya employee banao?
class EmployeeCreate(BaseModel):
    name: str
    email: EmailStr  # Auto check karega email sahi hai ya nahi
    department: str
    salary: float

    # Extra check: naam khali nahi hona chahiye
    # Pydantic v2 mein Field use karte hain
    # Lekin abhi simple rakhte hain

# 2. Bouncer for RESPONSE - DB se kya dikhana hai user ko?
class EmployeeResponse(BaseModel):
    id: int
    name: str
    email: str
    department: str
    salary: float

    class Config:
        from_attributes = True  # Ye jadu hai - DB ke object ko JSON mein badal dega

# 3. Bouncer for UPDATE - Sab optional hai
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None