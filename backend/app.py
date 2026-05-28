import os

import stripe
from flask import Flask, jsonify


app = Flask(__name__)

# Security: keep this value only in your backend hosting environment.
# Never place a Stripe secret key in frontend HTML, CSS, or JavaScript.
stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

YOUR_DOMAIN = os.environ.get("YOUR_DOMAIN", "https://your-domain.example")


@app.post("/create-checkout-session")
def create_checkout_session():
    """Create one Stripe Checkout Session and return its hosted checkout URL."""
    session = stripe.checkout.Session.create(
        mode="payment",
        payment_method_types=["card"],
        customer_creation="always",
        phone_number_collection={"enabled": True},
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "unit_amount": 2000,  # $20.00
                    "product_data": {
                        "name": "Valtori Security - Remote IT Support",
                        "description": "Remote troubleshooting and technical assistance session.",
                    },
                },
                "quantity": 1,
            }
        ],
        success_url=f"{YOUR_DOMAIN}/after-purchase.html?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{YOUR_DOMAIN}/shop.html",
    )

    return jsonify({"url": session.url})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=4242, debug=False)
