from pydantic import BaseModel

class PremiumPredict(BaseModel):
    driver_age: int
    gender: str
    martial_status: str
    occupation: str
    employment_status: str          
    income_band: str                 
    licence_years: int               
    vehicle_make: str                
    vehicle_year: int                
    vehicle_body_type: str           
    fuel_type: str                   
    gearbox_type: str                
    engine_cc: int                   
    abi_group: int                   
    car_value: float                   
    car_value_to_income_proxy: float   
    cover_type: str                  
    use_type: str                    
    annual_mileage: int              
    overnight_parking: str           
    voluntary_excess: int            
    payment_method: str              
    urban_flag: int                  
    monthly_pay_flag: int            
        