from pydantic import BaseModel, EmailStr
from datetime import date, datetime

class UserData(BaseModel):
    title: str
    first_name: str
    last_name: str
    email_address: EmailStr
    date_of_birth: date
    sex: bool
    nationality: str
    marital_status: str
    employment_status: str
    job_title: str
    occupation: str
    car_make: str
    car_model: str
    abi_group: int
    transmission: str
    vechile_usage: str
    parking: str
    driving_licence_type: str
    driving_licence_years: int
    licence_issue_country: str
    number_of_ncd_years: int
    number_of_past_claims: int
    number_of_ccjs: int
    medical_conditions: str
    cover_type: str
    start_date: date
    estimated_annual_mileage: int
    payment_frequency: str
    personal_injury_cover: bool
    breakdown_cover: bool
    courtesy_car: bool
    quoted_total_permium: int
    status: str
    created_at: datetime
    