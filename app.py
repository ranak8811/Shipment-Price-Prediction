from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
import os
import sys

from shipment.pipline.prediction_pipeline import PredictionPipeline, ShipmentData
from shipment.pipline.training_pipeline import TrainPipeline
from shipment.exception import shippingException
from shipment.logger import logging

app = FastAPI()

# templates ডিরেক্টরি সেটআপ করা
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    try:
        # index.html রেন্ডার করা
        return templates.TemplateResponse("index.html", {"request": request, "context": "None"})
    except Exception as e:
        raise shippingException(e, sys) from e


@app.get("/train")
async def trainRouteClient():
    try:
        # ওয়েব রিকোয়েস্টের মাধ্যমে মডেল ট্রেনিং পাইপলাইন রান করার রুট
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        return {"message": "Training successful!"}
    except Exception as e:
        return {"message": f"Training failed: {e}"}


@app.post("/predict", response_class=HTMLResponse)
async def predict_route(
    request: Request,
    artist_reputation: float = Form(...),
    height: float = Form(...),
    width: float = Form(...),
    weight: float = Form(...),
    material: str = Form(...),
    price_of_sculpture: float = Form(...),
    base_shipping_price: float = Form(...),
    international: str = Form(...),
    express_shipment: str = Form(...),
    installation_included: str = Form(...),
    transport: str = Form(...),
    fragile: str = Form(...),
    customer_information: str = Form(...),
    remote_location: str = Form(...),
):
    try:
        # ১. সাবমিট করা ফর্ম ডাটা থেকে ShipmentData অবজেক্ট তৈরি
        shipment_data = ShipmentData(
            artist_reputation=artist_reputation,
            height=height,
            width=width,
            weight=weight,
            material=material,
            price_of_sculpture=price_of_sculpture,
            base_shipping_price=base_shipping_price,
            international=international,
            express_shipment=express_shipment,
            installation_included=installation_included,
            transport=transport,
            fragile=fragile,
            customer_information=customer_information,
            remote_location=remote_location
        )
        
        # ২. ডাটাসেট রো ডাটায় রূপান্তর
        df = shipment_data.get_data_as_dataframe()
        
        # ৩. প্রেডিকশন রান করা
        predict_pipeline = PredictionPipeline()
        predictions = predict_pipeline.predict(df)
        
        # ৪. প্রেডিকশন কস্ট ২ দশমিক পর্যন্ত রাউন্ড করে ফরম্যাট করা
        cost = round(predictions[0], 2)
        
        # ৫. রেন্ডার করে ব্রাউজারে পাঠানো
        return templates.TemplateResponse(
            "index.html", 
            {"request": request, "cost": f"${cost:.2f}", "context": "Predicted"}
        )
        
    except Exception as e:
        logging.error(f"Prediction failed: {e}")
        return templates.TemplateResponse(
            "index.html", 
            {"request": request, "cost": f"Prediction failed: {e}", "context": "Error"}
        )

if __name__ == "__main__":
    # পোর্ট ৮০৮০ এ সার্ভার রান করা
    uvicorn.run(app, host="0.0.0.0", port=8080)