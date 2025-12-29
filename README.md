# Insurance Premium Rating Engine

A FastAPI-based machine learning service that predicts insurance premiums based on user input. The application uses a LightGBM model trained on historical insurance data to provide instant premium quotes.

## Overview

This rating engine provides an API endpoint that calculates insurance premiums based on driver, vehicle, and policy information. It's designed to be deployed on Render and integrated with a frontend application.

## System Architecture

```
┌─────────────────────┐
│   Frontend (UI)     │
│  - User Form        │
│  - Input Validation │
│  - Display Quote    │
└──────────┬──────────┘
           │ POST /predict
           │ (JSON Payload)
           ▼
┌─────────────────────┐
│  Render Deployment  │
│  ┌───────────────┐  │
│  │   FastAPI     │  │
│  │   - Router    │  │
│  │   - Validation│  │
│  └───────────────┘  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   ML Model Engine   │
│  ┌───────────────┐  │
│  │ LightGBM      │  │
│  │ - Prediction  │  │
│  │ - Calculation │  │
│  └───────────────┘  │
└──────────┬──────────┘
           │ Premium Quote
           ▼
┌─────────────────────┐
│  Response to UI     │
│  {predicted_premium}│
└─────────────────────┘
```

## Features

- ✅ Real-time premium prediction
- ✅ LightGBM machine learning model
- ✅ Pydantic schema validation
- ✅ Categorical feature handling
- ✅ RESTful API with FastAPI
- ✅ Ready for Render deployment

## Project Structure

```
rating-engine/
├── model/
│   └── model.joblib              # Trained LightGBM model
├── notebooks/
│   └── modeling.ipynb            # Model training notebook
├── src/
│   ├── app.py                    # FastAPI application
│   ├── config.py                 # Configuration & environment
│   ├── database.py               # Database utilities
│   └── rating_engine/
│       ├── model/
│       │   └── input_schema.py   # Pydantic models
│       └── routes/
│           └── api.py            # API endpoints
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
└── README.md                     # This file
```

## Installation

### Prerequisites

- Python 3.8+
- pip or conda

### Local Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd rating-engine
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # or
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**

   ```bash
   cp .env.example .env
   # Edit .env with your Supabase credentials
   ```

5. **Run the application**

   ```bash
   uvicorn src.app:app --reload
   ```

   API will be available at: `http://127.0.0.1:8000`
   API Documentation: `http://127.0.0.1:8000/docs`

## API Documentation

### Endpoint: POST `/predict`

Predicts the insurance premium based on user input.

**Request Body:**

```json
{
  "driver_age": 35,
  "gender": "M",
  "martial_status": "Single",
  "occupation": "Engineer",
  "employment_status": "Employed",
  "income_band": "30000-50000",
  "licence_years": 10,
  "vehicle_make": "Toyota",
  "vehicle_year": 2020,
  "vehicle_body_type": "Sedan",
  "fuel_type": "Petrol",
  "gearbox_type": "Manual",
  "engine_cc": 1600,
  "abi_group": 5,
  "car_value": 15000.0,
  "car_value_to_income_proxy": 0.5,
  "cover_type": "Comprehensive",
  "use_type": "Commute",
  "annual_mileage": 12000,
  "overnight_parking": "Garage",
  "voluntary_excess": 500,
  "payment_method": "Monthly",
  "urban_flag": 1,
  "monthly_pay_flag": 1
}
```

**Response:**

```json
{
  "predicted_premium": 1250.5
}
```

### Endpoint: GET `/`

Health check endpoint.

**Response:**

```json
{
  "message": "Application is running!"
}
```

## Input Parameters

| Parameter                 | Type  | Description                       |
| ------------------------- | ----- | --------------------------------- |
| driver_age                | int   | Age of the driver                 |
| gender                    | str   | Gender (M/F)                      |
| martial_status            | str   | Marital status                    |
| occupation                | str   | Driver's occupation               |
| employment_status         | str   | Employment type                   |
| income_band               | str   | Annual income range               |
| licence_years             | int   | Years holding a license           |
| vehicle_make              | str   | Car manufacturer                  |
| vehicle_year              | int   | Year of manufacture               |
| vehicle_body_type         | str   | Body type (Sedan, SUV, etc.)      |
| fuel_type                 | str   | Fuel type (Petrol, Diesel, etc.)  |
| gearbox_type              | str   | Transmission type (Manual/Auto)   |
| engine_cc                 | int   | Engine displacement               |
| abi_group                 | int   | ABI group rating                  |
| car_value                 | float | Vehicle value in currency         |
| car_value_to_income_proxy | float | Car value to income ratio         |
| cover_type                | str   | Insurance coverage type           |
| use_type                  | str   | Primary vehicle use               |
| annual_mileage            | int   | Annual miles/km driven            |
| overnight_parking         | str   | Parking location                  |
| voluntary_excess          | int   | Excess amount chosen              |
| payment_method            | str   | Payment frequency                 |
| urban_flag                | int   | 1 if urban, 0 if rural            |
| monthly_pay_flag          | int   | 1 if monthly payment, 0 otherwise |

## Deployment on Render

### Steps to Deploy

1. **Push to GitHub**

   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Render Service**

   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Select the repository and branch

3. **Configure Service**

   - **Name**: `rating-engine`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn src.app:app --host 0.0.0.0`
   - **Instance Type**: Free (or Paid as needed)

4. **Set Environment Variables**

   - Add the following in Render dashboard:
     - `SUPABASE_URL`: Your Supabase URL
     - `SUPABASE_KEY`: Your Supabase API key
     - `TABLE_NAME`: Your database table name

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy on every push to main

### API URL After Deployment

Your API will be available at: `https://your-service-name.onrender.com`

## Integration with Frontend

### Example Frontend Request (JavaScript/React)

```javascript
async function getPremiumQuote(formData) {
  const response = await fetch(
    "https://your-service-name.onrender.com/predict",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }
  );

  const result = await response.json();
  return result.predicted_premium;
}
```

### Display Quote on UI

```javascript
const premium = await getPremiumQuote(userFormData);
document.getElementById("quote").innerHTML = `
  <h2>Your Premium Quote</h2>
  <p class="price">£${premium.toFixed(2)}</p>
`;
```

## Model Information

- **Algorithm**: LightGBM Regressor
- **Features**: 23 input features
- **Target**: Quoted Premium (continuous value)
- **Training Data**: Historical insurance data from Supabase
- **Model File**: `model/model.joblib` (serialized using joblib)

## Training the Model

To retrain the model with new data:

1. Open `notebooks/modeling.ipynb`
2. Update data source if needed
3. Run all cells
4. Model will be saved to `model/model.joblib`
5. Commit and push changes to GitHub
6. Render will automatically redeploy

## Environment Variables

Create a `.env` file:

```
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_api_key
TABLE_NAME=your_table_name
```

## Dependencies

- fastapi - Web framework
- uvicorn - ASGI server
- pydantic - Data validation
- pandas - Data manipulation
- scikit-learn - ML utilities
- lightgbm - ML model
- joblib - Model serialization
- pydantic-settings - Settings management

See `requirements.txt` for full list and versions.

## Troubleshooting

### Model Prediction Error: "categorical_feature do not match"

- Ensure all categorical columns are converted to `category` dtype
- Check that categorical column names match those used during training

### 422 Unprocessable Content

- Verify all required fields are included in the request
- Check data types match the schema

### Import Errors

- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`

## Performance Metrics

- **Model R² Score**: ~0.85 (on test set)
- **Response Time**: <100ms average
- **Inference Time**: <10ms

## License

This project is private and proprietary.

## Support

For issues or questions, please contact the development team.
