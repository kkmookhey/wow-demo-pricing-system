"""FastAPI entry point for the pricing-system demo app."""
from fastapi import FastAPI
from services.pricing import make_pricing_chain

app = FastAPI(title="Pricing System")


@app.get("/price/{product}")
def price(product: str) -> dict:
    chain = make_pricing_chain()
    return {"product": product, "price_suggestion": chain.run(product=product)}
