from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    table_name: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings= Settings()

# Categorical columns for model prediction
CATEGORICAL_COLUMNS = [
    "gender", "martial_status", "occupation", "employment_status",
    "income_band", "vehicle_make", "vehicle_body_type", "fuel_type",
    "gearbox_type", "cover_type", "use_type", "overnight_parking", "payment_method"
]