from typing import List, Optional
from pydantic import BaseModel, Field, validator
import re
from .review import Review
from .order import Order

class CustomerBase(BaseModel):
    name: str
    phone: str
    address: str
    is_guest: bool
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None
    
    @validator('phone')
    def validate_phone_number(cls, v):
        """Validate phone number format"""
        # Remove any non-digit characters for validation
        digits_only = re.sub(r'\D', '', v)
        
        # Check if the result has a valid number of digits (10-15)
        if len(digits_only) < 10 or len(digits_only) > 15:
            raise ValueError('Phone number must have between 10 and 15 digits')
        
        # Optional: Check for specific country formats
        # This example validates US numbers (10 digits)
        if len(digits_only) == 10 and not digits_only.startswith(('0', '1')):
            return v
            
        # For international numbers, just ensure it has enough digits
        return v
    
    @validator('address')
    def validate_address(cls, v):
        """Validate address format and content"""
        # Check for minimum content (should contain numbers and letters)
        if not re.search(r'\d', v):
            raise ValueError('Address should contain at least one number')
        
        if not re.search(r'[a-zA-Z]', v):
            raise ValueError('Address should contain letters')
        
        # Basic sanity check for address parts
        parts = v.split(',')
        if len(parts) < 2:
            raise ValueError('Address should contain street and city, separated by commas')
            
        return v
    
    @validator('name')
    def validate_name(cls, v):
        """Validate name format"""
        # Check that name contains only letters, spaces, hyphens, and apostrophes
        if not re.match(r'^[a-zA-Z\s\'-]+$', v):
            raise ValueError('Name should contain only letters, spaces, hyphens, and apostrophes')
            
        # Check that name has at least a first and last name
        parts = v.strip().split()
        if len(parts) < 2:
            raise ValueError('Please provide both first and last name')
            
        return v

class CustomerCreate(CustomerBase):
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    is_guest: Optional[bool] = None
    # last_order_id: Optional[int] = None
    # last_payment_id: Optional[int] = None
    
    @validator('phone')
    def validate_phone_number(cls, v):
        if v is None:
            return v
            
        # Remove any non-digit characters for validation
        digits_only = re.sub(r'\D', '', v)
        
        # Check if the result has a valid number of digits (10-15)
        if len(digits_only) < 10 or len(digits_only) > 15:
            raise ValueError('Phone number must have between 10 and 15 digits')
            
        return v
    
    @validator('address')
    def validate_address(cls, v):
        if v is None:
            return v
            
        # Check for minimum content (should contain numbers and letters)
        if not re.search(r'\d', v):
            raise ValueError('Address should contain at least one number')
        
        if not re.search(r'[a-zA-Z]', v):
            raise ValueError('Address should contain letters')
            
        return v
    
    @validator('name')
    def validate_name(cls, v):
        if v is None:
            return v
            
        # Check that name contains only letters, spaces, hyphens, and apostrophes
        if not re.match(r'^[a-zA-Z\s\'-]+$', v):
            raise ValueError('Name should contain only letters, spaces, hyphens, and apostrophes')
            
        return v


class Customer(CustomerBase):
    id: int
    # last_order_id: Optional[int]
    # last_payment_id: Optional[int]
    review: Optional[Review] = None
    order: Optional[Order] = None

    class Config:
        from_attributes = True

